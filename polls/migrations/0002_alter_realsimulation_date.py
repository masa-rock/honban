# Generated by Django 3.2 on 2021-05-04 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realsimulation',
            name='date',
            field=models.DateField(),
        ),
    ]
