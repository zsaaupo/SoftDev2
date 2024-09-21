# Generated by Django 5.0 on 2023-12-25 02:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filter', '0002_option_option_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('category', models.ManyToManyField(related_name='product', to='filter.category')),
                ('category_type', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='product_type', to='filter.option')),
            ],
        ),
    ]
