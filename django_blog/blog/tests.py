#!/usr/bin/env python3

from django.test import TestCase
from django.contrib.auth.models import User


class SimpleTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testuser", password="password"
        )

    def tearDown(self):
        self.user.delete()

# testing adding blog posts.
# working test

    def test_add_blog_post(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(
            "/admin/blog/blog/add/",
            {"title": "TEST TITLE", "body": "SOME BODY", "_save": "SAVE"},
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/")
        self.assertTrue("TEST TITLE" in str(response.content))

# testing whether deleting the first post works
# how do i retrieve the test case

    # def test_delete_blog_post(self):
    #     self.client.login(username="testuser", password="password")
    #     response = self.client.delete(
    #         "/admin/blog/blog/1/delete/",
    #     )
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.get("/admin/blog/blog/4/change/")