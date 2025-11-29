from django.urls import path
from . import views

urlpatterns =[
    path('sliver/', views.show_data)
]