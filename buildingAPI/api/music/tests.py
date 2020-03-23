from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Songs
from .serializers import SongsSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Songs.objects.create(title=title, artist=artist)

    def setUp(self):
        # add test data
        self.create_song("like glue", "sean paul")
        self.create_song("simple song", "konshens")
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam rock", "damien marley")

    def fetch_a_song(self, pk=0):
        return self.client.get(
            reverse(
                "songs-detail",
                kwargs={
                    "version": "v1",
                    "pk": pk
                }
            )
        )