# Generated by Django 5.0 on 2024-01-05 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0009_order_orderid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
