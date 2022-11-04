from django.urls import path
from . import views

urlpatterns = [
    path('', views.hng9Stage1),
    path('stage2/', views.mathFunc),
]
