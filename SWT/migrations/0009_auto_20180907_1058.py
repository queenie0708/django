# Generated by Django 2.1 on 2018-09-07 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SWT', '0008_auto_20180907_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='prj',
            name='id',
            field=models.AutoField(default='0', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='prj',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
