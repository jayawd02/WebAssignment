from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin #to chk whether user is logged in


# Create your views here.

# def posts(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'gallery/posts.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'gallery/posts.html'  # instead of post_list.html redirecting to posts.html
    context_object_name = 'posts'  # instead of calling the object in html
    ordering = ['-date_posted']  # order the posts newest at top


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): # pass the current logged in user as author to the model
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):  # test whether user is logged in and as same as te authour of the post
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # checking user is same as author
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False
