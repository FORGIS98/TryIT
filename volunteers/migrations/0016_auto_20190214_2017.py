# Generated by Django 2.1.7 on 2019-02-14 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0015_auto_20190214_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='id',
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='identity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='tickets.Attendant'),
        ),
    ]
