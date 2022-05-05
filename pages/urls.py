from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('pages',views.pages,name='pages'),
]