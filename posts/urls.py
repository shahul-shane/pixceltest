from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('members/aboutus', views.aboutus, name='aboutus'),
    path('members/footer', views.footer, name='footer'),
    path('members/privacy', views.privacy, name='privacy'),
    path('members/portfolio', views.portfolio, name='portfolio'),
    path('members/contacts', views.contacts, name='contacts'),
    
]