# Generated by Django 3.2.16 on 2024-03-29 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_full_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
