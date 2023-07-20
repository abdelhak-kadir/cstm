# Generated by Django 4.2.3 on 2023-07-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('prenom', models.CharField(max_length=200, null=True)),
                ('cni', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('type_colis', models.CharField(max_length=200, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('from_colis', models.CharField(max_length=100, null=True)),
                ('to_colis', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='order_europ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('prenom', models.CharField(max_length=200, null=True)),
                ('cni', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('contry', models.CharField(choices=[('FR', 'France'), ('IT', 'Italie'), ('BE', 'Belgique'), ('DE', 'Allemagne'), ('NL', 'Holanda'), ('UK', 'Engletere')], max_length=100, null=True)),
                ('type_colis', models.CharField(max_length=200, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('from_colis', models.CharField(max_length=100, null=True)),
                ('to_colis', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('prenom', models.CharField(max_length=200, null=True)),
                ('nickname', models.CharField(max_length=200, null=True)),
                ('cni', models.CharField(max_length=200, null=True)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('weight', models.CharField(choices=[('3.5t-bache', '3.5t Bachè'), ('3.5t-plateau', '3.5t Plateau'), ('3.5t-plateau-ridal', '3.5t Plateau Ridal'), ('3.5t-avec-grue', '3.5t Avec Grue'), ('3.5t-fourgon', '3.5t Fourgon'), ('7.5t-bache', '7.5t Bachè'), ('7.5t-plateau', '7.5t Plateau'), ('7.5t-plateau-ridal', '7.5t Plateau Ridal'), ('7.5t-avec-grue', '7.5t Avec Grue'), ('7.5t-fourgon', '7.5t Fourgon'), ('10t-bache', '10t Bachè'), ('10t-plateau', '10t Plateau'), ('10t-plateau-ridal', '10t Plateau Ridal'), ('10t-avec-grue', '10t Avec Grue'), ('10t-fourgon', '10t Fourgon'), ('14t-bache', '14t Bachè'), ('14t-plateau', '14t Plateau'), ('14t-plateau-ridal', '14t Plateau Ridal'), ('14t-avec-grue', '14t Avec Grue'), ('14t-fourgon', '14t Fourgon'), ('19t-bache', '19t Bachè'), ('19t-plateau', '19t Plateau'), ('19t-plateau-ridal', '19t Plateau Ridal'), ('19t-avec-grue', '19t Avec Grue'), ('19t-fourgon', '19t Fourgon')], max_length=20, null=True)),
            ],
        ),
    ]
