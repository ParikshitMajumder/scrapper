# Generated by Django 3.2.12 on 2023-01-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_name',
            name='Name',
            field=models.CharField(max_length=16000),
        ),
    ]
