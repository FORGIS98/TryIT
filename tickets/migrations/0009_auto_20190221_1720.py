# Generated by Django 2.1.7 on 2019-02-21 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20190216_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validator',
            name='volunteer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='volunteers.Volunteer'),
        ),
    ]