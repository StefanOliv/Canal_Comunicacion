# Generated by Django 4.1.5 on 2023-02-27 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_comunicacion', '0008_archivoprivado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivopublico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filegroup', models.FileField(null=True, upload_to='archivos/grupales')),
            ],
        ),
        migrations.RemoveField(
            model_name='archivoprivado',
            name='filegroup',
        ),
        migrations.AddField(
            model_name='archivoprivado',
            name='filepriv',
            field=models.FileField(null=True, upload_to='archivos/privados'),
        ),
    ]
