from django.urls import path

from main import views as mainviews

urlpatterns = [
    path('',mainviews.main,name='main'),
]