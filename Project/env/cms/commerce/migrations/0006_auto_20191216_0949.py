# Generated by Django 3.0 on 2019-12-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0005_auto_20191216_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='Price',
            field=models.FloatField(default=0, max_length=10),
        ),
    ]
