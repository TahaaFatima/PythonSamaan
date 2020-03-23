from django.urls import path
from . import views
from .views import ListSongsView, SongsDetailView

urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('songs/<int:pk>/', SongsDetailView.as_view(), name="songs-detail"),
]