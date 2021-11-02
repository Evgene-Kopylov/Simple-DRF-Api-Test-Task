from rest_framework import viewsets

from .serializers import LetterSerializer
from .models import Letter

class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all().order_by('date')
    serializer_class = LetterSerializer

