from django.urls import path, include

urlpatterns = [
    path('todos/', include('TodoApp.urls'))
]
