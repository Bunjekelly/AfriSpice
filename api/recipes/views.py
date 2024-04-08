from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Recipe, Ingredient
from .serializers import (
  RecipeGetSerializer,
  RecipeCreateSerializer,
  RecipeUpdateSerializer,
  RecipeDeleteSerializer,
  IngredientSerializer,
)
class RecipeCreateAPIView(generics.CreateAPIView):
    """
    Endpoint to create a new recipe.

    Required Permissions:
        - User must be authenticated.

    HTTP Methods:
        - POST: Create a new recipe.

    Request Body:
        - title (string): Title of the recipe.
        - description (string): Description of the recipe.
        - cooking_time (string): Cooking time required for the recipe.
        - procedure (string): Procedure or steps to prepare the recipe.
        - ingredients (list of integers): IDs of ingredients required for the recipe.

    Response:
        - 201 Created: Returns the details of the created recipe.
    """
    permission_classes = [IsAuthenticated]

    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateSerializer
    
class RecipeListAPIView(generics.ListAPIView):
    """
    Endpoint to list all recipes.

    HTTP Methods:
        - GET: Retrieve a list of all recipes.

    Response:
        - 200 OK: Returns a list of all recipes.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeGetSerializer

class RecipeRetrieveView(generics.RetrieveAPIView):
    """
    View to retrieve a recipe.

    - To retrieve a specific recipe, send a GET request to this endpoint
      with the recipe's ID.
    Required Permissions:
    - None

    Response:
    - Returns the data of the specified recipe.

    Serializer:
    - RecipeGetSerializer: Serializes Recipe model data for retrieval.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeGetSerializer

class RecipeUpdateAPIView(generics.UpdateAPIView):
    """
    Endpoint to update an existing recipe.

    Required Permissions:
        - User must be authenticated.

    HTTP Methods:
        - PUT: Update an existing recipe.

    Request Body:
        - title (string): Title of the recipe.
        - description (string): Description of the recipe.
        - cooking_time (string): Cooking time required for the recipe.
        - procedure (string): Procedure or steps to prepare the recipe.
        - ingredients (list of integers): IDs of ingredients required for the recipe.

    Response:
        - 200 OK: Returns the updated recipe details.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeUpdateSerializer
    permission_classes = [IsAuthenticated]

class RecipeDeleteAPIView(generics.DestroyAPIView):
    """
    Endpoint to delete an existing recipe.

    Required Permissions:
        - User must be authenticated.

    HTTP Methods:
        - DELETE: Delete an existing recipe.

    Request Body:
        - None

    Response:
        - 204 No Content: Recipe deleted successfully.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeDeleteSerializer
    permission_classes = [IsAuthenticated]

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

    serializer_class = RecipeCreateSerializer

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Recipe.objects.filter(created_by_id=user_id)