# Generated by Django 3.2 on 2022-10-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20220925_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]