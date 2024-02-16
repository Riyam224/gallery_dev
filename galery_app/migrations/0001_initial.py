# Generated by Django 5.0.2 on 2024-02-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallerys',
            },
        ),
    ]
