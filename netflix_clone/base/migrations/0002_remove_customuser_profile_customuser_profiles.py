# Generated by Django 4.1.7 on 2023-06-23 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile',
        ),
        migrations.AddField(
            model_name='customuser',
            name='profiles',
            field=models.ManyToManyField(to='base.profile'),
        ),
    ]
