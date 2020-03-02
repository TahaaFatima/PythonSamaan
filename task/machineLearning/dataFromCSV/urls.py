from django.urls import path
from . import views

app_name = 'dataFromCSV'

urlpatterns =   [
                    path('', views.index, name='index'),
                    # path('simple-upload', views.simple_upload, name='file-upload'),
                ]