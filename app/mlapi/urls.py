from django.urls import path
from . import views
urlpatterns=[
    path('', views.mlapi_views, name="api_endpoint"),
]