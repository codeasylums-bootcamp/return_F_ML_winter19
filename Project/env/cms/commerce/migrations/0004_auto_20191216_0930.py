# Generated by Django 3.0 on 2019-12-16 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_auto_20191216_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='Price',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
