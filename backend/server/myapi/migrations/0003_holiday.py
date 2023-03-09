# Generated by Django 3.1.2 on 2021-02-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_events_event_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.CharField(max_length=60)),
                ('end_date', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=60)),
            ],
        ),
    ]
