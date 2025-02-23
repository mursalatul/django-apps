from django.urls import path

from main import views as mainviews
from polls import views as pollviews

urlpatterns = [
    path('',mainviews.main,name='main'),
]