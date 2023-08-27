# Generated by Django 4.2.2 on 2023-08-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=80)),
            ],
            options={
                'verbose_name': 'info',
                'verbose_name_plural': 'infos',
            },
        ),
    ]