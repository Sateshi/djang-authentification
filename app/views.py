from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from .models import Member

# Create your views here.


def home(request):
    members = Member.objects.all()
    return render(request,'app/home.html',{'members':members})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'app/register.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'app/login.html',{'error_message':error_message})
    else:
        return render(request, 'app/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('home')