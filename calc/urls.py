from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"), #the name can also be index.html
    path('add', views.add, name="add") #views.add -> add is the function name

]