from django.views.generic import UpdateView, DetailView, ListView, CreateView, DeleteView

from todoapp.models import Todo


class ListTodo(ListView):
    queryset = Todo.objects.order_by('-updated')
    template_name = 'list.html'


class DetailTodo(DetailView):
    model = Todo
    template_name = 'detail.html'


class UpdateTodo(UpdateView):
    model = Todo
    template_name = 'update.html'
    success_url = '/list/'
    fields = ['title', 'body', 'completed']


class CreateTodo(CreateView):
    model = Todo
    template_name = 'create.html'
    success_url = '/list/'
    fields = ['title', 'body', 'completed']


class DeleteTodo(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = '/list/'
