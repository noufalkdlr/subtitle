from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('list/',views.list,name='list'),
    path('edit/',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete')
]