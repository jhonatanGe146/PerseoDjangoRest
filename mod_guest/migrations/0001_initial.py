# Generated by Django 4.2.7 on 2023-12-04 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Huesped',
            fields=[
                ('numero_documento', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=70)),
                ('apellido', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
    ]
