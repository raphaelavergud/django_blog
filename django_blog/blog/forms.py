from hashlib import sha256
from django import forms

# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm

from .models import Blog, NewUser


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

    def save(self, commit=True):
        post = super(NewPostForm, self).save()
        if commit:
            post.save()
        return post


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
