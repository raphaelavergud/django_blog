from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, UserManager

class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# class User(AbstractBaseUser):
#     objects = UserManager()

#     def create_superuser(self, username, email, password):
#         return self._create_user(username, email, password)