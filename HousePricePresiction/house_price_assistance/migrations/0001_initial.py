# Generated by Django 5.0 on 2023-12-24 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredictPriceModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=100)),
                ('predict_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('room', models.IntegerField()),
                ('state', models.CharField(max_length=100)),
            ],
        ),
    ]