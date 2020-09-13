from django import forms
from django.forms import formset_factory

from gallery.models import Post, Video, PostComment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 25}),
        }


PostCreateFormSet = formset_factory(PostCreateForm, extra=2, max_num=2, min_num=1)


class VideoCreateForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'type',  'link','thumbnail']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }


VideoCreateFormSet = formset_factory(VideoCreateForm, extra=3, max_num=3, min_num=1)



class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = [ 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }