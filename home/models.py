from django.db import models
from django.contrib.auth.models import User

class Notas(models.Model):
    matricula= models.ForeignKey("Matricula", models.CASCADE, related_name="matricula", blank=False, null=False)
    avaliacao= models.CharField(max_length=50, verbose_name="Avaliação")
    nota= models.DecimalField(max_digits=5, verbose_name="Nota",decimal_places=2)
    data_avaliacao= models.DateField(verbose_name="Data avaliação", default=None, blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        db_table="notas"
        verbose_name="notas"

    def __str__(self):
        return self.avaliacao
    

class Matricula(models.Model):
    turma= models.ForeignKey("Turma", models.CASCADE, related_name="turma_matricula", blank=False, null=False)
    aluno= models.ForeignKey("Aluno", models.CASCADE, related_name="aluno_matricula", blank=False, null=False)
    data_matricula= models.DateField(verbose_name="Data de Matricula", default=None, blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        db_table="matriculas"
        verbose_name="matriculas"


class Turma(models.Model):
    nome= models.CharField(max_length=50)
    professor= models.ForeignKey("Professor", models.CASCADE, related_name="professores_turma", blank=False, null=False)
    disciplina= models.ForeignKey("Disciplina", models.CASCADE, related_name="disciplina_turma", blank=False, null=False)
    data_inicio= models.DateField(verbose_name="Data de Matricula", default=None, blank=True, null=True)
    data_fim= models.DateField(verbose_name="Data de Matricula", default=None, blank=True, null=True)
    carga_horaria= models.IntegerField(verbose_name="Carga horario", blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        db_table="turmas"
        verbose_name="turmas"

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    instituicao= models.ForeignKey("Instituicao", models.CASCADE, related_name="instituicao_aluno", blank=False, null=False)
    user= models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name="Aluno")
    cpf= models.CharField(max_length=11, verbose_name="Cpf")
    email= models.CharField(max_length=40, verbose_name="Email")
    telefone= models.CharField(max_length=15, verbose_name="Telefone")
    data_nacimento= models.DateField(verbose_name="Data de Nascimento", default=None, blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        db_table="alunos"
        verbose_name="alunos"

    def __str__(self):
        return self.user
    

class Instituicao(models.Model):
    nome= models.CharField(max_length=40, verbose_name="Nome")
    endereco= models.CharField(max_length=11, verbose_name="Endereço")
    telefone= models.CharField(max_length=15, verbose_name="Telefone")
    cnpj= models.CharField(max_length=14, verbose_name="Cnpj")

    class Meta:
        db_table="instituicao"
        verbose_name="instituicao"

    def __str__(self):
        return self.nome


class Professor(models.Model):
    instituicao= models.ForeignKey(Instituicao, models.CASCADE, related_name="instituicao_professor", blank=False, null=False)
    user= models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name="Professor")
    cpf= models.CharField(max_length=11, verbose_name="Cpf")
    especializacao= models.CharField(max_length=40, verbose_name="Especialização")
    
    class Meta:
        db_table="professores"
        verbose_name="professores"

    def __str__(self):
        return self.user


class Habilitacao(models.Model):
    professor= models.ForeignKey(Professor, models.CASCADE, related_name="professor_habilitacao", blank=False, null=False)
    disciplina= models.ForeignKey("Disciplina", models.CASCADE, related_name="disciplina_habilitacao", blank=False, null=False)
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        db_table="habilitacao"
        verbose_name="habilitacao"

    def __str__(self):
        return self.professor
    

class Disciplina(models.Model):
    nome= models.CharField(max_length=14, verbose_name="Disciplina")
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        db_table="disciplina"
        verbose_name="disciplina"

    def __str__(self):
        return self.nome
    

class Historico(models.Model):
    professor= models.ForeignKey(Professor, models.CASCADE, related_name="professores_historico", blank=False, null=False)
    disciplina= models.ForeignKey(Disciplina, models.CASCADE, related_name="disciplina_historico", blank=False, null=False)
    turma= models.ForeignKey(Turma, models.CASCADE, related_name="turma_historico", blank=False, null=False)
    semestre= models.IntegerField(verbose_name="Semestre")
    horario= models.DateTimeField(verbose_name="Horário")
    carga_horaria= models.IntegerField(verbose_name="Carga horario", blank=True, null=True)
    quantidade_aluno= models.IntegerField(verbose_name="Quantidade de alunos")
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        db_table="historico"
        verbose_name="historico"

    def __str__(self):
        return self.semestre
# Create your models here.
