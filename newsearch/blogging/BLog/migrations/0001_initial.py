# Generated by Django 5.0.1 on 2024-02-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=550)),
            ],
        ),
    ]
