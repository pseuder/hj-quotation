# Generated by Django 2.2.4 on 2022-04-01 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('remark', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'Attachment',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'Unit',
            },
        ),
    ]
