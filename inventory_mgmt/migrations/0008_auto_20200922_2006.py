# Generated by Django 3.1rc1 on 2020-09-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_mgmt', '0007_stock_export_to_csv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='export_to_CSV',
            field=models.BooleanField(null=True),
        ),
    ]