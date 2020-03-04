from django.urls import path
from . import views

app_name = 'dataFromCSV'

urlpatterns =   [
                    path('', views.index, name='index'),
                    path('show-data', views.show_data, name='show_data'),
                ]