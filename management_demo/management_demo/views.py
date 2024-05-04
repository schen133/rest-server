from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .utils.helper_utils import (deleteAllDataHelper, loadDataHelper)
from .utils.db_utils import (getAllProducts, getProduct, insertNewProduct, deleteProduct, checkProductExists)
from .serializer import ProductSerializer

class ProductsView(APIView):
    def get(self, request, product_id=None):
        if product_id:
            product = getProduct(product_id)
            if product is None:
                return Response("Product does not exist", status=status.HTTP_404_NOT_FOUND)
            product = ProductSerializer(product).data
            return Response({"product": product})
        # get all products
        products = getAllProducts()
        return Response({"products": products}) 

    def post(self, request):
        
        return Response("Create a product", status=status.HTTP_201_CREATED)
        
    def delete(self, request):
        # this is delete
        pass 

    def put(self, request):
        # this is put
        pass 

# helper API calls
@api_view(['POST'])
def loadData(request):
    if request.method == "POST": 
        mockData = request.data
        loadDataHelper(mockData)
        print(mockData)
    return Response("Data loaded")

@api_view(['POST'])
def deleteAllData(request):
    deleteAllDataHelper()
    return Response("Data deleted")

        