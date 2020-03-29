from django.shortcuts import render, redirect
from . models import Todos
from . forms import TodosForm
from django.contrib import messages

def home(request):

    if request.method == 'POST':
        form = TodosForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_todos = Todos.objects.all
            messages.success(request, ('New todo added!'))
            return render(request, 'home.html', { 'all_todos': all_todos })

    else: 
        all_todos = Todos.objects.all
        return render(request, 'home.html', { 'all_todos': all_todos })

def detail(request, todo_id):
    todo = Todos.objects.get(id=todo_id)
    return render(request, 'todos_detail.html', { 
        'todo': todo
        })

def delete(request, todo_id):
    todo = Todos.objects.get(pk=todo_id)
    todo.delete()
    messages.success(request, ('Todo deleted!'))
    return redirect('home')


