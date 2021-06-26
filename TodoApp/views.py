from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from TodoApp.models import Todo


class TodoDetail(DetailView):
    model = Todo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TodoList(ListView):
    model = Todo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TodoCreate(CreateView):
    model = Todo
    fields = ['title', 'completed']
    success_url = '/todos/list/'


class TodoUpdate(UpdateView):
    model = Todo
    fields = ['title', 'completed']
    success_url = '/todos/list/'


class TodoDelete(DeleteView):
    model = Todo
    success_url = '/todos/list/'
