# Generated by Django 5.0.1 on 2024-06-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='Destino',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='Origem',
            field=models.CharField(max_length=200),
        ),
    ]