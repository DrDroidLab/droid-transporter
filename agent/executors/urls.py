from django.urls import path
from . import views

urlpatterns = [
    path('v1/api/grafana', views.v1_api_grafana),
]
