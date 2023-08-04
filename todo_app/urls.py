from django.urls import path
from .views import list_todo

urlpatterns=[
    path("list-todo",list_todo,name="my_todo_list")
]