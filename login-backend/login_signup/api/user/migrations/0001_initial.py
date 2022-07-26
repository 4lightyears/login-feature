# Generated by Django 4.0.5 on 2022-07-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(blank=True, max_length=80)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('phone_number', models.CharField(blank=True, max_length=12)),
                ('session_token', models.CharField(default=0, max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'user',
            },
        ),
    ]
