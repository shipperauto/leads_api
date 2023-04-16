# Generated by Django 4.1.5 on 2023-04-11 08:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0006_alter_car_models'),
        ('city', '0004_rename_city_city_city_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_year', models.IntegerField(max_length=4, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2100)])),
                ('pick_up_date', models.DateField(default=django.utils.timezone.now)),
                ('is_operable', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carmodel')),
                ('clients', models.ManyToManyField(related_name='quotes', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='customers.customer')),
                ('drop_off_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drop_off_quotes', to='city.city')),
                ('pick_up_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pick_up_quotes', to='city.city')),
            ],
        ),
    ]