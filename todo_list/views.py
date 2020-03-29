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

