from rest_framework import generics, mixins
from musicapp.models import Song, Artiste, Lyrics
from .serializers import SongSerializer, ArtisteSerializer, LyricsSerializer


class SongListCreateAPIView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


song_list_create = SongListCreateAPIView.as_view()

class SongDetailAPIView(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


song_detail_create = SongDetailAPIView.as_view()


class SongUpdateAPIView(generics.UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'pk'


song_update_create = SongUpdateAPIView.as_view()

class SongDeleteAPIView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


song_destroy_view = SongDeleteAPIView.as_view()

