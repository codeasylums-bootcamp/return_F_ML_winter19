# Generated by Django 3.0 on 2019-12-15 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='Price',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
