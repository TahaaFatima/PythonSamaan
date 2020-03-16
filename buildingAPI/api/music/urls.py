from django.urls import path
from . import views
from .views import ListSongsView

app_name = "music"

urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
]