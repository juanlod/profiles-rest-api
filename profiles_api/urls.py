from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name= 'hello-viewset')
# Si solo es un conjunto de consultas, no es necesario poner el base_name. 
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hellow-view/', views.HelloApiView.as_view()),
    # Agrega un conjunto de rutas asociadas a su url
    path('', include(router.urls))

]
