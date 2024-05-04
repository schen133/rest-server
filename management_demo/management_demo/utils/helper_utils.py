from base.models import Product

def loadDataHelper(data):
    for row in data:
        name = row['name']
        description = row['description']
        tempPrice = row['price']
        price = float(tempPrice.replace('$', ''))
        in_stock = row['in_stock']
        tempProduct = Product(name=name, description=description, price=price, in_stock=in_stock)
        tempProduct.save()
    print("Initial data loaded")

def deleteAllDataHelper():
    Product.objects.all().delete()
    print("All data in database deleted")
    
    
