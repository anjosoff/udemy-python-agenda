
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def login (request):
    if request.method!='POST':
        return render(request,'accounts/login.html')
    usuario=request.POST.get('usuario')
    senha=request.POST.get('senha')
    user=auth.authenticate(request,username=usuario,password=senha)
    if not user:
        messages.error(request,'Usuario e/ou senha inválidos')
        return render(request,'accounts/login.html')
    else:
        messages.success(request,'Logado com sucesso')
        auth.login(request,user)
        return redirect('dashboard')
def logout (request):
    auth.logout(request)
    return redirect('dashboard')
def register (request):
    if request.method !='POST':
        return render(request,'accounts/register.html')
    nome=request.POST.get('nome')    
    sobrenome=request.POST.get('sobrenome')    
    email=request.POST.get('email')    
    usuario=request.POST.get('usuario')    
    senha=request.POST.get('senha')    
    senha2=request.POST.get('senha2')    
    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request,'Nenhum campo pode ficar vazio')
        return render(request,'accounts/register.html')
    try:
        validate_email(email)
    except:
        messages.error(request,'Email invalido')
        return render(request,'accounts/register.html')
    if len(senha)<6:
        messages.error(request,'A senha precisa conter mais de 6 caracteres')
        return render(request,'accounts/register.html')
    if len(usuario)<6:
        messages.error(request,'O usuario precisa conter mais de 6 caracteres')
        return render(request,'accounts/register.html')
    if senha!= senha2:
        messages.error(request,'A senhas não conferem')
        return render(request,'accounts/register.html')
    if User.objects.filter(username=usuario).exists():
        messages.error(request,'Usuario já existe')
        return render(request,'accounts/register.html')
    if User.objects.filter(email=email).exists():
        messages.error(request,'Email já cadastrado')
        return render(request,'accounts/register.html')
    messages.success(request,'Registrado com sucesso! Faça login.')
    user=User.objects.create_user(
        username=usuario,
        email=email,
        password=senha,
        first_name=nome,
        last_name=sobrenome,
    )
    user.save()
    return redirect('login')
@login_required(redirect_field_name='login')
def dashboard (request):

    return render(request,'accounts/dashboard.html')
