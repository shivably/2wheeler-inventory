# Generated by Django 4.0.5 on 2023-02-28 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_alter_newstockmodel_manufacturing_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstockmodel',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]