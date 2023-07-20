from django.db import models
from datetime import datetime

# Create your models here.
class person(models.Model):
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=200 , null=True)
    prenom = models.CharField(max_length=200, null=True)
    nickname = models.CharField(max_length=200, null=True)
    cni = models.CharField(max_length=200, null=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, null=True , choices=gender)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True)
    weight_choices=(
         ('3.5t-bache', '3.5t Bachè'),
        ('3.5t-plateau', '3.5t Plateau'),
        ('3.5t-plateau-ridal', '3.5t Plateau Ridal'),
        ('3.5t-avec-grue', '3.5t Avec Grue'),
        ('3.5t-fourgon', '3.5t Fourgon'),
        ('7.5t-bache', '7.5t Bachè'),
        ('7.5t-plateau', '7.5t Plateau'),
        ('7.5t-plateau-ridal', '7.5t Plateau Ridal'),
        ('7.5t-avec-grue', '7.5t Avec Grue'),
        ('7.5t-fourgon', '7.5t Fourgon'),
        ('10t-bache', '10t Bachè'),
        ('10t-plateau', '10t Plateau'),
        ('10t-plateau-ridal', '10t Plateau Ridal'),
        ('10t-avec-grue', '10t Avec Grue'),
        ('10t-fourgon', '10t Fourgon'),
        ('14t-bache', '14t Bachè'),
        ('14t-plateau', '14t Plateau'),
        ('14t-plateau-ridal', '14t Plateau Ridal'),
        ('14t-avec-grue', '14t Avec Grue'),
        ('14t-fourgon', '14t Fourgon'),
        ('19t-bache', '19t Bachè'),
        ('19t-plateau', '19t Plateau'),
        ('19t-plateau-ridal', '19t Plateau Ridal'),
        ('19t-avec-grue', '19t Avec Grue'),
        ('19t-fourgon', '19t Fourgon'),
    )
    weight = models.CharField(max_length=20 , null=True, choices=weight_choices)
    published_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + " " + self.prenom
    
class order(models.Model):
    name = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    cni = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    type_colis = models.CharField(max_length=200, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    from_colis = models.CharField(max_length=100, null=True)
    to_colis = models.CharField(max_length=100, null=True)
    published_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + " " + self.prenom
    
class order_europ(models.Model):
    contry_choices=(
        ('France', 'France'),
        ('Italie', 'Italie'),
        ('Belgique', 'Belgique'),
        ('Allemagne', 'Allemagne'),
        ('Holanda', 'Holanda'),
        ('Engletere', 'Engletere'),
    )
    name = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    cni = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=20 , null=True)
    phone_number = models.CharField(max_length=20, null=True)
    contry = models.CharField(max_length=20, null=True , choices=contry_choices)
    type_colis = models.CharField(max_length=200, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    from_colis = models.CharField(max_length=100, null=True)
    to_colis = models.CharField(max_length=100, null=True)
    published_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + " " + self.prenom
    
class adminstation(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username
    

class news(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    link = models.CharField(max_length=300)
    published_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title