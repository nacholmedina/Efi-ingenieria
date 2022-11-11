# Generated by Django 2.2.7 on 2019-11-27 05:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carrera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('lastname', models.CharField(max_length=254)),
                ('age', models.CharField(max_length=254)),
                ('gender', models.CharField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='career', to='carrera.Carrera')),
            ],
            options={
                'db_table': 'registro',
            },
        ),
    ]