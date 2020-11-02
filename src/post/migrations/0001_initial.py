# Generated by Django 3.1.1 on 2020-09-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('ranking', models.FloatField(default=0)),
                ('director', models.CharField(max_length=100)),
                ('cast', models.CharField(max_length=100)),
                ('budget', models.FloatField(default=0)),
                ('runtime', models.FloatField(default=0)),
                ('cum_worldwide_gross', models.FloatField(default=0)),
            ],
        ),
    ]
