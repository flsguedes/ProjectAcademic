# Generated by Django 5.1.6 on 2025-02-15 18:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=14, verbose_name='Disciplina')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'disciplina',
                'db_table': 'disciplina',
            },
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('endereco', models.CharField(max_length=11, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('cnpj', models.CharField(max_length=14, verbose_name='Cnpj')),
            ],
            options={
                'verbose_name': 'instituicao',
                'db_table': 'instituicao',
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, verbose_name='Cpf')),
                ('email', models.CharField(max_length=40, verbose_name='Email')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('data_nacimento', models.DateField(blank=True, default=None, null=True, verbose_name='Data de Nascimento')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Aluno')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instituicao_aluno', to='home.instituicao')),
            ],
            options={
                'verbose_name': 'alunos',
                'db_table': 'alunos',
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_matricula', models.DateField(blank=True, default=None, null=True, verbose_name='Data de Matricula')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aluno_matricula', to='home.aluno')),
            ],
            options={
                'verbose_name': 'matriculas',
                'db_table': 'matriculas',
            },
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.CharField(max_length=50, verbose_name='Avaliação')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Nota')),
                ('data_avaliacao', models.DateField(blank=True, default=None, null=True, verbose_name='Data avaliação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matricula', to='home.matricula')),
            ],
            options={
                'verbose_name': 'notas',
                'db_table': 'notas',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, verbose_name='Cpf')),
                ('especializacao', models.CharField(max_length=40, verbose_name='Especialização')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instituicao_professor', to='home.instituicao')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Professor')),
            ],
            options={
                'verbose_name': 'professores',
                'db_table': 'professores',
            },
        ),
        migrations.CreateModel(
            name='Habilitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplina_habilitacao', to='home.disciplina')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professor_habilitacao', to='home.professor')),
            ],
            options={
                'verbose_name': 'habilitacao',
                'db_table': 'habilitacao',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('data_inicio', models.DateField(blank=True, default=None, null=True, verbose_name='Data de Matricula')),
                ('data_fim', models.DateField(blank=True, default=None, null=True, verbose_name='Data de Matricula')),
                ('carga_horaria', models.IntegerField(blank=True, null=True, verbose_name='Carga horario')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplina_turma', to='home.disciplina')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professores_turma', to='home.professor')),
            ],
            options={
                'verbose_name': 'turmas',
                'db_table': 'turmas',
            },
        ),
        migrations.AddField(
            model_name='matricula',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turma_matricula', to='home.turma'),
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.IntegerField(verbose_name='Semestre')),
                ('horario', models.DateTimeField(verbose_name='Horário')),
                ('carga_horaria', models.IntegerField(blank=True, null=True, verbose_name='Carga horario')),
                ('quantidade_aluno', models.IntegerField(verbose_name='Quantidade de alunos')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplina_historico', to='home.disciplina')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professores_historico', to='home.professor')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turma_historico', to='home.turma')),
            ],
            options={
                'verbose_name': 'historico',
                'db_table': 'historico',
            },
        ),
    ]
