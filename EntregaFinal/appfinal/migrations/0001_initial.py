# Generated by Django 4.1.3 on 2022-11-16 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=40)),
                ('profesion', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreempresa', models.CharField(max_length=40)),
                ('descempresa', models.CharField(max_length=120)),
                ('ofertaactiva', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reclutadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('manager', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Recomendadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=40)),
                ('itrecruiter', models.BooleanField(default=False)),
            ],
        ),
    ]
