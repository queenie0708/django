# Generated by Django 2.1 on 2018-08-31 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SWT', '0004_auto_20180831_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='result_url',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='result',
            name='type_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='version',
            name='lastupdate',
            field=models.DateTimeField(null=True),
        ),
    ]