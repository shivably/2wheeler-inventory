# Generated by Django 4.0.5 on 2023-02-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('2_WHEELER', '2 Wheeler'), ('4_WHEELER', '4 Wheeler'), ('OTHER', 'Other')], default='2_WHEELER', max_length=20)),
            ],
        ),
    ]
