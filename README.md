# Software-Engineering-Final

## Introduction
Hey guys, I've created the skeleton we can work off of for our Django project.

## Quick Project Rundown
  1. lu_residence_webapp is the project name and contains all files required to run the website. You'll notice there is also a directory under this top project directory with the same name. The files contained in this sub-clone directory affect the entire project (have to do with configurations). 
  2. The other directories (e.g. common & home) are known as Django apps. A Django project(aka website) can contain multiple apps. This facilitates for easy reusability but I think we'll be okay with just putting all our stuff in one app (home) for now.
  3. Look at the files under the common app and home app... The common app is used to store static files (e.g. html templates, images, etc.) and home is where our logic is (specifically in views.py).
  4. Under our home app, you'll want to pay attention to view.py and urls.py (and maybe models.py if you need to create and store info in MySQL).
  5. When you create a template for 'news' for example, you need to create a function in views that takes a request and returns a template. 
  
##
## To run
  1. To run a test server to debug the 
  code using:
  ```commandline
  >py manage.py runserver
  ```
