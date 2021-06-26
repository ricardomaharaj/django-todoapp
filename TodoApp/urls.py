from django.urls import path

from TodoApp.views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete

urlpatterns = [
    path('detail/<int:pk>', TodoDetail.as_view(template_name='TodoDetail.html'), name='TodoDetail'),
    path('list/', TodoList.as_view(template_name='TodoList.html'), name='TodoList'),
    path('create/', TodoCreate.as_view(template_name='TodoCreate.html'), name='TodoCreate'),
    path('update/<int:pk>', TodoUpdate.as_view(template_name='TodoUpdate.html'), name='TodoUpdate'),
    path('delete/<int:pk>', TodoDelete.as_view(template_name='TodoDelete.html'), name='TodoDelete')
]
