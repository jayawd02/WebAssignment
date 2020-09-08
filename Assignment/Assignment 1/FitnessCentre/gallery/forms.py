from django import forms
from django.forms import formset_factory

from gallery.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']


PostCreateFormSet = formset_factory(PostCreateForm, extra=2, max_num=2, min_num=1)
