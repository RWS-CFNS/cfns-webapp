# Generated by Django 3.2 on 2021-05-18 12:16

from django.db import migrations, models
import fontawesome_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', fontawesome_5.fields.IconField(blank=True, max_length=60)),
            ],
        ),
    ]