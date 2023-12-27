# Generated by Django 4.2.4 on 2023-08-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donate', '0036_video_delete_vide'),
    ]

    operations = [
        migrations.CreateModel(
            name='blood_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media/')),
                ('content', models.CharField(max_length=2000)),
            ],
        ),
    ]