# Generated by Django 5.0.3 on 2024-03-29 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_auction', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='conditon',
            new_name='condition',
        ),
    ]