# Generated by Django 5.0 on 2023-12-28 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DNISTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dnis', models.CharField(max_length=20)),
                ('queue', models.CharField(max_length=30)),
                ('play_welcome', models.BooleanField()),
                ('prio', models.IntegerField()),
            ],
        ),
    ]
