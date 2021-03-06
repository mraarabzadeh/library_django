# Generated by Django 3.0.6 on 2020-05-30 07:12

import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='book',
            managers=[
                ('AllBook', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='libraryadmin',
            managers=[
                ('MostDeliver', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='reservehistory',
            managers=[
                ('ReservedBookSpecialTimeRange', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('DidNotGetBook', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='reservehistory',
            old_name='time',
            new_name='end_time',
        ),
        migrations.AddField(
            model_name='reservehistory',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 30, 11, 42, 38, 772995)),
        ),
    ]
