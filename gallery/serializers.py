from rest_framework import serializers
from gallery.models import Video, Post, Recipe, PostComment, PostLike, PostDislike


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        exclude = ['date_posted', 'posted_by']


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ['date_posted', 'posted_by']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['date_posted', 'author']


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        exclude = ['created_on']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike


class PostDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostDislike
