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
    ordering = ['-date_posted']
    paginate_by = 10


class VideoDetailView(DetailView):
    model = Video

class VideoCreateView(LoginRequiredMixin,CreateView):
    model = Video
    fields = ['title', 'description','type', 'thumbnail','link']

    def form_valid(self, form):
        form.instance.posted_by= self.request.user
        return super(VideoCreateView, self).form_valid(form)

class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                     UpdateView):  # test whether user is logged in and as same as the authour of the post
    model = Video
    fields = ['title', 'description','type', 'thumbnail','link']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
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
    fields = ['name', 'type', 'category', 'description', 'recipe_image','ingredients','prep_time']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super(RecipeCreateView, self).form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                      UpdateView):  # test whether user is logged in and as same as the authour of the post
    model = Recipe
    fields = ['name', 'type', 'category', 'description', 'recipe_image', 'ingredients', 'prep_time']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
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
