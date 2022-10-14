# Generated by Django 4.0.4 on 2022-10-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputEmpresa', models.CharField(blank=True, max_length=255, null=True)),
                ('inputCNPJ', models.CharField(blank=True, max_length=18, null=True)),
                ('inputEmail', models.EmailField(blank=True, max_length=100, null=True)),
                ('inputTel', models.CharField(blank=True, max_length=13, null=True)),
                ('inputCel', models.CharField(blank=True, max_length=14, null=True)),
                ('inputAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('inputNumber', models.PositiveIntegerField(blank=True, null=True)),
                ('inputAddress2', models.CharField(blank=True, max_length=100, null=True)),
                ('inputCEP', models.CharField(blank=True, max_length=9, null=True)),
                ('inputCity', models.CharField(blank=True, max_length=50, null=True)),
                ('inputEstado', models.CharField(blank=True, max_length=20, null=True)),
                ('inputTipo', models.BooleanField(blank=None, null=None)),
            ],
        ),
    ]
