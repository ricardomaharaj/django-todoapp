from django.urls import path

from todoapp.views import ListTodo, DeleteTodo, DetailTodo, CreateTodo, UpdateTodo

urlpatterns = [
    path('create/', CreateTodo.as_view(), name='create'),
    path('list/', ListTodo.as_view(), name='list'),
    path('update/<int:pk>', UpdateTodo.as_view(), name='update'),
    path('detail/<int:pk>', DetailTodo.as_view(), name='detail'),
    path('delete/<int:pk>', DeleteTodo.as_view(), name='delete'),
    path('', ListTodo.as_view(), name='home')
]
