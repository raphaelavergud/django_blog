#!/usr/bin/env python3

from django.test import TestCase
from blog.models import Blog


class SimpleTest(TestCase):
    def setUp(self):
        self.user = Blog.objects.create_superuser(username='testuser', password='password')

    def tearDown(self):
        self.user.delete()

    def test_add_blog_post(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post('/admin/blog/django_blog/add/', {'title': 'TEST TITLE', 'body': 'SOME BODY', '_save': 'SAVE'})
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/')
        self.assertTrue('TEST TITLE' in str(response.content))