from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('set-mode/', views.set_mode, name='set_mode'),
    path('adoption/', views.adoption, name='adoption'),
    path('pet/<int:pk>/', views.pet_detail, name='pet_detail'),
    path('awareness/', views.awareness, name='awareness'),
    path('gallery/', views.gallery, name='gallery'),
    path('donation/', views.donation, name='donation'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
