# Generated by Django 5.1 on 2024-09-28 00:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=500)),
                ('file', models.FileField(upload_to='documents/')),
                ('uploadedAt', models.DateTimeField(auto_now_add=True)),
                ('rating', models.CharField(max_length=100, null=True)),
                ('views', models.CharField(max_length=100, null=True)),
                ('downloads', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]
