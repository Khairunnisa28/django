from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='home'),
    path('user/<int:pk>', views.user_detail, name='user_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
]
