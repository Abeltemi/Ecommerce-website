# Generated by Django 4.2 on 2023-05-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.CharField(default='product', max_length=1000),
        ),
    ]