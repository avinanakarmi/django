from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Recipe, Tag
from .serializer import RecipeSerializer


@api_view(['GET'])
def get_all_recipe(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True).data
    return Response(serializer)


@api_view(['POST'])
def add_recipe(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # The create method in the serializer handles the tags
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
