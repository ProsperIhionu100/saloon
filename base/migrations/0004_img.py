# Generated by Django 5.0 on 2023-12-11 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_employee_service_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='')),
                ('about', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
