# Generated by Django 4.2.3 on 2023-07-19 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
