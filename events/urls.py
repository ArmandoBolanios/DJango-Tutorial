from django.urls import path
from . import views

urlpatterns = [
    #int: nombers
    #str: strings
    #path: urls/
    path('<int:year>/<str:month>/', views.home, name="home"),
]