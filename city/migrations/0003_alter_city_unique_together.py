# Generated by Django 4.1.5 on 2023-02-22 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0002_alter_city_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='city',
            unique_together={('city', 'state_name')},
        ),
    ]