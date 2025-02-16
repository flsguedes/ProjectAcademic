from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from .models import *

User = get_user_model()


def AuthLogin(request):
    if request.method == "GET":
        return render(request, "./home/auth_login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            with transaction.atomic():
                user = User.objects.get(username = username)
        except User.DoesNotExist:
            messages.error(request, "Usuario ou senha incorretos.")
            return render(request, './home/auth_login.html')
        
        if check_password(password, user.password):
            login(request, user)
            return redirect(Index) 
        else:
            messages.error(request, "Usuario ou senha incorretos.")
            return render(request, './home/auth_login.html')
    
@login_required(login_url=AuthLogin)
def Logout(request):
    logout(request)
    return redirect(AuthLogin)

@login_required(login_url=AuthLogin)
def Base(request):
    user = request.user
    return render(request, "./home/base.html", {"user":user})

@login_required(login_url=AuthLogin)
def Index(request):
    return render(request, "./home/index.html")

def ConsultaDisciplina(request):
    if request.method == "GET":
        habilitacao = Habilitacao.objects.all()
    return render(request, "./home/consulta_disciplina.html" , { "habilitacao" : habilitacao})

def ConsultaProfessores(request):
    if request.method == "GET":
        historico = Historico.objects.all()
    return render(request, "./home/consulta_professores.html", { "historico" : historico })

def Professores(request, id=None):
    if request.method == "GET":
        professor = Professor.objects.all()
        
    elif request.method == "POST":
        professor = Professor.objects.get(id=id)
        professor.delete()
        referer = request.META.get('HTTP_REFERER', '/default-url/')
        return redirect(referer)
    return render(request, "./home/professores.html", { "professor" : professor })

def ProfessoresAdd(request):
    if request.method == "GET":
        instituicao = Instituicao.objects.all()
        professor = Professor.objects.all()
        user = User.objects.all()
    elif request.method == "POST":
        instituicao_id = request.POST.get("instituicao")
        user_id = request.POST.get("user")
        especializacao = request.POST.get("especializacao")

        instituicao = Instituicao.objects.get(id=instituicao_id)
        user = User.objects.get(id=user_id)

        Professor.objects.create(
            instituicao=instituicao,
            user=user,
            especializacao=especializacao
        )
        
        return redirect(Professores)

    return render (request, "./home/professores_add.html", { "professor" : professor, "instituicao": instituicao, "user": user})

def ProfessoresAlter(request, id):
    if request.method == "GET":
        professor_id = Professor.objects.get(id=id)
        instituicao = Instituicao.objects.all()
        user = User.objects.all()

    elif request.method == "POST":
        professor_id = Professor.objects.get(id=id)

        instituicao1 = request.POST.get("instituicao")
        user = request.POST.get("user")
        especializacao = request.POST.get("especializacao")

        
        professor_id.especializacao = especializacao

        if instituicao1:
            professor_id.instituicao = Instituicao.objects.get(id=instituicao1)
        if user:
            professor_id.user = User.objects.get(id=user)

        professor_id.save()
        return redirect(Professores)

    return render (request, "./home/professores_alter.html", { "professor" : professor_id, "instituicao": instituicao, "user": user})

    

def Disciplinas(request):
    return render(request, "./home/disciplinas.html")

def Turmas(request):
    return render(request, "./home/turmas.html")

def Alunos(request):
    return render(request, "./home/alunos.html")
