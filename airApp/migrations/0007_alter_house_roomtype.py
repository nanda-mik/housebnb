# Generated by Django 3.2.3 on 2021-05-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airApp', '0006_auto_20210524_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='roomtype',
            field=models.ManyToManyField(blank=True, to='airApp.HouseType'),
        ),
    ]