from django.test import TestCase, Client
from django.urls import reverse 
from base.models import Product
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.products_url = reverse('products')
        self.load_data_url = reverse('load_data')
        self.delete_data_url = reverse('delete_all_data')
        # load up data, please input in the path to 
        f = open("mock_data/mock_data.json")
        mock_data = json.load(f)
        f.close()
        mock_data = json.dumps(mock_data)
        # call load
        self.client.post(self.load_data_url, data=mock_data, content_type='application/json')
    
    # *** GET ***
    def test_products_all_GET(self):
        total_row_counts = Product.objects.all().count()
        response = self.client.get(self.products_url)
        returned_row_counts = len(response.data["products"])
        self.assertEqual(returned_row_counts, total_row_counts)

    # *** POST *** 
    def test_delete_all_data(self):
        response = self.client.post(self.delete_data_url)
        print("after deletion")
        print(Product.objects.all().count())
        self.assertEqual(Product.objects.all().count(), 0)




        
        
    
