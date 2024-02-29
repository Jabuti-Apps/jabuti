# Generated by Django 5.0.1 on 2024-02-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manutencao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manutencao',
            name='data',
        ),
        migrations.AddField(
            model_name='manutencao',
            name='dataEntrada',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manutencao',
            name='dataSaida',
            field=models.DateField(blank=True, null=True),
        ),
    ]
