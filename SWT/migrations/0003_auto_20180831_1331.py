# Generated by Django 2.1 on 2018-08-31 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SWT', '0002_auto_20180831_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prj',
            name='dut_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='prj',
            name='sku_id',
            field=models.CharField(max_length=30),
        ),
    ]
