AfriSpice Recipe Sharing API

AfriSpice is an API that allows users to discover, create, and share African meal recipes. It provides various endpoints for managing recipes, ingredients, and user authentication.

Features
User authentication (signup, login, logout)
CRUD operations for recipes and ingredients
Retrieving user profiles
Listing all users
Comprehensive documentation using Swagger UI

Usage
Authentication
User Signup: POST /api/signup/
Create a new user account with a username and password.
User Login: POST /api/login/
Log in with a username and password to obtain an authentication token.
User Logout: POST /api/logout/
Log out by deleting the authentication token.
User Profile: GET /api/profile/
View and update the authenticated user's profile.
Recipes
List/Create Recipes: GET/POST /api/recipes/
List all recipes or create a new recipe.
Retrieve/Update/Delete Recipe: GET/PUT/PATCH/DELETE /api/recipes/<id>/
Retrieve, update, or delete a specific recipe.
Ingredients
List/Create Ingredients: GET/POST /api/ingredients/
List all ingredients or create a new ingredient.
Retrieve/Update/Delete Ingredient: GET/PUT/PATCH/DELETE /api/ingredients/<id>/
Retrieve, update, or delete a specific ingredient.
Data Models
Recipe: Represents a recipe with fields such as title, description, ingredients, etc.
Ingredient: Represents an ingredient with fields such as name, quantity, unit, etc.
CustomUser: Represents a user with custom fields in addition to Django's default user model.

Contributing

Contributions to AfriSpice are welcome! To contribute, follow these steps:
Fork the repository on GitHub.
Create a new branch for your feature or bug fix.
Make your changes and submit a pull request.
Ensure your code passes all tests and follows the project's coding standards.