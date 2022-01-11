# Generated by Django 4.0 on 2022-01-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('distance', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
