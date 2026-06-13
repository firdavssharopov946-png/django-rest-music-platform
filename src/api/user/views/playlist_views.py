from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from api.user.serializers import playlist_serializers
from rest_framework import status
from rest_framework.response import Response
from apps.music.models import Playlist

class PlaylistListApiView(ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_serializers.PlaylistListSerializers
    permission_classes = [IsAuthenticated]


class PlaylistCreateAPIView(CreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_serializers.PlaylistCreateSerializers
    permission_classes = [IsAuthenticated]


class PlaylistUpdateAPIView(UpdateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_serializers.PlaylistCreateSerializers
    permission_classes = [IsAuthenticated]


class PlaylistRetrieveAPIView(RetrieveAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_serializers.PlaylistListSerializers
    permission_classes = [IsAuthenticated]


class PlaylistDestroyAPIView(DestroyAPIView):
    queryset = Playlist.objects.all()
    permission_classes = [IsAuthenticated]