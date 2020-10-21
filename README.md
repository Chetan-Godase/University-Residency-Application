# Software-Engineering-Final

## Introduction
Hey guys, I've created the skeleton we can work off of for our Django project. I've incorporated bootstrap into the base.html so any template extending this one can use bootstrap 4 components. Please review my base.html along with login.html to get an idea of how template inheritance works in Django and what you need to include in your template.


## Quick Project Rundown
  1. lu_residence_webapp is the project name and contains all files required to run the website. You'll notice there is also a directory under this top project directory with the same name. The files contained in this sub-clone directory affect the entire project (have to do with configurations). 
  2. The other directories (e.g. common & home) are known as Django apps. A Django project(aka website) can contain multiple apps. This facilitates for easy reusability but I think we'll be okay with just putting all our stuff in one app (home) for now.
  3. Look at the files under the common app and home app... The common app is used to store static files (e.g. html templates, images, etc.) and home is where our logic is (specifically in views.py).
  4. Under our home app, you'll want to pay attention to view.py and urls.py (and maybe models.py if you need to create and store info in MySQL).
  5. When you create a template for 'news' for example, you need to create a function in views that takes a request and returns a template. 
  
## Setup Steps
  1. Clone this repository onto your local machine,
  2. Download MySQL onto your machine to setup the backend,
  3. Create a database using MySQL Command Line,
  ```
  CREATE NEW database_name;
  ```
  4. Create a new user and set priviledges for it so that the webapp can access and manipulate the new database,
  ```
  CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
  GRANT ALL PRIVILEGES ON database_name.* TO 'newuser'@'localhost';
  FLUSH PRIVILEGES;
  ```
  5. Go to settings.py, scroll down to DATABASEs dictionary (around line 80) and specify your database name, with the new user username and password,
  6. Install Django globally on your machine,
  ```
  pip install Django==3.1.2
  ```
  7. cd into lu_residence_webapp (the root/outer one) and run the below command. 
  This will add the required tables the django project needs to your database you specified in settings.py. 
  ```
  py manage.py migrate
  ```
  8. You should now be ready to run the development server. 
  ```
  py manage.py runserver
  ```
## If we could all...
 - Keep our static files (html, css, js, etc.) in the common directory under their respective sub-directory (e.g. templates, static, images).
 - Try not to change the base.html or base.css static files often if at all as these will affect all sub-templates (e.g. news, login, register, etc.)
 - Be specific with your commit summaries.
 - Only commit when finished a section/week (just don't commit for every small change.
 - Don't move the login.html or register.html templates under the register directory as Django requires this due to built-in libraries for user authentication and authorization.

