from django import forms

# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm

from .models import NewUser


# Create your forms here.


class NewUserForm(forms.ModelForm):
    class Meta:
        model = NewUser
        widgets = {
            "password": forms.PasswordInput(),
        }
        fields = ["email", "username", "password", "first_name"]

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


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
