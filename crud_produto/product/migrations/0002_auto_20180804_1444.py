# Generated by Django 2.1rc1 on 2018-08-04 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('nome',)},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='nome',
        ),
    ]