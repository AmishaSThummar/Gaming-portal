# Generated by Django 4.0.1 on 2022-07-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gamers_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('tetrisMaxScore', models.BigIntegerField()),
            ],
        ),
    ]