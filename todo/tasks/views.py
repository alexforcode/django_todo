from django.shortcuts import redirect, render

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    task_form = TaskForm()

    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
        return redirect('/')

    context = {'tasks': tasks, 'task_form': task_form}
    return render(request, 'tasks/index.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    task_form = TaskForm(instance=task)

    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('/')

    context = {'task': task, 'task_form': task_form}
    return render(request, 'tasks/update.html', context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task': task}
    return render(request, 'tasks/delete.html', context)
