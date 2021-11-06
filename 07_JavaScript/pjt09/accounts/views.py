from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm
from django.http import JsonResponse


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
    auth_logout(request)
    return redirect('community:index')


@login_required
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        # me = request.user 헷갈리면 이렇게 바꿔서 써보면 괜찮을 듯 person은 you로 바꾸고
        person = get_object_or_404(get_user_model(), pk=user_pk)
        
        # 너와 내가 다른 사람이어야 팔로우를 진행할 수 있음
        # 나 자신은 팔로우해서는 안됨
        if request.user != person:
            # 내가 상대방의 팔로워 리스트에 있다면
            # if person.followers.filter(pk=request.user.pk).exists():
            if request.user in person.followers.all():
                followed = False
                # 언팔로우
                person.followers.remove(request.user)
            else:
                followed = True
                # 팔로우
                person.followers.add(request.user)

            context = {
                'followed': followed,
                'followingCnt': person.followings.count(),
                'followerCnt': person.followers.count(),
            }

        return JsonResponse(context)
    return redirect('accounts:login')

