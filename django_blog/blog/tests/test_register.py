#!/usr/bin/env python3

from blog.models import CustomAccountManager
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager
from django.test import TestCase
from django.urls import reverse

class ViewBaseTest(TestCase):
    def setUp(self):
        self.register_url=reverse('register')

        return super().setUp()

class RegisterViewTest(ViewBaseTest):
    def test_can_view_registerpage_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/register.html')

class RegisterTestCase(TestCase):
    def setUp(self):
        pass

    def test_value_error_when_email_is_none(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                username="Raphiie", first_name="Test", email=None, password="se"
            )

    def test_value_error_when_email_is_empty(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                username="Raphiie", first_name="Test", email="", password="se"
            )

    def test_user_registration(self):
        username = "Raphiie"
        first_name = "Test"
        email = "test@test.com"
        password = "se"
        user = get_user_model().objects.create_user(
            username=username, first_name=first_name, email=email, password=password
        )
        self.assertEquals(user.username, username)
        self.assertEquals(user.first_name, first_name)
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)


class SuperUserTestCase(TestCase):
    def setUp(self):
        pass

    def test_value_error_when_email_is_none(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(
                username="Raphiie", first_name="Test", email=None, password="se"
            )

    def test_value_error_when_email_is_empty(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(
                username="Raphiie", first_name="Test", email="", password="se"
            )

    def test_value_error_when_is_staff_false(self):
        username = "Raphiie"
        first_name = "Test"
        email = "test@test.com"
        password = "se"
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_superuser(
                username=username,
                first_name=first_name,
                email=email,
                password=password,
                is_staff=False,
            )

    def test_value_error_when_is_superuser_false(self):
        username = "Raphiie"
        first_name = "Test"
        email = "test@test.com"
        password = "se"
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_superuser(
                username=username,
                first_name=first_name,
                email=email,
                password=password,
                is_superuser=False,
            )

    def test_superuser_registration(self):
        username = "Raphiie"
        first_name = "Test"
        email = "test@test.com"
        password = "se"
        user = get_user_model().objects.create_superuser(
            username=username, first_name=first_name, email=email, password=password
        )
        self.assertEquals(user.username, username)
        self.assertEquals(user.first_name, first_name)
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)
