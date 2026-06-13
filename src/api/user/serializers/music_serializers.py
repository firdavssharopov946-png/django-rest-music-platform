from rest_framework.serializers import ModelSerializer
from apps.music.models import Music

class MusicListSerializers(ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'

class MusicCreateSerializers(ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'

