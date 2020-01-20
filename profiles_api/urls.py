from django.urls import path, include, re_path

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name= 'hello-viewset')
# Si solo es un conjunto de consultas, no es necesario poner el base_name. 
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    path('hellow-view/', views.HelloApiView.as_view()),
    # Agrega un conjunto de rutas asociadas a su url
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))

]
