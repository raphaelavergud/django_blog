from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Blog, Run, NewUser
from django.forms import Textarea


class BlogAdmin(admin.ModelAdmin):
    pass


class UserAdminConfig(UserAdmin):

    model = NewUser

    search_fields = ("email", "username", "first_name")
    ordering = ("-start_date",)

    list_display = ("email", "username", "first_name", "is_active", "is_staff")
    list_filter = ("email", "username", "first_name", "is_active", "is_staff")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "username",
                    "first_name",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        ("Personal", {"fields": ("about",)}),
    )

    formfield_overrides = {
        NewUser.about: {"widget": Textarea(attrs={"rows": 10, "cols": 40})},
    }

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Run, BlogAdmin)
admin.site.register(NewUser, UserAdminConfig)
