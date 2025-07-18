# Generated by Django 4.2 on 2025-07-14 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exp_app', '0003_rename_current_balance_current_ammount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='ammount',
            field=models.FloatField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='current_balance',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='exp_app.current_ammount'),
        ),
    ]
