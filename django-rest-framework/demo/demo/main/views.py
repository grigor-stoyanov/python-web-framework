from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.mixins import DestroyModelMixin
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
from demo.main.models import Product, Category


class FullCategorySerializer(serializers.ModelSerializer):
    product_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class IdAndNameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = FullCategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=False)
    category = IdAndNameCategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


class ManualProductsListView(APIView):
    http_method_names = ['get', 'post']

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.validated_data)
            return Response(status=201)
        return Response(serializer.errors, status=400)


class ProductsListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = IdAndNameCategorySerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    # def get_queryset(self):
    def list(self, request, *args, **kwargs):
        print(self.request.user)
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        # executes serializer.save()
        return super().perform_create(serializer)


class SingleProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = IdAndNameCategorySerializer


class RandomView(ListAPIView, DestroyModelMixin):
    pass
