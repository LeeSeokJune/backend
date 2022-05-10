# Generated by Django 4.0.4 on 2022-05-09 06:56

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_pet', models.CharField(default='강아지', max_length=20)),
                ('p_name', models.CharField(max_length=100)),
                ('p_brand', models.CharField(max_length=100)),
                ('p_large_category', models.CharField(blank=True, max_length=100)),
                ('p_medium_category', models.CharField(blank=True, max_length=100)),
                ('p_small_category1', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, size=None)),
                ('p_small_category2', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, size=None)),
                ('p_small_category3', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, size=None)),
                ('p_small_category4', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, size=None)),
                ('p_small_category5', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, size=None)),
                ('p_small_category6', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, size=None)),
                ('p_small_category7', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, size=None)),
                ('p_small_category8', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, size=None)),
                ('p_ratail_price', models.IntegerField(blank=True)),
                ('p_wholesale_price', models.IntegerField(blank=True)),
                ('p_product_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]