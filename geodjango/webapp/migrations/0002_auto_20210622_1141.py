# Generated by Django 3.2 on 2021-06-22 11:41

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='aisDecoded',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('encodedAIS', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='webapp.ais')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('received_from', models.CharField(max_length=128)),
                ('received_at', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='ais',
            options={},
        ),
        migrations.AddField(
            model_name='ais',
            name='received_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
