# Generated by Django 3.1.1 on 2020-09-18 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
        migrations.AddField(
            model_name='post',
            name='visit',
            field=models.IntegerField(default=0),
        ),
    ]
