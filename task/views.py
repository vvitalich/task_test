from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'object_list'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'

