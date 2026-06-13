from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from api.user.serializers import userfavourite_serializers
from rest_framework import status
from rest_framework.response import Response
from apps.users.models import Favourite

class FavouriteListApiView(ListAPIView):
    queryset = Favourite.objects.all()
    serializer_class = userfavourite_serializers.FavouriteListSerializers
    permission_classes = [IsAuthenticated]


class FavouriteCreateAPIView(CreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = userfavourite_serializers.FavouriteCreateSerializers
    permission_classes = [IsAuthenticated]


class FavouriteUpdateAPIView(UpdateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = userfavourite_serializers.FavouriteCreateSerializers
    permission_classes = [IsAuthenticated]


class FavouriteRetrieveAPIView(RetrieveAPIView):
    queryset = Favourite.objects.all()
    serializer_class = userfavourite_serializers.FavouriteListSerializers
    permission_classes = [IsAuthenticated]


class FavouriteDestroyAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)