# Generated by Django 3.0.7 on 2020-06-24 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20200624_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default='Aurangabad'),
        ),
    ]
