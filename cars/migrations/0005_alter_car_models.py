# Generated by Django 4.1.5 on 2023-02-11 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_carmodel_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='models',
            field=models.ManyToManyField(blank=True, null=True, related_name='car_names', to='cars.carmodel'),
        ),
    ]