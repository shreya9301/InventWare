# Generated by Django 3.1rc1 on 2020-09-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(blank=True, choices=[('Food', 'Food'), ('Healthcare', 'Healthcare'), ('Textiles', 'Textiles')], max_length=50, null=True),
        ),
    ]
