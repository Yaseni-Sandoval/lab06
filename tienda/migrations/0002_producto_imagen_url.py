# Generated by Django 5.0.4 on 2024-04-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
