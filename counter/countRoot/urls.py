from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy_session),
    path('add_2', views.add_2),
    path('selection', views.selection)
]