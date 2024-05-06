This is a back-end api server for a simple product management system. It handles GET, POST, DELETE, and PUT requests.
## Tech Stacks
- Django rest framework
- SQLite
- Redis
## Setup  
1) Clone github directory
```
git clone https://github.com/schen133/rest-server.git 
```
2) cd into project directory and start python virtual environment
```
//Mac os
source venv/bin/activate
```
3) download all required modules
```
pip install -r requirements.txt
```
4) cd into management_demo directory and start server
```
cd management_demo
python manage.py runserver 
```
The app will now be running on http://127.0.0.1:8000/
### Database
When you clone the repository, it should have some initial mock data loaded in the database already. (See *db.sqlite3*) If you would like to load in your own database. Please send post request to http://127.0.0.1:8000/loadData along with a request data of items (Array of dictionaries) you wish to add to the Product table. 
## Design
This project has two Django apps, one is called "management_demo" and the other is called "base".  
**management_demo**  
The "management_demo" app is for the purpose of our REST server, it contains majority of the important code written such as *views.py*, *urls.py*, and *serializer.py*.
**base**  
The "base" app is for the purpose of the database model we need, which is "Product".
**caching**  
The server integrates Redis as a caching solution. Caching happens when you try to get a product with a new product id, so the next time you try to get the same product with the product id again, it will hit the cache. It also happens whenever you send a put request to update the product, it will also update the product value. Whenever you delete a product from table through a delete http request, server will remove entry from cache table as well.
## Functionalities and API endpoints
**GET /products**   
This endpoint returns all products currently on the Product table.   
**GET /products/id**  
This endpoint returns a single product using the primary key (product id).  
**POST /products**  
This endpoint allows you to add a product to the product table in the database. It takes in a json dictionary containing all fields of a single product. (name, description, price, in_stock). You can also pass in an array of dictionaries as the post request data, this allows you to bulk add products.  
**PUT /products/id**  
This endpoint allows you to update an **existing** product. Simply call a PUT request along with a request data of a dictionary that contains the key and value pairs of attributes you wish to update. It allows partial updates, so if you simply want to update the name field or description field, you are welcome to do so.  
**DELETE /products/id**  
This endpoint allows you to delete a specific product.  