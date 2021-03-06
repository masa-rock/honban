# Generated by Django 3.2 on 2021-05-04 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Realsimulation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=255)),
                ('open', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('currency', models.IntegerField(blank=True, null=True)),
                ('code', models.CharField(max_length=255)),
                ('rsi', models.FloatField(blank=True, null=True)),
                ('days50', models.FloatField(blank=True, null=True)),
                ('days150', models.FloatField(blank=True, null=True)),
                ('days200', models.FloatField(blank=True, null=True)),
                ('weeks20', models.FloatField(blank=True, null=True)),
                ('stdev', models.FloatField(blank=True, null=True)),
                ('bb', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
    ]
