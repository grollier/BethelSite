from rest_framework import serializers
from prejub.models import Suggestion

class suggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = '__all__'