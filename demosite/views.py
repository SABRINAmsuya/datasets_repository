from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'demosite/home.html', {})

def public_datasets(request):
    return render(request, 'demosite/public_datasets.html', {})

@login_required
def private_datasets(request):
    return render(request, 'demosite/private_datasets.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = UserCreationForm()
    return render(request, 'demosite/signup.html', {'form': form})