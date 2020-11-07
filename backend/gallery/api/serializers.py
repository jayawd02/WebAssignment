from rest_framework import serializers
from gallery.models import Video, Post, Recipe, PostComment, PostLike, PostDislike
from users.models import Profile


class VideoSerializer(serializers.ModelSerializer):
    ##posted_by = serializers.ReadOnlyField(source='posted_by.first_name')
    #profile_pic = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all())

    class Meta:
        model = Video
        exclude = ['date_posted']


class RecipeSerializer(serializers.ModelSerializer):
    ##posted_by = serializers.ReadOnlyField(source='posted_by.first_name')

    class Meta:
        model = Recipe
        exclude = ['date_posted']


class PostSerializer(serializers.ModelSerializer):
    ##posted_by = serializers.ReadOnlyField(source='posted_by.first_name')
    posted_by=serializers.CharField(source='posted_by.first_name')
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=PostComment.objects.all())
    #likes = serializers.PrimaryKeyRelatedField(many=True,queryset=PostLike.objects.all())
    #dislikes = serializers.PrimaryKeyRelatedField(many=True,queryset=PostDislike.objects.all())

    class Meta:
        model = Post
       # fields = ['content','posted_by','image','comments','likes','dislikes']
        exclude = ['date_posted']


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
