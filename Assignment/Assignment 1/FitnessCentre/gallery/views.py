from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import PostCreateForm
from .models import Post, Video, Recipe
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # to chk whether user is logged in


class PostListView(ListView):
    model = Post
    # template_name = 'gallery/post_list.html'  # instead of post_list.html redirecting to post_list.html
    # context_object_name = 'posts'  # instead of calling the object in html
    ordering = ['-date_posted']  # order the posts newest at top
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content', 'image']

    def form_valid(self, form):  # pass the current logged in user as author to the model
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


# def post_create(request):
#     if request.method == "POST":
#         post_create_form = PostCreateForm(request.POST, request.FILES, instance=request.user)
#         if post_create_form.is_valid():
#             post_create_form.save()
#             messages.success(request, f'Your post has been created!')
#             # return redirect('post-list')
#
#     else:
#         post_create_form = PostCreateForm(instance=request.user)
#
#     context = {
#         'form': post_create_form,
#     }
#     return render(request, 'gallery/post_form.html', context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                     UpdateView):  # test whether user is logged in and as same as te authour of the post
    model = Post
    fields = ['content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
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
    ordering = ['title']
    paginate_by = 10


class VideoDetailView(DetailView):
    model = Video


class RecipeListView(ListView):
    model = Recipe
    ordering = ['name']
    paginate_by = 10


class RecipeDetailView(DetailView):
    model = Recipe
