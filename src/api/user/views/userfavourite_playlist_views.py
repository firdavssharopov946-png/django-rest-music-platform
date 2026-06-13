from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from api.user.serializers import userfavourite_playlist_serializers
from rest_framework import status
from rest_framework.response import Response
from apps.users.models import FavouritePlaylist

class FavouritePlaylistListApiView(ListAPIView):
    queryset = FavouritePlaylist.objects.all()
    serializer_class = userfavourite_playlist_serializers.FavouritePlaylistListSerializers
    permission_classes = [IsAuthenticated]


class FavouritePlaylistCreateAPIView(CreateAPIView):
    queryset = FavouritePlaylist.objects.all()
    serializer_class = userfavourite_playlist_serializers.FavouritePlaylistCreateSerializers
    permission_classes = [IsAuthenticated]


class FavouritePlaylistUpdateAPIView(UpdateAPIView):
    queryset = FavouritePlaylist.objects.all()
    serializer_class = userfavourite_playlist_serializers.FavouritePlaylistCreateSerializers
    permission_classes = [IsAuthenticated]


class FavouritePlaylistRetrieveAPIView(RetrieveAPIView):
    queryset = FavouritePlaylist.objects.all()
    serializer_class = userfavourite_playlist_serializers.FavouritePlaylistListSerializers
    permission_classes = [IsAuthenticated]


class FavouritePlaylistDestroyAPIView(DestroyAPIView):
    queryset = FavouritePlaylist.objects.all()
    permission_classes = [IsAuthenticated]