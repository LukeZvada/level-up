from django.urls import path
from .views import usergame_list
from django.conf import settings

urlpatterns = [
    path('reports/usergames', usergame_list),
]