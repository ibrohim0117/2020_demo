from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from .filters import ProductFilter
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductListSerializer, ProductDetailSerializer
from product.models import Product


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    # filterset_fields = ('category', 'name')
    filterset_class = ProductFilter
    permission_classes = (IsAuthenticated, )




class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        product.update_views()
        serializer = ProductDetailSerializer(product)
        data = {
            'message': 'success',
            'data': serializer.data
        }
        return Response(data)
