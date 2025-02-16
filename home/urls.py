from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.views import *

urlpatterns = [ 
    path("auth_login/", AuthLogin, name="auth_login"),
    path("logout/", Logout, name="logout"),
    path("base/", Base, name="base"),
    path("", Index, name="index"),

    path("consulta_disciplina/", ConsultaDisciplina, name="consulta_disciplina"),
    path("consulta_professores/", ConsultaProfessores, name="consulta_professores"),
    
    path("professores/", Professores, name="professores"),
    path("professores/<int:id>", Professores, name="professor_id"),
    path("professores/add/", ProfessoresAdd, name="professor_add"),
    path("professores/<int:id>/alter", ProfessoresAlter, name="professor_alter"),



    path("disciplinas/", Disciplinas, name="disciplinas"),
    path("turmas/", Turmas, name="turmas"),
    path("alunos/", Alunos, name="alunos"),
]