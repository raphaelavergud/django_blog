# Generated by Django 4.0 on 2022-01-21 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='blog.newuser'),
        ),
    ]
