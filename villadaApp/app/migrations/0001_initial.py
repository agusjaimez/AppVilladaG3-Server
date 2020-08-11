# Generated by Django 3.1 on 2020-08-11 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(choices=[('1A', 'Primero A'), ('1B', 'Primero B'), ('1C', 'Primero C'), ('2A', 'Segundo A'), ('2B', 'Segundo B'), ('2C', 'Segundo C'), ('3A', 'Tercero A'), ('3B', 'Tercero B'), ('3C', 'Tercero C'), ('4A', 'Cuarto A'), ('4B', 'Cuarto B'), ('4C', 'Cuarto C'), ('5A', 'Quinto A'), ('5B', 'Quinto B'), ('5C', 'Quinto C'), ('6A', 'Sexto A'), ('6B', 'Sexto B'), ('6C', 'Sexto C'), ('7A', 'Septimo A'), ('7B', 'Septimo B'), ('7C', 'Septimo C')], default='1A', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Directivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PadreTutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('delegado', models.BooleanField(default=False)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudReunion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('motivo', models.TextField()),
                ('padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.padretutor')),
            ],
        ),
        migrations.CreateModel(
            name='Preceptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=30)),
                ('curso', models.ManyToManyField(to='app.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('tipo_form', models.CharField(choices=[('F1', 'Formulario 1'), ('F2', 'Formulario 2'), ('F3', 'Formulario 3')], default='F1', max_length=2)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='ComunicadoGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('mensaje', models.TextField()),
                ('directivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.directivo')),
            ],
        ),
        migrations.CreateModel(
            name='ComunicadoCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('mensaje', models.TextField()),
                ('cursos', models.ManyToManyField(to='app.Curso')),
                ('directivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.directivo')),
            ],
        ),
        migrations.CreateModel(
            name='ComunicadoCiclo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('mensaje', models.TextField()),
                ('ciclo', models.CharField(choices=[('B', 'Basico'), ('A', 'Avanzado')], default='B', max_length=20)),
                ('directivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.directivo')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso'),
        ),
    ]
