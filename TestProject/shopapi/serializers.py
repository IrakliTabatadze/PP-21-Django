from rest_framework import serializers
from shop.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'category_type')

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'stock', 'description', 'category', 'picture')