Django 

Model - Template - View <br>
Template acts as View <br>
Framework itself acts as the Controller

### django-admin startproject <project_name>

Inside project directory there are various files automatically generated such as<br>
<b>asgi.py</b>
- Asynchronous Server Gateway Interface (ASGI) application with ASGI-compatible web servers. ASGI is the emerging Python standard for asynchronous web servers and applications.
- In the past, websites used a method called WSGI,It worked well, but it could only make the website do one thing at a time
- ASGI can make the website do many things at once if the website is finding a lot of information, it can still do other things like show images or respond to other people visiting the site.

### cd <project_name>
### python manage.py migrate

By applying the initial migrations, the tables for the applications listed in the INSTALLED_APPS setting are created in the database.

## Running the Dev Server

### python manage.py runserver

## Some project settings
- DEBUG = True by default. Django will throw detail error messages when exception is thrown directly on the browser if debug is ON. In production it needs to be turned off.
- ALLOWED_HOSTS - ALLOWED_HOSTS is not applied while debug mode is on or when the tests are run. Once the debug is false we need to add domain name of our site to it serve django site.
- INSTALLED_APPS - tells us which apps are active for this site
- MIDDLEWARE - states the middleware to be executed
- ROOT_URLCONF - ROOT_URLCONF indicates the Python module where the root URL patterns of your application are defined
- DATABASES - dictionary with all databases related settings

One django project which is a site may contain multiple applications inside it. 

###  python manage.py startapp <app_name>

## Creating a Django Model
- https://docs.djangoproject.com/en/4.1/ref/models/fields/
- A Django model is a source of information and behaviors of your data. It consists of a Python class that subclasses django.db.models.Model. 
- Define class in model - which will be table and all the fields inside the class will be columns in the database table
- There is one auto incrementing primary key created by Django but if we want we can add primary_key = True to any of our unique attribute
- The class Meta inside a Django model allows you to define metadata for the model. ordering attribute is used to sort the data while fetching.
- If we want to add index to our model need to add in same meta class in the indexes attribute which takes list.
- https://docs.djangoproject.com/en/4.1/ref/models/indexes/
- If we want to add custom table name in the model we can use db_table attribute in the meta classpyth
- It’s a good practice to define choices inside the model class and use the enumeration types. This will allow you to easily reference choice labels, values, or names from anywhere in your code.
- We can use already inbuilt django user model
- If you edit the model such as add, remove, or change the column or add new model then we will need to create new migrations again and apply using migrate command

### Add your app name in INSTALLED_APPS list in settings.py
<app_name>.apps.<app_name>Config

## Accessing Django Administration Site
### Create a Super user
#### python manage.py createsuperuser

### Customizing admin site
- In admin.py we can provide different attributes under class which inherits from admin.ModelAdmin such as
- list_display - while displaying the list of posts these columns will be displayed
- list_filer - allows us to filter attribute using these columns
- search_fileds - gives us search bar to search particular fields
- date_hierarchy - below search bar there is date filtering method to see the data
- ordering - default sorting criteria for posts
- prepopulated_fields - populates some fields based on the other fields entered
- raw_id_fields - look up widget instead of drop down as we may have lots of users
- https://docs.djangoproject.com/en/4.1/ref/contrib/admin/

## Django ORM
- It allows developers to perform database operations using Python code and object-oriented principles, without needing to write raw SQL queries.
- QuerySets are the primary way to interact with the database using Django ORM. A QuerySet is a collection of model objects retrieved from the database based on certain conditions or filters. 
- Overall, Django ORM simplifies database operations by providing a high-level Python API that abstracts away the complexities of SQL queries and database-specific code. It promotes code reusability, reduces the chance of SQL injection attacks, and allows developers to work with databases using Python objects and methods.
- get(), create(), Post.objects.all(), filter(), exclude(), order_by(), delete()
- Query set is not evaluated right away. It only runs when it is called and evaluates to give back result set.


## Creating Model Managers
- Default manager for any model we define is <b>objects</b> manager.
- There are two ways to add or customize managers for your models: you can add extra manager methods to an existing manager or create a new manager by modifying the initial QuerySet that the manager returns.
```
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                     .filter(status=Post.Status.PUBLISHED)
```
- The above code gives you the custom manager for post model with only give back published posts when requested the query set
- If you declare any managers for your model, but you want to keep the objects manager as well, you have to add it explicitly to your model.
```
class Post(models.Model):
    # model fields
    # ...
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
```


## Building list and detail views
- A Django view is just a Python function that receives a web request and returns a web response.
- First, you will create your application views, then you will define a URL pattern for each view, and finally, you will create HTML templates to render the data generated by the views.
- Creating a urls.py file for each application is the best way to make your applications reusable by other projects.

## Creating Templates for Views
- https://docs.djangoproject.com/en/4.1/ref/templates/language/
- Template tags control the rendering of the template and look like {% tag %}
- Template variables get replaced with values when the template is rendered and look like {{ variable }}
- Template filters allow you to modify variables for display and look like {{ variable|filter }}
- https://docs.djangoproject.com/en/4.1/ref/templates/builtins/
- {% load static %} tells Django to load the static template tags that are provided by the django.contrib.staticfiles application, which is contained in the INSTALLED_APPS setting.
- Always use the {% url %} template tag to build URLs in your templates instead of writing hardcoded URLs. This will make your URLs more maintainable.
- 