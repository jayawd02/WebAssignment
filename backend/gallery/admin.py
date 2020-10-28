from django.contrib import admin
from .models import Video, Recipe, Post, PostComment


class VideoAdmin(admin.ModelAdmin):
    fields =['title','type','description','thumbnail','link','posted_by']
    list_display=('title','description','type','posted_by','date_posted')
    list_filter = ['type','date_posted']
    search_fields = ['title','type']

class RecipeAdmin(admin.ModelAdmin):
    fields = ['name', 'type','category','prep_time', 'description','ingredients', 'recipe_image', 'posted_by']
    list_display = ('name', 'type','category','prep_time', 'posted_by', 'date_posted')
    list_filter = ['type','category', 'date_posted']
    search_fields = ['name','type']


class PostAdmin(admin.ModelAdmin):
    fields = ['posted_by','content', 'image']
    list_display = ('posted_by','date_posted','content')
    list_filter = ['posted_by', 'date_posted']
    search_fields = ['content']



class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name',  'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

# Register your models here.
admin.site.register (Video,VideoAdmin)
admin.site.register (Recipe, RecipeAdmin)
admin.site.register (Post,PostAdmin)
admin.site.register (PostComment,PostCommentAdmin)
