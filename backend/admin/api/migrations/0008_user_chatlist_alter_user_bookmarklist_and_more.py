# Generated by Django 5.1 on 2024-09-28 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_user_bookmarklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chatList',
            field=models.JSONField(default=[], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bookMarkList',
            field=models.JSONField(default=[], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ratingList',
            field=models.JSONField(default=[], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ratings',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='uploads',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='viewList',
            field=models.JSONField(default=[], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='views',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]
