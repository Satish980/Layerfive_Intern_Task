# Layerfive_Intern_Task

This repo consists of Codes of Read and Add Operations Using Django task given by Layerfive

# Problem Statement
  
    Brief Django API
	1. Create an API for a user request which will take the following input parameters:
	• First Name
	• Last Name
	• Email
	• Phone Number
	• Address (Address Line1, Address Line2, City, Zipcode, State)
	
	2. Create an API which will retrieve all the user request data
	3. Create a Angular form (or use any front-end javaScript library or simple HTML if not familiar with JavaScript) which will have  the fields mentioned in the above API, Integrate the API to submit the form data.
	4. Create a page to display submitted data on another page

	Ø Use Django Rest Framework to achieve the above goal
	Ø Use Postgres as database and use migrations to create the tables
	Ø Follow python guidelines and coding standards
  
# Solution
  
    1. To achieve the task i have used HTML and Django
    2. Technologies Used
       Frontend: HTML, Bootstrap
       Backend : Django
       Database: PostgreSql
    3. Live Link: https://layerfive-django-task.herokuapp.com/

# Procedure
   1. Download the code or clone the repository using below link
   	
	https://github.com/Satish980/Layerfive-Intern-Task.git
	
   2. Install all the modules using below command
   
   			
	pip install -r requirements.txt
   3. Now go to the settings.py file of the Django App. Under the settings for Databases, change the settings from current database to
      your database name, user name and password and host 
      
      	  DATABASES={
		  'default':{
		      'ENGINE':'django.db.backends.postgresql_psycopg2',
		      'NAME':'your_project_name',
		      'USER':'user_name',
		      'PASSWORD':'password',
		      'HOST':'localhost',
		      'PORT':'5432',
		    }
		  }
   4. Now run the below command to convert all the models into queries for the database.

	python manage.py makemigrations
   5. Now run the below command to migrate these changes into our database.

	python manage.py migrate
   6. Now run the below command to execute the project

	python manage.py runserver
   7. Now copy the url you got from command line and open it in the browser to view the project. In my case that url is
   
   		http://127.0.0.1:8000/
   # Thank You

	
