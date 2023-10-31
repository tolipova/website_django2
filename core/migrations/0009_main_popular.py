# Generated by Django 4.2.6 on 2023-10-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_posts_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_Popular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='user_info/')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('little_info', models.CharField(max_length=255)),
                ('big_info', models.TextField()),
            ],
        ),
    ]
