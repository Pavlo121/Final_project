# Generated by Django 5.1.4 on 2025-01-24 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='manager_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]