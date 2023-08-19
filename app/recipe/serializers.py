"""
Serializer for Recepi API.
"""

from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for Recepi model.
    """
    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'time_minutes',
            'price',
            'link'
        ]
        read_only_fields = ['id']

    # def create(self, validated_data):
    #     """
    #     Create a new Recepi.
    #     """
    #     return Recepi.objects.create(**validated_data)


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""
    class Meta(RecipeSerializer.Meta):
        """Meta class."""
        fields = RecipeSerializer.Meta.fields + ['description']
