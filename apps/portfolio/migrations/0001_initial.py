# Generated by Django 3.0.3 on 2020-02-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('preview_image', models.FilePathField(path='/img')),
                ('reference_link', models.URLField(max_length=250)),
            ],
        ),
    ]
