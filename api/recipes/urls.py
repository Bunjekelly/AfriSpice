from django.urls import path
from .views import (
    RecipeListAPIView,
    RecipeRetrieveUpdateDestroyView,
    IngredientListCreateView,
    IngredientRetrieveUpdateDestroyView,
    UserRecipesListView,
    RecipeCreateAPIView,
)

urlpatterns = [
    path('recipes/', RecipeListAPIView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeRetrieveUpdateDestroyView.as_view(), name='recipe-detail'),
    path('ingredients/', IngredientListCreateView.as_view(), name='ingredient-list-create'),
    path('ingredients/<int:pk>/', IngredientRetrieveUpdateDestroyView.as_view(), name='ingredient-detail'),
    path('users/<int:id>/recipes/', UserRecipesListView.as_view(), name='user-recipes'),
    path('recipes/create/', RecipeCreateAPIView.as_view(), name='recipe_create'),
]