from rest_framework import serializers
from .models import Part, Plane, Team

# Parça (Part) modeli için serializer
class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'

# Uçak (Plane) modeli için serializer
class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = '__all__'

# Takım (Team) modeli için serializer
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
