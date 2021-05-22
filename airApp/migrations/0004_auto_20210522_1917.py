# Generated by Django 3.2.3 on 2021-05-22 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airApp', '0003_auto_20210522_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='house', to='airApp.user'),
        ),
        migrations.AlterField(
            model_name='house',
            name='roomtype',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='house', to='airApp.housetype'),
        ),
    ]
