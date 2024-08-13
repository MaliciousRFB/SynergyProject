from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import News, Astro, Vehicle,  LifeInSpace, UniverseList
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout

# Page with news

def HomePage(request):
    news = News.objects.all()
    planets = UniverseList.objects.all()
    context = {
        'planets': planets,
        'news': news,
    }
    return render(request, 'Nasa/Basic/home_page.html', context=context)


def ViewNews(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    planets = UniverseList.objects.all()
    context = {
        'planets': planets,
        'news_item': news_item
    }
    return render(request, 'Nasa/Views/view_news.html', context=context)


# Page with astronauts

def ActiveAstro(request):
    astro = Astro.objects.all()
    planets = UniverseList.objects.all()
    context = {
        'planets': planets,
        'astro': astro
    }
    return render(request, 'Nasa/Basic/astro.html', context=context)

def ViewBio(request, astro_id):
    astro_item = get_object_or_404(Astro, pk=astro_id)
    planets = UniverseList.objects.all()
    context = {
        'planets': planets,
        'astro_item': astro_item
    }
    return render(request, 'Nasa/Views/view_bio.html', context=context)


# Page with vehicle

def Spaceships(request):
    vehicle = Vehicle.objects.all()
    planets = UniverseList.objects.all()
    context = {
        'planets': planets,
        'vehicle': vehicle
    }
    return render(request, 'Nasa/Basic/vehicle.html', context=context)

def ViewVehicle(request, vehicle_id):
    vehicle_item = get_object_or_404(Vehicle, pk=vehicle_id)
    planets = UniverseList.objects.all()
    context = {
        'planets': planets,
        'vehicle_item':vehicle_item
    }
    return render(request, 'Nasa/Views/view_vehicle.html', context=context)



# Page with live

def LifeSpace(request):
    life = LifeInSpace.objects.all()
    planets = UniverseList.objects.all()
    context = {
        'planets': planets,
        'life': life,
    }
    return render(request, 'Nasa/Basic/life_space.html', context=context)


def ViewLive(request, article_id):
    live_item = get_object_or_404(LifeInSpace, pk=article_id)
    planets = UniverseList.objects.all()
    context = {
        'planets': planets,
        'live_item': live_item
    }
    return render(request, 'Nasa/Views/view_live.html', context=context)



#Register and Login

def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration succeed!')
            return redirect('Login')
        else:
            messages.error(request, 'Invalid data for registration')
    else:
        form = UserRegisterForm()

    return render(request, 'Nasa/register.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(request, 'Nasa/login.html', {'form': form})


def LogOut(request):
    logout(request)
    return redirect('Login')