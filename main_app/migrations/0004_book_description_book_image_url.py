# Generated by Django 4.2.1 on 2023-06-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_child_user_alter_book_age_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(default='Description', max_length=300),
        ),
        migrations.AddField(
            model_name='book',
            name='image_url',
            field=models.CharField(default='Description', max_length=300),
        ),
    ]
