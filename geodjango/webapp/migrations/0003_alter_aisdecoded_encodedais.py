# Generated by Django 3.2 on 2021-06-24 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20210624_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aisdecoded',
            name='encodedAIS',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.ais'),
        ),
    ]
