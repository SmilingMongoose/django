# Generated by Django 4.0.4 on 2023-08-04 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_ticker_dates_alter_ticker_price_close_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticker',
            name='volume',
            field=models.TextField(null=True),
        ),
    ]