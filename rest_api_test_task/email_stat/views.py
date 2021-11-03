from rest_framework import viewsets
from rest_framework.decorators import api_view

import datetime


from .serializers import LetterSerializer
from .models import Letter

from rest_framework.response import Response
from django.db.models import Count


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all().order_by('date')
    serializer_class = LetterSerializer


@api_view()
def stat_24(request):
    total = len(Letter.objects.all())

    t1 = datetime.datetime.now()
    t2 = t1 - datetime.timedelta(days=1)

    top_10 = Letter.objects.values('email'
        ).annotate(Count('email')
        ).filter(date__range=[t2, t1]
        ).order_by("email__count")[::-1]

    return Response({
        "total": total,
        "top_10": top_10,
        })
