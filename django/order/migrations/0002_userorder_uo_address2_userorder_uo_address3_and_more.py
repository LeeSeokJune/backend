# Generated by Django 4.0.4 on 2022-05-24 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='uo_address2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userorder',
            name='uo_address3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='uo_address1',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
