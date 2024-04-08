from django.urls import path
from .views import (
    RecipeListAPIView,
    RecipeRetrieveView,
    RecipeUpdateAPIView,
    RecipeDeleteAPIView,
    IngredientListCreateView,
    IngredientRetrieveUpdateDestroyView,
    UserRecipesListView,
    RecipeCreateAPIView,
)

urlpatterns = [
    path('recipes/', RecipeListAPIView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeRetrieveView.as_view(), name='recipe-detail'),
    path('recipes/<int:pk>/update/', RecipeUpdateAPIView.as_view(), name='recipe-update'),
    path('recipes/<int:pk>/delete/', RecipeDeleteAPIView.as_view(), name='recipe-delete'),
    path('ingredients/', IngredientListCreateView.as_view(), name='ingredient-list-create'),
    path('ingredients/<int:pk>/', IngredientRetrieveUpdateDestroyView.as_view(), name='ingredient-detail'),
    path('users/<int:id>/recipes/', UserRecipesListView.as_view(), name='user-recipes'),
    path('recipes/create/', RecipeCreateAPIView.as_view(), name='recipe_create'),
]