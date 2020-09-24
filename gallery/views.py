from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.views.generic.base import View

from .forms import PostCreateForm, VideoCreateFormSet, PostCommentForm
from .models import Post, Video, Recipe, PostDislike, PostLike
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # to chk whether user is logged in
from django.views.generic.edit import FormView
from sentry_sdk import capture_exception


class PostListView(ListView):
    model = Post
    ordering = ['-date_posted']  # order the posts newest at top
    paginate_by = 10


@login_required
def post_detail(request, post_id):
    template_name = 'gallery/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.exclude(active=False).order_by('created_on')
    new_comment = None

    if request.method == 'POST':
        comment_form = PostCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            comment_form.instance.name = request.user
            new_comment.post = post
            new_comment.name = request.user
            new_comment.save()
            messages.success(request, f'Your comment has been send to administrator to approve')
            comment_form = PostCommentForm()
    else:
        comment_form = PostCommentForm()

    context = {'post': post,
               'comments': comments,
               'new_comment': new_comment,
               'form': comment_form}
    return render(request, template_name, context)




class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'gallery/post_form.html'
    form_class = PostCreateForm

    def form_valid(self, form):  # pass the current logged in user as author to the model
        form.instance.author = self.request.user
        form.save()
        messages.success(self.request, f'Your post has been created!')
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                     UpdateView):  # test whether user is logged in and as same as te authour of the post
    model = Post
    fields = ['content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Your post has been updated!')
        return super().form_valid(form)

    def test_func(self):  # checking user is same as author
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class VideoListView(ListView):
    model = Video
    ordering = ['-date_posted']
    paginate_by = 10


class VideoDetailView(DetailView):
    model = Video


# class VideoCreateView(LoginRequiredMixin, CreateView):
#     model = Video
#     fields = ['title', 'description', 'type', 'thumbnail', 'link']
#
#     def form_valid(self, form):
#         form.instance.posted_by = self.request.user
#         messages.success(self.request, f'Your video has been added!')
#         return super(VideoCreateView, self).form_valid(form)

# formset create video
class VideoCreateView(FormView):
    template_name = 'gallery/video_form.html'
    form_class = VideoCreateFormSet
    success_url = '/'

    def form_valid(self, form):  # pass the current logged in user as author to the model
        for form in form:
            if form.instance.title != "":
                form.instance.posted_by = self.request.user
                form.save()
        messages.success(self.request, f'Your video(s) has been added!')
        return super(VideoCreateView, self).form_valid(form)


class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                      UpdateView):  # test whether user is logged in and as same as the authour of the post
    model = Video
    fields = ['title', 'description', 'type', 'thumbnail', 'link']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        messages.success(self.request, f'Your video has been updated!')
        return super().form_valid(form)

    def test_func(self):  # checking user is same as author
        video = self.get_object()
        if self.request.user == video.posted_by:
            return True
        return False


class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    success_url = '/'

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.posted_by:
            return True
        return False


class RecipeListView(ListView):
    model = Recipe
    ordering = ['-date_posted']
    paginate_by = 10


class RecipeDetailView(DetailView):
    model = Recipe


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name', 'type', 'category', 'description', 'recipe_image', 'ingredients', 'prep_time']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        messages.success(self.request, f'Your recipe has been created!')
        return super(RecipeCreateView, self).form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                       UpdateView):  # test whether user is logged in and as same as the authour of the post
    model = Recipe
    fields = ['name', 'type', 'category', 'description', 'recipe_image', 'ingredients', 'prep_time']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        messages.success(self.request, f'Your recipe has been updated!')
        return super().form_valid(form)

    def test_func(self):  # checking user is same as author
        recipe = self.get_object()
        if self.request.user == recipe.posted_by:
            return True
        return False


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = '/'

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.posted_by:
            return True
        return False


class UpdatePostVote(LoginRequiredMixin, View):
    template_name = 'gallery/post_detail.html'


    def get(self, request, *args, **kwargs):

        post_id = self.kwargs.get('post_id', None)
        opinion = self.kwargs.get('opinion', None) # like or dislike button clicked

        post = get_object_or_404(Post, id=post_id)

        try:
            post.dislikes
        except Post.dislikes.RelatedObjectDoesNotExist as identifier:
            PostDislike.objects.create(post = post)
            capture_exception(identifier)

        try:
            post.likes
        except Post.likes.RelatedObjectDoesNotExist as identifier:
            PostLike.objects.create(post = post)
            capture_exception(identifier)

        if opinion.lower() == 'like':

            if request.user in post.likes.users.all():
                post.likes.users.remove(request.user)
            else:
                post.likes.users.add(request.user)
                post.dislikes.users.remove(request.user)

        elif opinion.lower() == 'dislike':

            if request.user in post.dislikes.users.all():
                post.dislikes.users.remove(request.user)
            else:
                post.dislikes.users.add(request.user)
                post.likes.users.remove(request.user)
        else:
            return HttpResponseRedirect(reverse('post-detail',kwargs={'post_id':post.id} ))
        return HttpResponseRedirect(reverse('post-detail', kwargs={'post_id':post.id} ))
