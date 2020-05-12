# Generated by Django 3.0.5 on 2020-05-05 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_curso_nivel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alunos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.Aluno')),
                ('cursos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.Curso')),
            ],
        ),
    ]