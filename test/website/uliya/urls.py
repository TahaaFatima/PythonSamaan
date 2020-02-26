from django.urls import path
from . import views

app_name = "uliya"

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact-us/', views.contact, name="contact")
]