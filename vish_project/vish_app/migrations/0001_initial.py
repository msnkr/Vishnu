# Generated by Django 4.0.5 on 2022-06-17 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=50)),
                ('product_description', models.TextField()),
                ('product_price', models.FloatField()),
                ('product_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
