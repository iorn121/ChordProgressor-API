from .models import Tone
from rest_framework import viewsets,filters
from .serializers import Serializer

class ChordViewSet(viewsets.ModelViewSet):
    queryset=Tone.objects.all()
    serializer_class=Serializer
    # filter_backends=(filters.SearchFilter,)
    # search_fields=('id', 'name')