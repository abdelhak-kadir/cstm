# Generated by Django 4.2.3 on 2023-08-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_alter_carte_nom_alter_carte_prenom_alter_person_ice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carte',
            name='cni',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='carte',
            name='nom',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='carte',
            name='prenom',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
