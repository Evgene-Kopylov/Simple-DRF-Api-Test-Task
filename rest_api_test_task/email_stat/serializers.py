from rest_framework import serializers

from .models import Letter

class LetterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Letter
        fields = ('id', 'email', 'theme', 'date')

