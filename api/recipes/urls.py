from django.urls import path
from .views import (
    RecipeListCreateView,
    RecipeRetrieveUpdateDestroyView,
    IngredientListCreateView,
    IngredientRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeRetrieveUpdateDestroyView.as_view(), name='recipe-detail'),
    path('ingredients/', IngredientListCreateView.as_view(), name='ingredient-list-create'),
    path('ingredients/<int:pk>/', IngredientRetrieveUpdateDestroyView.as_view(), name='ingredient-detail'),
]