from django.test import SimpleTestCase 
from django.urls import reverse, resolve
from .. import views

class TestURLs(SimpleTestCase):

    # *** Named Urls ***
    # products
    # products_with_id

    # *** all products ***
    def test_products_get(self):
        url = reverse('products')
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, views.ProductsView)

    # *** one product with id ***
    def test_products_arg_resolves(self):
        # try passing in random args, if non-int, it should be not good
        url = reverse('products_with_id', args=['1'])
        resolver =  resolve(url)
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, views.ProductsView)

    
