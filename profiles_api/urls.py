from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-set', views.ViewHelloSet, basename='hello-set')

urlpatterns =[
    path('hello/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
