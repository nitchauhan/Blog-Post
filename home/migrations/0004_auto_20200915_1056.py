# Generated by Django 3.1.1 on 2020-09-15 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200914_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
