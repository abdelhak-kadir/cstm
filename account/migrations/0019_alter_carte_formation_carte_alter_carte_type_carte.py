# Generated by Django 4.2.3 on 2023-08-05 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_carte_cni_alter_carte_nom_alter_carte_prenom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carte',
            name='formation_carte',
            field=models.CharField(choices=[('FIMO', 'FIMO'), ('FCO', 'FCO')], max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='carte',
            name='type_carte',
            field=models.CharField(choices=[('سيارات الأجرة', 'سيارات الأجرة'), ('نقل البضائع', 'نقل البضائع'), ('النقل الجماعي', 'النقل الجماعي'), ('TGR/TLS', 'TGR/TLS')], max_length=200, null=True, unique=True),
        ),
    ]
