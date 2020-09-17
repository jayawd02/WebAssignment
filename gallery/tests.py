from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class PostListViewTests(TestCase):
    def test_no_postlist(self):
        response =self.client.get('post-list')
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No post list")
        self.assertQuerysetEqual(response.context['object_list'], [])

class VideoListViewTests(TestCase):
    def test_no_videolist(self):
        response=self.client.get('video-list')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No videos list")
        self.assertQuerysetEqual(response.context['object_list'], [])


class RecipeListViewTests(TestCase):
    def test_no_recipelist(self):
        response=self.client.get('recipe-list')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No recipes list")
        self.assertQuerysetEqual(response.context['object_list'], [])