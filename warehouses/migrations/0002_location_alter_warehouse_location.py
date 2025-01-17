# Generated by Django 5.1.4 on 2025-01-14 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('exact_location', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='warehouses.location'),
        ),
    ]
