# Generated by Django 5.0.7 on 2024-08-08 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Astro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('astronaut', models.CharField(max_length=100, verbose_name='Name')),
                ('bio', models.TextField(verbose_name='Bio')),
                ('photo', models.ImageField(upload_to='', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'new astronaut',
                'verbose_name_plural': 'Astronauts',
            },
        ),
        migrations.CreateModel(
            name='LifeInSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('photos', models.ImageField(upload_to='', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'new fact',
                'verbose_name_plural': 'Life in Space',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Published at')),
                ('photo', models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'News from Nasa',
                'verbose_name_plural': 'Articles',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='UniverseList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space_object', models.CharField(max_length=150, verbose_name='Object')),
                ('read', models.TextField(verbose_name='About')),
                ('photo', models.ImageField(upload_to='', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'new planet',
                'verbose_name_plural': 'SpaceObjects',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spaceship', models.CharField(max_length=100, verbose_name='Vehicle')),
                ('about', models.TextField(verbose_name='About')),
                ('photo', models.ImageField(upload_to='', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'new vehicle',
                'verbose_name_plural': 'Vehicles',
            },
        ),
    ]
