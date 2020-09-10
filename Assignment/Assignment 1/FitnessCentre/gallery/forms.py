from django import forms
from django.forms import formset_factory

from gallery.models import Post, Video


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']


PostCreateFormSet = formset_factory(PostCreateForm, extra=2, max_num=2, min_num=1)


class VideoCreateForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'type',  'link','thumbnail']


VideoCreateFormSet = formset_factory(VideoCreateForm, extra=3, max_num=3, min_num=1)
