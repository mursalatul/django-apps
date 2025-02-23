from django.urls import path
from polls import views

urlpatterns=[
    path('<str:app_name>/', views.index, name='index'),
]