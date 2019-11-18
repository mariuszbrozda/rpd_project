# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-04 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpd_home', '0002_auto_20191102_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation_model_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email_adress', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('street_address1', models.CharField(max_length=40)),
                ('street_address2', models.CharField(max_length=40)),
                ('county', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Quotation_model_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.CharField(blank=True, max_length=20)),
                ('town_or_city', models.CharField(max_length=40)),
                ('Property_type', models.CharField(choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Duplex', 'Duplex'), ('Bungalow', 'Bungalow'), ('Studio', 'Studio'), ('Other', 'Other')], max_length=10)),
                ('Bedrooms_nr', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=10)),
                ('Bathrooms_nr', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=10)),
                ('comments', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Quotation_model',
        ),
    ]