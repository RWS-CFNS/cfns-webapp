# Generated by Django 3.2 on 2021-08-25 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210825_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lorawanmodel',
            name='alt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
