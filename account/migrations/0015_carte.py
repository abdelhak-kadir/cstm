# Generated by Django 4.2.3 on 2023-08-05 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_order_europ_contry_alter_order_europ_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='carte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_carte', models.CharField(choices=[('سيارات الأجرة', 'سيارات الأجرة'), ('نقل البضائع', 'نقل البضائع'), ('النقل الجماعي', 'النقل الجماعي'), ('TGR/TLS', 'TGR/TLS')], max_length=200, null=True)),
                ('formation_carte', models.CharField(choices=[('FIMO', 'FIMO'), ('FCO', 'FCO')], max_length=200, null=True)),
                ('permis', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/')),
                ('visite_medicale', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/')),
                ('phone', models.CharField(max_length=100, null=True)),
                ('ville', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
