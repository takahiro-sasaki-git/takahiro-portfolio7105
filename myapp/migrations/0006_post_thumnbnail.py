# Generated by Django 3.2.2 on 2021-06-14 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumnbnail',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
