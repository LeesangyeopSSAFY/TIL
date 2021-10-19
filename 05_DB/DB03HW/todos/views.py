from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        todos = Todo.objects.order_by('-pk')

        context = {
            'todos': todos,
        }
        return render(request, 'todos/index.html', context)
    else:
        return redirect('accounts:login')

@login_required
@require_http_methods(['GET', 'POST'])
def new(request):
    if request.method == "POST":
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            todo = todo_form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/new.html', context)