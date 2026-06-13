from rest_framework.serializers import ModelSerializer
from apps.users.models import Favourite

class FavouriteListSerializers(ModelSerializer):

    class Meta:
        model = Favourite
        fields = '__all__'

class FavouriteCreateSerializers(ModelSerializer):

    class Meta:
        model = Favourite
        fields = '__all__'

