# Generated by Django 5.0 on 2023-12-07 17:19

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('Title', models.CharField(blank=True, max_length=200, null=True)),
                ('service_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
