# Generated by Django 3.2 on 2022-10-18 09:00

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('town_or_city', models.CharField(max_length=40)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('description', models.TextField(default=False)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('genre', models.ManyToManyField(to='about.Genre')),
                ('instrument', models.ManyToManyField(to='about.Instrument')),
            ],
        ),
    ]
