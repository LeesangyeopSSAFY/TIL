from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_http_methods
# Create your views here.
@require_http_methods(['GET','POST'])
def signup(request):
    # Q1-1
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    context={
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET','POST'])
def login(request):
    # Q2-1
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def index(request):
    return render(request, 'accounts/index.html')
