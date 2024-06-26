from rest_framework.serializers import ModelSerializer, ReadOnlyField

from musician.models import Musician


class MusicianSerializer(ModelSerializer):

    class Meta:
        model = Musician
        fields = [
            "first_name", "last_name",
            "instrument", "age", "date_of_applying",
            "is_adult"
        ]
