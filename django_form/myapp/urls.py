

from . import views
from django.urls import path, include

urlpatterns = [

    path('', views.contact),
    path('snippet/', views.snippet_detail),
]
