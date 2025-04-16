from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from product.models import Product


class ProductListSerializer(ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['category_name', 'name', 'rating', 'sale', 'price', 'sale_price', 'views', 'image_list']

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None


class ProductDetailSerializer(ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['category_name', 'name', 'rating', 'sale', 'price',
                  'sale_price', 'views', 'code', 'type', 'information', 'is_available',  'image_list']

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

