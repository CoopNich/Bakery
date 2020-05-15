# Welcome to the Bakery

You have been tasked to build an app that will allow the employees of the bakery to manage the different breads that are baked.

## Project Setup

* Clone down the repo and `cd` into it

* Change this from a git repo to a regular directory:
  * `rm -rf .git`

* Create a new repository on Github and make your first commit with this boilerplate code:
  * Create a brand new repository under your account on Github
  * `git init`
  * `git add .`
  * `git commit -m "First commit with boilerplate code"`
  * `git remote add origin your-new-repos-ssh-remote-url`
  * `git push -u origin master`

* Create your OSX/Linux OS virtual environment in Terminal:

  * `python -m venv bakeryenv`
  * `source ./bakeryenv/bin/activate`

* Install the app's dependencies:

  * `pip install -r requirements.txt`

* All your models and migrations have already been created, so ahead and run migrations:

  * `python manage.py migrate`

* Create a superuser for your local version of the app:

  * `python manage.py createsuperuser`

* Populate your database with initial data from fixtures files: (_NOTE: every time you run this it will remove existing data and repopulate the tables_)

  * `python manage.py loaddata breads`
  * `python manage.py loaddata ingredients`
  * `python manage.py loaddata bread_ingredients`

* Make a copy of `breadapp/views/connection.py.example` and remove the `.example` extension and change the path to the database 

* Fire up your dev server and get to work!

  * `python manage.py runserver`


## Requirements

You need to meet the following requirements in the order they are listed since they build on each other. After each requirement has been met, please make sure you make a commit with a detailed commit message explaining what feature has been completed. You **do not** need to worry about authentication for this application.

1. When a user navigates to the root URL of the application (`/`), they should see a list of all the breads in alphabetical order.

1. Above the list of breads, provide a link that presents the user with a form to add a new bread by providing the name and region. When the form is submitted, the user should be directed to `/` and should see the newly added bread in the list.

1. Add a link to view the details of each bread for every item on the list of breads. When the user clicks on this link, they should see the name of the bread, the region, the names of the many ingredients that are needed to make that bread and the amount of each ingredient needed for the recipe.

1. Add a DELETE button next to each ingredient listed on the details page for a bread. When the user clicks this button, the ingredient should be removed from the ingredients list for that bread. **This action should not delete the ingredient itself!**

1. Add an EDIT button at the bottom of the bread details page. When the user clicks on the button, they should be presented with a form that lets them edit only the region of the bread. 
