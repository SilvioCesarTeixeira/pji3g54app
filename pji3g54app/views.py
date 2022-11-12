from django.shortcuts import render, redirect
from pji3g54app.forms import CadastroForm
from pji3g54app.models import Cadastro
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from pji3g54app.geocode import get_address, get_location

def home(request):
    return render(request, 'home.html')

def index(request):
    data = {}
    search = request.GET.get('search')
    tipo = request.GET.get('inputTipo')

    if search:
        if tipo == "None":
            data['db'] = Cadastro.objects.filter(inputCity__icontains=search)
        else:
            data['db'] = Cadastro.objects.filter(inputCity__icontains=search, inputTipo=tipo)
    else:
        qry_data = Cadastro.objects.get_queryset().order_by('id') # Garante que o DB fornece um registro de cada vez, ordenado por Id
        paginator = Paginator(qry_data, 4)  # Exibe 4 registros do DB por página
        pages = request.GET.get('page')  # Captura qual é a página (page) selecionada no index.html pelo usuário
        data['db'] = paginator.get_page(pages)
    #   data['db'] = Cadastro.objects.all() ## Para buscar todos os registros do DB ## Linha para request sem paginação
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = CadastroForm()
    return render(request, 'form.html', data)


def formpf(request):
    data = {}
    data['formpf'] = CadastroForm()
    return render(request, 'formPF.html', data)


def create(request):
    form = CadastroForm(request.POST or None)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('index')


def view(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    form = data['db']
    if (str(form)) == 'True':
        data['formpf'] = CadastroForm(instance=data['db'])
        return render(request, 'formPF.html', data)
    else:
        data['form'] = CadastroForm(instance=data['db'])
        return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    form = CadastroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('index')


def delete(request, pk):
    db = Cadastro.objects.get(pk=pk)
    db.delete()
    return redirect('index')


def create_user(request):
    return render(request, 'create_user.html')


def store_user(request):
    data = {}
    if (request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'store_user.html', data)


def vmoleo (request, inputCEP):
    data = {}
    # print(inputCEP)
    vmoleo = '7.38'
    data['vmoleo'] = vmoleo
    endereco = get_address(inputCEP)
    # pontos = get_location(data['endereco'])
    if endereco:
        data['endereco'] = endereco
    else:
        data['endereco'] = 'endereço não encontrado'
    return render(request, 'vmoleo.html', data)


def painel(request):
    return render(request, 'painel.html')


def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha inválidos!'
        data['class'] = 'alert-danger'
    return render(request, 'painel.html', data)


def dashboard(request):
    return render(request, 'index.html')


def dologout(request):
    logout(request)
    return redirect('/painel/')


def troca_senha(request):
    # precisa criar formulario de troca senha na área restrita
    user = User.objects.get(email=request.POST.user)
    user.set_password(request.POST['troca_senha'])
    user.save()
    logout(request)
    return redirect('/painel/')