# Generated by Django 4.2.3 on 2023-08-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_carte'),
    ]

    operations = [
        migrations.AddField(
            model_name='carte',
            name='nom',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='carte',
            name='prenom',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
