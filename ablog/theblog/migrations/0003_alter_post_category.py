# Generated by Django 4.0.6 on 2022-07-23 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_remove_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Coding', max_length=100),
        ),
    ]
