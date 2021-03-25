from django.urls import path

from todo import views

urlpatterns = [
    path('', views.index),
    path('edit/<int:todo_id>', views.edit),
    path('update/<int:todo_id>', views.update),
    path('delete/<int:todo_id>', views.delete),
    path('new/', views.new),
    path('create/', views.create)
]
