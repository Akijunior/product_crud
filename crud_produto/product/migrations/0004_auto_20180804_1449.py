# Generated by Django 2.1rc1 on 2018-08-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantidade',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
