# Generated by Django 5.0 on 2023-12-24 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_price_assistance', '0002_alter_predictpricemodel_predict_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictpricemodel',
            name='predict_price',
            field=models.CharField(max_length=100),
        ),
    ]