from rest_framework import viewsets
from rest_framework.decorators import api_view

from .serializers import LetterSerializer
from .models import Letter

from rest_framework.response import Response


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all().order_by('date')
    serializer_class = LetterSerializer


@api_view()
def stat_24(request):
    total = len(Letter.objects.all())
    return Response({
        "total": total,
        })




