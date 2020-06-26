# Generated by Django 3.0.7 on 2020-06-24 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_order_cust_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='descrip',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='food',
            name='per',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='biryani',
            field=models.IntegerField(default=0, verbose_name='No. of biryani plates(Rs. 50 per plate)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='chicken',
            field=models.IntegerField(default=0, verbose_name='No. of packet of fried chicken(Rs. 75 per packet. Each packet contains one quarter of a chicken)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cust_id',
            field=models.IntegerField(default=0, verbose_name='Mobile No.'),
        ),
    ]
