# Generated by Django 3.1 on 2020-09-15 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200915_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicadociclo',
            name='titulo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='comunicadocurso',
            name='titulo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='comunicadogeneral',
            name='titulo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
