# Generated by Django 3.1rc1 on 2020-09-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_mgmt', '0012_remove_stock_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
