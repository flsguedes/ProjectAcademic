from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.register(Notas)
admin.site.register(Matricula)
admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(Instituicao)
admin.site.register(Professor)
admin.site.register(Habilitacao)
admin.site.register(Disciplina)
admin.site.register(Historico)


# Register your models here.
