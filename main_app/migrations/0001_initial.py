# Generated by Django 4.0.4 on 2023-08-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entered_visitor_name', models.CharField(max_length=200)),
            ],
        ),
    ]
