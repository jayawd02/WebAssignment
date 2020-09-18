from django.contrib.auth.models import User
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from gallery.forms import PostCreateForm
from gallery.views import post_detail, PostListView, PostCreateView, PostUpdateView, PostDeleteView
from gallery.models import Post, PostComment, PostLike, PostDislike


# Create your tests here.
class PostListViewTests(TestCase):
    def test_no_postlist(self):
        response = self.client.get('post-list')
        self.assertEqual(response.status_code, 404)


class VideoListViewTests(TestCase):
    def test_no_videolist(self):
        response = self.client.get('video-list')
        self.assertEqual(response.status_code, 404)


class RecipeListViewTests(TestCase):
    def test_no_recipelist(self):
        response = self.client.get('recipe-list')
        self.assertEqual(response.status_code, 404)


class TestUrls(SimpleTestCase):
    def test_post_list_url_resolves(self):
        url = reverse('post-list')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_post_detail_url_resolves(self):
        url = reverse('post-detail', args=['199'])
        self.assertEquals(resolve(url).func, post_detail)

    def test_post_create_url_resolves(self):
        url = reverse('post-create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_post_update_url_resolves(self):
        url = reverse('post-update', args=['199'])
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_post_delete_url_resolves(self):
        url = reverse('post-delete', args=['199'])
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(id=1, first_name='Test', last_name='test', username='user1')
        self.post1 = Post.objects.create(id=1, content='This is test', author=self.user)
        self.post_list_url = reverse('post-list')
        self.post_detail_url = reverse('post-detail', args=[1])
        self.post_delete_url = reverse('post-delete', args=[1])
        self.post_create_url = reverse('post-create')

    def test_post_list_GET(self):
        response = self.client.get(self.post_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/post_list.html')


    def test_post_detail_POST_no_data(self):
        response = self.client.post(self.post_detail_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.post1.comments.count(), 0)


class TestModels(TestCase):
    def setUp(self):
        self.user3 = User.objects.create(id=3, first_name='Test', last_name='test', username='user3')
        self.user4 = User.objects.create(id=4, first_name='Test', last_name='test', username='user4')
        self.post3 = Post.objects.create(id=3, content='This is test post 3', author=self.user3)
        self.post4 = Post.objects.create(id=4, content='This is test post 4', author=self.user4)

    def test_post_total_likes(self):
        users_set = [self.user3, self.user4]
        postlike = PostLike.objects.create(post=self.post3)
        postlike.users.set(users_set)
        self.assertEquals(self.post3.get_total_likes(), 2)

    def test_post_total_dislikes(self):
        users_set = [self.user3, self.user4]
        postdislike = PostDislike.objects.create(post=self.post4)
        postdislike.users.set(users_set)
        self.assertEquals(self.post4.get_total_dislikes(), 2)


class TestForms(SimpleTestCase):

    def test_post_create_form_valid_data(self):
        form = PostCreateForm(data={'content': 'Test post'})
        self.assertTrue(form.is_valid())

    def test_post_create_form_no_data(self):
        form = PostCreateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)