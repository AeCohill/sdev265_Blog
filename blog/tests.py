from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Upvote, Downvote
from django.utils import timezone

class BlogTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create a second user
        self.user2 = User.objects.create_user(username='testuser2', password='testpassword2')
        # Create a test post
        self.post = Post.objects.create(
            author=self.user,
            title='Test Post',
            text='This is a test post',
            created_date=timezone.now(),
            published_date=timezone.now()
        )
        # Set up the client
        self.client = Client()

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertContains(response, 'Test Post')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile', kwargs={'username': self.user.username}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/profile.html')

    def test_author_detail_view(self):
        response = self.client.get(reverse('author_detail', kwargs={'author_id': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/author_detail.html')

    def test_upvote_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('upvote_post', kwargs={'post_id': self.post.pk}))
        self.assertEqual(response.status_code, 302)  # Redirects after upvoting
        self.assertTrue(Upvote.objects.filter(post=self.post, user=self.user).exists())

    def test_downvote_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('downvote_post', kwargs={'post_id': self.post.pk}))
        self.assertEqual(response.status_code, 302)  # Redirects after downvoting
        self.assertTrue(Downvote.objects.filter(post=self.post, user=self.user).exists())

    def test_post_new_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post_new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_edit.html')
        response = self.client.post(reverse('post_new'), {
            'title': 'New Post',
            'text': 'This is a new post',
        })
        self.assertEqual(response.status_code, 302)  # Redirects to post_detail after creation

    def test_post_edit_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post_edit', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_edit.html')
        response = self.client.post(reverse('post_edit', kwargs={'pk': self.post.pk}), {
            'title': 'Edited Post',
            'text': 'This is an edited post',
        })
        self.assertEqual(response.status_code, 302)  # Redirects to post_detail after editing

    def test_my_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('my_profile'))
        self.assertEqual(response.status_code, 302)  # Redirects to profile

    def test_post_delete_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post_delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 302)  # Redirects to post_list after deletion
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
