# Generated by Django 3.0.6 on 2020-05-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='capitale',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
