# Generated by Django 3.1 on 2020-09-19 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200919_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='notes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
