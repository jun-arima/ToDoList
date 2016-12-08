from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required


@login_required
def index(request, task_id=None):
    task_list = Task.objects.all()
    context = {'task_list': task_list, }
    return render(request, 'todos/index.html', context)

@login_required
def delete(request, task_id):
    delete_task = Task.objects.filter(id=task_id)
    delete_task.delete()
    return HttpResponseRedirect('/todos')

@login_required
def update(request, task_id):
    comp_task = Task.objects.get(id=task_id)
    if comp_task.comp_flg == 1:
        comp_task.comp_flg = 0
    else:
        comp_task.comp_flg = 1
    comp_task.save()
    return HttpResponseRedirect('/todos')

@login_required
def create(request):
    name = request.POST['add_name']
    print(name)
    text = request.POST['add_text']
    new_task = Task(task_nm=name, task_text=text, comp_flg=0 )
    new_task.save()
    return HttpResponseRedirect('/todos')
