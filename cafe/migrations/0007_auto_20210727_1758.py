# Generated by Django 3.1.7 on 2021-07-27 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0006_auto_20210727_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailystatement',
            name='timestamp',
            field=models.DateField(auto_now_add=True, unique=True, verbose_name='Date'),
        ),
    ]
