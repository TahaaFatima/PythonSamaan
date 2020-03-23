from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer
from rest_framework.response import Response
from rest_framework.views import status


class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

class SongsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET songs/:id/
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_song = self.queryset.get(pk=kwargs["pk"])
            return Response(SongsSerializer(a_song).data)
        except Songs.DoesNotExist:
            return Response(
                data={
                    "message": "Song with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )