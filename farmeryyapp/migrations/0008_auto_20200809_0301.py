# Generated by Django 3.0.3 on 2020-08-08 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmeryyapp', '0007_product2_proimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product2',
            name='expted_delivery',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='product2',
            name='pre_delivery',
            field=models.DateField(),
        ),
    ]
