# Generated by Django 4.2.2 on 2023-06-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blog_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover',
            field=models.ImageField(default='default.jpg', upload_to='cover-photos'),
        ),
    ]
