# Generated by Django 4.1.4 on 2023-02-02 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmediadb', '0003_remove_followuser_user_remove_like_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='', upload_to='img_post/%y/%m'),
        ),
    ]
