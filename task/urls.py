from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('',views.task_list,name='home'), # show all task 
    path('add/',views.add_task , name='add_task'), # add new task 
    path('update/<int:pk>/',views.update_task, name='update_task'), # Edit task 
    path('delete/<int:pk>/',views.delete_task,name='delete_task'), # delte task 
]
