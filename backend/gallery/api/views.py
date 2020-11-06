from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin  # to chk whether user is logged in
from sentry_sdk import capture_exception
from rest_framework import viewsets
from rest_framework import permissions
from gallery.models import Post, Video, Recipe,PostComment, PostDislike, PostLike
from .serializers import PostSerializer,VideoSerializer,RecipeSerializer,PostCommentSerializer,PostLikeSerializer,PostDislikeSerializer
from .permissions import IsOwnerOrReadOnly



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]
    #
    # def perform_create(self, serializer):
    #     serializer.save(posted_by=self.request.user)



class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.AllowAny]
    ##permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                         ## IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

class PostCommentViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(name=self.request.user)

class PostLikeViewset(viewsets.ModelViewSet):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(users=self.request.user)

class PostDislikeViewset(viewsets.ModelViewSet):
    queryset = PostDislike.objects.all()
    serializer_class = PostDislikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(users=self.request.user)


#todo Need to serialize
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
