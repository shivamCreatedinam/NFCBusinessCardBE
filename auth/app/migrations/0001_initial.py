# Generated by Django 5.0.6 on 2024-06-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
    ]
