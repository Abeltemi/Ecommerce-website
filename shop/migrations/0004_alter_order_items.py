# Generated by Django 4.2 on 2023-05-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.CharField(max_length=1000),
        ),
    ]