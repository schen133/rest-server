from base.models import Product

def load_data_helper(data):
    for row in data:
        name = row['name']
        description = row['description']
        temp_price = row['price']
        price = float(temp_price.replace('$', ''))
        in_stock = row['in_stock']
        tempProduct = Product(name=name, description=description, price=price, in_stock=in_stock)
        tempProduct.save()

def delete_all_data_helper():
    Product.objects.all().delete()
    
    
