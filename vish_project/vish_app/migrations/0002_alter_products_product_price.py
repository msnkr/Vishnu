# Generated by Django 4.0.5 on 2022-06-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vish_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_price',
            field=models.CharField(max_length=10),
        ),
    ]
