from rest_framework import generics
from rest_framework import status
from .models import Recipe, Ingredient
from .serializers import RecipeSerializer, IngredientSerializer

class RecipeListCreateView(generics.ListCreateAPIView):
    """
    View to list all recipes or create a new recipe.

    - To list all recipes, send a GET request to this endpoint.
    - To create a new recipe, send a POST request to this endpoint
      with the required data.

    Required Permissions:
    - None

    Response:
    - Returns a list of all recipes in the database or creates a new recipe
      and returns the newly created recipe data.

    Serializer:
    - RecipeSerializer: Serializes Recipe model data.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a recipe.

    - To retrieve a specific recipe, send a GET request to this endpoint
      with the recipe's ID.
    - To update a recipe, send a PUT or PATCH request to this endpoint
      with the recipe's ID and the updated data.
    - To delete a recipe, send a DELETE request to this endpoint with
      the recipe's ID.

    Required Permissions:
    - None

    Response:
    - Returns the data of the specified recipe.

    Serializer:
    - RecipeSerializer: Serializes Recipe model data.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class IngredientListCreateView(generics.ListCreateAPIView):
    """
    View to list all ingredients or create a new ingredient.

    - To list all ingredients, send a GET request to this endpoint.
    - To create a new ingredient, send a POST request to this endpoint
      with the required data.

    Required Permissions:
    - None

    Response:
    - Returns a list of all ingredients in the database or creates a new
      ingredient and returns the newly created ingredient data.

    Serializer:
    - IngredientSerializer: Serializes Ingredient model data.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete an ingredient.

    - To retrieve a specific ingredient, send a GET request to this
      endpoint with the ingredient's ID.
    - To update an ingredient, send a PUT or PATCH request to this endpoint
      with the ingredient's ID and the updated data.
    - To delete an ingredient, send a DELETE request to this endpoint with
      the ingredient's ID.

    Required Permissions:
    - None

    Response:
    - Returns the data of the specified ingredient.

    Serializer:
    - IngredientSerializer: Serializes Ingredient model data.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class UserRecipesListView(generics.ListAPIView):
    """
    View to retrieve all recipes created by a specific user.

    **GET** method:
    - Requires:
      - `id`: The ID of the user whose recipes to retrieve.
    - Returns:
      - A list of all recipes created by the specified user.
    """

    serializer_class = RecipeSerializer

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Recipe.objects.filter(created_by_id=user_id)