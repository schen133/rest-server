from base.models import Product
from ..serializer import ProductSerializer 

def check_product_exists(product_id):
    if Product.objects.filter(id=product_id).exists():
        return True
    else:
        return False

# also serialize
def insert_product(new_product):
    new_product.save()

# need to serialize
def delete_product(product_id):
    if check_product_exists(product_id):
        Product.objects.get(id=product_id).delete()
        return True
    else:
        return False

def get_product(product_id):
    if check_product_exists(product_id):
        product = Product.objects.get(id=product_id)
        return product 
    else:
        # product does not exist
        return None

def get_products():
    all_products = Product.objects.all()
    serializer = ProductSerializer(all_products, many=True)
    return serializer.data 

# serialize as well
def update_product_details(og_product_serializer, fields_to_update):
    # pass in og serializer
    serializer = ProductSerializer(og_product_serializer, data=fields_to_update, partial=True)
    if serializer.is_valid():
        serializer.save()
        return True
    else:
        return False
