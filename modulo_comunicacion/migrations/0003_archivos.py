# Generated by Django 4.1.5 on 2023-02-12 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_comunicacion', '0002_mensajes_canal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='modelo_comunicacion/archivos/')),
                ('mensajes_canal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_comunicacion.mensajes_canal')),
            ],
        ),
    ]