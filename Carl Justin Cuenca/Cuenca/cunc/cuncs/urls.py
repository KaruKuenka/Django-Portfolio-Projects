from django.urls import path
from . import views

urlpatterns =[
    path('sliver/', views.show_data),
    path('', views.portfolio_view, name='portfolio'),
]