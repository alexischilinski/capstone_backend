# Generated by Django 3.0.3 on 2020-03-04 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running', '0024_message_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='race_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
