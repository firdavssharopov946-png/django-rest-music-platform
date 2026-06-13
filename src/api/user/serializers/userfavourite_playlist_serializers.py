from rest_framework.serializers import ModelSerializer
from apps.users.models import FavouritePlaylist

class FavouritePlaylistListSerializers(ModelSerializer):

    class Meta:
        model = FavouritePlaylist
        fields = '__all__'

class FavouritePlaylistCreateSerializers(ModelSerializer):

    class Meta:
        model = FavouritePlaylist
        fields = '__all__'

