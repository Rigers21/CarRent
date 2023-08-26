# Generated by Django 4.2.4 on 2023-08-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.BigIntegerField()),
                ('fuel', models.CharField(max_length=50)),
                ('price', models.BigIntegerField()),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
