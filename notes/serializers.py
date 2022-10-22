from rest_framework import serializers
from . import models

class NoteSerializer(serializers.ModelSerializer):

    """
        Serializer for Note Model
        Consists of fields that have to be returned in an API request
    """

    class Meta:

        model = models.Note
        fields = [
            'id', 'title', 'text', 'date', 'starred'
        ]