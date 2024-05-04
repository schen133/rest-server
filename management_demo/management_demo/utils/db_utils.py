from base.models import Product

def checkProductExists(product_id):
    if Product.objects.filter(id=product_id).exists():
        return True
    else:
        return False

def insertNewProduct(new_product_details):
    pass

def deleteProduct(product_id):
    pass

def getProduct(product_id):
    if checkProductExists(product_id):
        product = Product.objects.get(id=product_id)
        return product
    else:
        # product does not exist
        return None

def getAllProducts():
    all_products_query = Product.objects.all()
    all_products = list(all_products_query.values())
    return all_products

        
    