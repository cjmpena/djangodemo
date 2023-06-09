from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get    -> list -> Queryset
    get    -> retrieve -> Product Instance Detail View
    put    -> Update
    patch  -> Partial Update
    delete -> destroy
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default
    
    
    
class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    '''
    get    -> list -> Queryset
    get    -> retrieve -> Product Instance Detail View
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default
    
Product_list = ProductGenericViewSet.as_view({'get': 'list'})
Product_list = ProductGenericViewSet.as_view({'get': 'retrieve'})