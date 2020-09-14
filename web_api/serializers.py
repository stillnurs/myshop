from rest_framework import serializers
from store.products.models import Category

from store.products.models import Product


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['cate',
                  'name',
                  'slug',
                  'image',
                  'description',
                  'price',
                  'create',
                  ]
