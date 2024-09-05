from rest_framework import serializers
from .models import Recipe, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']


class RecipeSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = '__all__'

    def get_tags(self, obj):
        return [tag.title for tag in obj.tags.all()]

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        recipe = Recipe.objects.create(**validated_data)

        tags = []
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(title=tag_name['title'])
            tags.append(tag)

        recipe.tags.set(tags)
        return recipe
