from .views import get_all_recipe, add_recipe
from django.urls import path

urlpatterns = [
    path('', get_all_recipe),
    path('create/', add_recipe)
]
