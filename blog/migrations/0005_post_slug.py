# Generated by Django 3.1.1 on 2020-09-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200915_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=220),
            preserve_default=False,
        ),
    ]
