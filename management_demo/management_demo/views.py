from rest_framework.response import Response
from django.http import HttpResponse 
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .utils.helper_utils import (load_data_helper, delete_all_data_helper)
from .utils.db_utils import (get_products, get_product, insert_product, delete_product, update_product_details) 
from .serializer import ProductSerializer
from django.core.cache import cache

class ProductsView(APIView):
    def get(self, request, product_id=None):
        if product_id:
            # could be in cache
            product = get_product(product_id)
            if product is None:
                return Response("Product does not exist", status=status.HTTP_404_NOT_FOUND)
            serializer = ProductSerializer(product)
            return Response({"product": serializer.data})
        # get all products
        products = get_products()
        return Response({"products": products})

    def post(self, request):
        # if bulk product insertion, request would be an array instance instead of a dictionary
        if isinstance(request.data, list):
            new_products_details = request.data
            failed_insertions = []
            for new_product_details in new_products_details:
                serializer = ProductSerializer(data=new_product_details)
                if serializer.is_valid():
                    insert_product(serializer)
                else:
                    failed_insertions.append(new_product_details)
                    continue
            return Response({"message": {"success": len(request.data)-len(failed_insertions), "failed": len(failed_insertions)}}, status=status.HTTP_400_BAD_REQUEST)

        new_product_detail = request.data
        serializer = ProductSerializer(data=new_product_detail)
        if serializer.is_valid():
            insert_product(serializer)
            return Response({"message": "product created"}, status=status.HTTP_201_CREATED)
        else:
            print("error here")
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, **kwargs):
        product_id = kwargs.get('product_id')
        # check if product_id is even in the paramater
        if not product_id:
            return Response("Product ID is not provided with DELETE HTTP request", status=status.HTTP_400_BAD_REQUEST)

        if not delete_product(product_id): 
            return Response("Product does not exist, deletion failed", status=status.HTTP_404_NOT_FOUND)
        
        # TODO@schen133: BULK deletion

        return Response({"message": "product " + str(product_id) + " deleted"}, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        product_id = kwargs.get('product_id')
        
        if not product_id:
            return Response("Product ID is not provided with PUT HTTP request", status=status.HTTP_400_BAD_REQUEST)
        
        og_product = get_product(product_id) 
        if not og_product:
            return Response("Product does not exist", status=status.HTTP_404_NOT_FOUND)

        fields_to_update = request.data

        if not update_product_details(og_product, fields_to_update):
            return Response("Update failed", status=status.HTTP_400_BAD_REQUEST)
        
        return Response("Product updated", status=status.HTTP_200_OK) 
        
# helper API calls
@api_view(['POST'])
def load_data(request):
    if request.method == "POST": 
        mock_data= request.data

        load_data_helper(mock_data)
    return Response("Data loaded")

@api_view(['POST'])
def delete_all_data(request):
    delete_all_data_helper()
    return Response("Data deleted")