# Generated by Django 3.0.4 on 2020-10-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20201028_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='acceptedcrypto',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
