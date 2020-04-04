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
