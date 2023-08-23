# Generated by Django 4.2 on 2023-08-02 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=32)),
                ('titulo', models.CharField(max_length=32)),
                ('vimeo_id', models.CharField(max_length=32)),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
