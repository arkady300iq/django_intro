# Generated by Django 5.0.6 on 2024-06-24 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_published_date_blog_published_dat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='published_dat',
            new_name='published_date',
        ),
    ]
