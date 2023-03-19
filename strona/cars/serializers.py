from cars.models import Car
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):

    engine_name = serializers.CharField(source='get_engine_display', read_only=True)

    class Meta:
        model = Car
        fields = (
            'id', 'name', 'engine_name', 'power', 'engine'
        )
