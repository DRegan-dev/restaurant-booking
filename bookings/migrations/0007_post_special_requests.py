# Generated by Django 4.2.11 on 2024-03-07 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_post_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='special_requests',
            field=models.TextField(null=True),
        ),
    ]
