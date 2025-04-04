from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Todo


class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'deadline']
    template_name = 'todo_form.html'
    success_url = '/'

# Create your views here.
