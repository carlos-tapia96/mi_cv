# Generated by Django 4.2.5 on 2023-09-06 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_cv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='score',
            field=models.IntegerField(blank=True, default=80, null=True),
        ),
    ]
