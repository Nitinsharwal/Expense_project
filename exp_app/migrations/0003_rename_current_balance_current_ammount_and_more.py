# Generated by Django 4.2 on 2025-07-13 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exp_app', '0002_current_balance_tracker_delete_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='current_balance',
            new_name='current_ammount',
        ),
        migrations.RenameField(
            model_name='current_ammount',
            old_name='current_ammount',
            new_name='current_balance',
        ),
        migrations.RenameField(
            model_name='tracker',
            old_name='current_ammount',
            new_name='current_balance',
        ),
    ]
