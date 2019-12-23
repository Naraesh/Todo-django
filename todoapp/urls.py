from django.urls import path
from .import views 

urlpatterns = [
   path('',views.index,name="hello"),
   path('save/',views.mod,name="save"),
   path('delete/<int:id>', views.destroy),
   path('edit/<int:id>', views.edit),
   path('update/<int:id>', views.update),
]