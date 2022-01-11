from django.contrib import admin
from .models import Blog, Run


class BlogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)
admin.site.register(Run, BlogAdmin)
