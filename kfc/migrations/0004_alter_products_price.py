# Generated by Django 4.0.5 on 2022-06-30 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kfc', '0003_alter_products_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=255),
        ),
    ]
