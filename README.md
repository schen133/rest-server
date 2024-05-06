This is a back-end api server for a simple product management system. It handles GET, POST, DELETE, and PUT requests.
## Tech Stacks
___
- Django rest framework
- SQLite
- Redis
## Setup  
___
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
## Design
___
This project has two Django apps, one is called "management_demo" and the other is called "base". 
#### management_demo
The "management_demo" app is for the purpose of our REST server, it contains majority of the important code written such as *views.py*, *urls.py*, and *serializer.py*.
#### base 
The "base" app is for the purpose of the database model we need, which is "Product".
#### Functionalities and API endpoints
___
**GET /products**
this
