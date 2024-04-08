from rest_framework import serializers
from .models import Recipe, Ingredient

class RecipeGetSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    ingredients = serializers.StringRelatedField(many=True)
    class Meta:
        model = Recipe
        fields = ['id', 'created_by', 'title', 'description', 'cooking_time', 'procedure', 'created_at', 'updated_at', 'ingredients']
        read_only_fields = ['created_at', 'updated_at']

class RecipeCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ['id', 'created_by', 'title', 'description', 'cooking_time', 'procedure', 'created_at', 'updated_at', 'ingredients']
        read_only_fields = ['created_at', 'updated_at']

class RecipeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cooking_time', 'procedure', 'ingredients']

class RecipeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = []

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'quantity']