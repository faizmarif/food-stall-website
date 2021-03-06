# Generated by Django 3.0.7 on 2020-06-24 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='chatni',
            field=models.IntegerField(default=0, verbose_name='No. of packet of chatni'),
        ),
        migrations.AddField(
            model_name='order',
            name='salad',
            field=models.IntegerField(default=0, verbose_name='No. of packet of salad'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(default='', verbose_name='Full Address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='biryani',
            field=models.IntegerField(default=0, verbose_name='No. of biryani plates'),
        ),
        migrations.AlterField(
            model_name='order',
            name='chicken',
            field=models.IntegerField(default=0, verbose_name='No. of packet of fried chicken'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cust_id',
            field=models.IntegerField(null=True, verbose_name='Mobile No.'),
        ),
    ]
