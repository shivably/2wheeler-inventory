# Generated by Django 4.0.5 on 2023-02-28 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newstockmodel',
            name='manufacturing_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='newstockmodel',
            name='registration_date',
            field=models.DateField(default=None),
        ),
    ]
