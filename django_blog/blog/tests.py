#!/usr/bin/env python3

from django.test import TestCase
from django.contrib.auth import get_user_model


class UserAccountTests(TestCase):
    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            "testuser@super.com", "username", "firstname", "password"
        )
        self.assertEqual(super_user.email, "testuser@super.com")
        self.assertEqual(super_user.username, "username")
        self.assertEqual(super_user.first_name, "firstname")
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "username")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="testuser@super.com",
                username="username1",
                first_name="first_name",
                password="password",
                is_superuser=False,
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="testuser@super.com",
                username="username1",
                first_name="first_name",
                password="password",
                is_staff=False,
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="",
                username="username1",
                first_name="first_name",
                password="password",
                is_superuser=True,
            )

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            "testuser@user.com", "username", "firstname", "password"
        )
        self.assertEqual(user.email, "testuser@user.com")
        self.assertEqual(user.username, "username")
        self.assertEqual(user.first_name, "firstname")
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email="", username="a", first_name="first_name", password="password"
            )


# class SimpleTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_superuser(
#             username="testuser", password="password"
#         )

#     def tearDown(self):
#         self.user.delete()

# # testing adding blog posts.
# # working test

#     def test_add_blog_post(self):
#         self.client.login(username="testuser", password="password")
#         response = self.client.post(
#             "/admin/blog/blog/add/",
#             {"title": "TEST TITLE", "body": "SOME BODY", "_save": "SAVE"},
#         )
#         self.assertEqual(response.status_code, 302)
#         response = self.client.get("/")
#         self.assertTrue("TEST TITLE" in str(response.content))

# # testing whether deleting the first post works
# # how do i retrieve the test case

#     def test_delete_blog_post(self):
#         self.client.login(username="testuser", password="password")
#         response = self.client.delete(
#             "/admin/blog/blog/1/delete/",
#         )
#         self.assertEqual(response.status_code, 302)
#         response = self.client.get("/admin/blog/blog/4/change/")

# # class RegisterTest(TestCase):
# #     def user_already_exists(self):
# #         "what if a user with this username already exists"
# #         self.client.register(username in )
