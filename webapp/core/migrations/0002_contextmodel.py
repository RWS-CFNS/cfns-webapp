# Generated by Django 3.2 on 2021-08-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContextModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tentant_id', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
