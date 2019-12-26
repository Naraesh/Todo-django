from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('add/',views.todoforms,name="adtodo"),
    path('update/<int:id>',views.update,name="update"),
    path('destroy/',views.destroy,name="destroy")
]