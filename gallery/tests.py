from django.contrib.auth.models import User
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from gallery.views import post_detail, PostListView, PostCreateView, PostUpdateView, PostDeleteView
from gallery.models import Post, PostComment


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
        self.client=Client()
        self.post_list_url=reverse('post-list')
        self.post_detail_url=reverse('post-detail',args=[999])
        self.user = User.objects.create(id=1, first_name='Test', last_name='test',username='user1')
        self.post999= Post.objects.create(id=999,content='This is test',author=self.user)

    def test_post_list_GET(self):
        response = self.client.get(self.post_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'gallery/post_list.html')

    def test_post_detail_GET(self):
        response = self.client.get(self.post_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/post_detail.html')

    def test_post_detail_POST_add_new_comment(self):
         self.user2= User.objects.create(id=999, first_name='Test2', last_name='test2',username='user2')
         response = self.client.post(self.post_detail_url,{'new_comment':'test comment','name':self.user2,'post':self.post999})
         self.assertEquals(response.status_code,302)
         print(self.post999.comments)
         #self.assertEquals(self.post999.comments.first().comment,'test comment')

    def test_post_detail_POST_no_data(self):
         response = self.client.post(self.post_detail_url )
         self.assertEquals(response.status_code, 302)
         self.assertEquals(self.post999.comments.count(), 0)
