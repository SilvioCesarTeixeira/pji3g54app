# Generated by Django 4.1.2 on 2022-11-10 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pji3g54app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='inputCPF',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='inputNome',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='inputPF',
            field=models.BooleanField(blank=None, default=False, null=None),
        ),
    ]
