from rest_framework import serializers
from .models import Artist, Music

class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('id', 'title',)

class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'
        read_only_fields = ('artist',)

class ArtistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name',)

class ArtistSerializer(serializers.ModelSerializer):
    musics = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    musics_count = serializers.IntegerField(source='musics.count', read_only=True)

    class Meta:
        model = Artist
        fields = '__all__'
