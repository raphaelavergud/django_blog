# Generated by Django 4.0 on 2022-02-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_run_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newuser",
            name="password",
            field=models.CharField(max_length=90),
        ),
    ]
