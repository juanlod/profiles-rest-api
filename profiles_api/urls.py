from django.urls import path, include
from profiles_api import views

urlpatterns = [
    path('hellow-view/', views.HelloApiView.as_view()),

]
