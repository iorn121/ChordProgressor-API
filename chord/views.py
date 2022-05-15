from .models import Tone
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import Serializer

class api(ListCreateAPIView):
    queryset=Tone.objects.all()
    serializer_class=Serializer

    permission_classes=[IsAuthenticated]
    