from hashlib import sha256
from django import forms
from django.http import request

# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm

from .models import Blog, NewUser, Run


# Create your forms here.


class NewUserForm(forms.ModelForm):
    class Meta:
        model = NewUser
        widgets = {
            "password": forms.PasswordInput(),
        }
        fields = ["email", "username", "password", "first_name"]

    def save(self, commit=True):
        user = super(NewUserForm, self).save()
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "body"]

    def __init__(self, *args, **kwargs):
        self.logged_in_user = kwargs.pop("logged_in_user", None)
        super(NewPostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super(NewPostForm, self).save(commit=False)
        post.author_id = self.logged_in_user.id
        if commit:
            post.save()
        return post


class NewRunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = ["title", "distance", "body"]

    def __init__(self, *args, **kwargs):
        self.logged_in_user = kwargs.pop("logged_in_user", None)
        super(NewRunForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        run = super(NewRunForm, self).save(commit=False)
        run.author_id = self.logged_in_user.id
        if commit:
            run.save()
        return run


# class NewUserForm(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta:
# 		model = get_user_model()
# 		fields = ("user_name", "email", "password1", "password2")

# def save(self, commit=True):
# 	user = super(NewUserForm, self).save(commit=False)
# 	user.email = self.cleaned_data['email']
# 	if commit:
# 		user.save()
# 	return user
