# Generated by Django 4.0.6 on 2022-07-24 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link Above to read post..', max_length=100),
        ),
    ]
