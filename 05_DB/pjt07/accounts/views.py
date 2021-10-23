from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .forms import CustomUserCreationForm

User = get_user_model()

# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('community:index')


@require_safe
def profile(request, username):
    profile = get_object_or_404(get_user_model(), username=username)
    is_following = profile.followers.filter(pk=request.user.pk).exists()
    context={
        'profile': profile,
        'is_following': is_following,
    }
    return render(request, 'accounts/profile.html', context)

@require_POST
def follow(request, username):
    if request.user.is_authenticated:
        follower = request.user
        following = get_object_or_404(User, username=username)
        
        if follower != following:
            if follower.followings.filter(pk=following.pk).exists():
                follower.followings.remove(following)
            else:
                follower.followings.add(following)
        return redirect('accounts:profile', following.username)
    return redirect('accounts:login')