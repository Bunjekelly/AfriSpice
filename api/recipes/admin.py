from django.contrib import admin
from .models import Recipe, Ingredient

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    search_fields = ('title', 'created_by__username')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Recipe, RecipeAdmin)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')
    search_fields = ('name',)

admin.site.register(Ingredient, IngredientAdmin)
