from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'letters', views.LetterViewSet, basename='letters')

from email_stat.views import stat_24

urlpatterns = [
    path('', include(router.urls)),
    path('stat_24/', stat_24),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



