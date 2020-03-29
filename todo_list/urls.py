# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('todos_detail/<int:todo_id>/', views.detail, name='detail'),
    path('todos/<int:todo_id>/edit', views.todos_update, name='todos_update'),
    path('delete/<int:todo_id>/', views.delete, name="delete"),
]