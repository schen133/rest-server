from base.models import Product
from ..serializer import ProductSerializer 
from django.core.cache import cache

def check_product_exists(product_id):
    if Product.objects.filter(id=product_id).exists():
        return True
    else:
        return False

def insert_product(new_product):
    new_product.save()
    # cache newly inserted product
    cache.set(new_product.instance.id, new_product.instance)

def delete_product(product_id):
    if check_product_exists(product_id):
        Product.objects.get(id=product_id).delete()
        # clear cache
        cache.delete(product_id)
        return True
    else:
        return False

def get_product(product_id):
    # if in cache
    if cache.get(product_id):
        print("Cache hits")
        return cache.get(product_id)

    if check_product_exists(product_id):
        product = Product.objects.get(id=product_id)
        cache.set(product_id, product)
        return product 
    else:
        # product does not exist
        return None

def get_products():
    all_products = Product.objects.all()
    serializer = ProductSerializer(all_products, many=True)
    return serializer.data 

def update_product_details(og_product_serializer, fields_to_update):
    # pass in og serializer
    serializer = ProductSerializer(og_product_serializer, data=fields_to_update, partial=True)
    if serializer.is_valid():
        serializer.save()
        # cache the id with the serializer instance (Product instance)
        cache.set(serializer.instance.id, serializer.instance)
        return True
    else:
        return False
