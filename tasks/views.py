from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm


# Create your views here.
class TaskListView(ListView):  # displays a list of all 'Task' objects
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):  # displays the details of single `Task` object
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskCreateView(CreateView):  # displays a form for creating a new `Task` object
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'


class TaskUpdateView(UpdateView):  # displays a form for updating an existing Task object
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'


class TaskDeleteView(DeleteView):  # displays a confirmation page for deleting an existing Task object
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
