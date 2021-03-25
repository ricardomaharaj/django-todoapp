from django.shortcuts import render, redirect

from todo.models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})


def edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'edit.html', {'todo': todo})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.title = request.POST['title']
    todo.completed = False
    if 'completed' in request.POST:
        todo.completed = True
    todo.save()
    return redirect('/')


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('/')


def new(request):
    return render(request, 'new.html')


def create(request):
    todo = Todo()
    todo.title = request.POST['title']
    todo.completed = False
    if 'completed' in request.POST:
        todo.completed = True
    todo.save()
    return redirect('/')
