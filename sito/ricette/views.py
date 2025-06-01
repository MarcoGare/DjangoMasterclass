from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Ricetta, Preferito, Concorrente, Chef
from django.contrib.auth.models import User

def home(request):
    concorrenti = Concorrente.objects.all()
    chef = Chef.objects.all()
    return render(request, 'ricette/home.html', {
        'concorrenti': concorrenti,
        'chef': chef
    })

def ricette_concorrente(request, concorrente_id):
    try:
        concorrente = Concorrente.objects.get(id=concorrente_id)
        ricette = Ricetta.objects.filter(concorrente=concorrente)
        return render(request, 'ricette/ricette_concorrente.html', {'concorrente': concorrente, 'ricette': ricette})
    except:
        return HttpResponse("Concorrente non trovato.")

def ricette_chef(request, chef_id):
    try:
        chef = Chef.objects.get(id=chef_id)
        ricette = chef.ricette_giudicate.all()
        return render(request, 'ricette/ricette_chef.html', {'chef': chef, 'ricette': ricette})
    except:
        return HttpResponse("Chef non trovato.")


def dettaglio_ricetta(request, ricetta_id):
    ricetta = Ricetta.objects.get(id=ricetta_id)
    is_preferito = False
    if request.user.is_authenticated:
        is_preferito = Preferito.objects.filter(user=request.user, ricetta=ricetta).exists()
    return render(request, 'ricette/dettaglio.html', {
        'ricetta': ricetta,
        'is_preferito': is_preferito,
    })



def login_register(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password, email=email)
                login(request, user)
                return redirect('home')
        elif 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    return render(request, 'ricette/login_register.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def preferiti(request):
    if not request.user.is_authenticated:
        return redirect('login_register')
    lista = Preferito.objects.filter(user=request.user)
    return render(request, 'ricette/preferiti.html', {'preferiti': lista})

def aggiungi_preferito(request, ricetta_id):
    if request.user.is_authenticated:
        ricetta = Ricetta.objects.get(id=ricetta_id)
        Preferito.objects.get_or_create(user=request.user, ricetta=ricetta)
        return redirect('preferiti')
    return redirect('login_register')

def elimina_preferito(request, ricetta_id):
    if request.user.is_authenticated:
        preferito = Preferito.objects.filter(user=request.user, ricetta_id=ricetta_id).first()
        if preferito:
            preferito.delete()
        return redirect('preferiti')
    else:
        return redirect('login_register')

