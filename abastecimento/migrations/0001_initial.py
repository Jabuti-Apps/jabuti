# Generated by Django 5.0.1 on 2024-04-02 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('veiculos', '0005_veiculo_ultimalavagem_alter_veiculo_alugado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abastecer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorpago', models.FloatField()),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veiculos.veiculo')),
            ],
        ),
    ]