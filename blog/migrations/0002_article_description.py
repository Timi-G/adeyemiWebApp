# Generated by Django 5.2 on 2025-04-21 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="description",
            field=models.TextField(default="..."),
            preserve_default=False,
        ),
    ]
