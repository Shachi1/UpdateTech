To run the tasks run,
1. python -m venv env
2. .\env\Scripts\activate
3. source env/bin/activate
4. install all the requirements
5. python manage.py migrate
6. python manage.py runserver

Task1: 

Code: Here the app named "api" implements login and registration API with DRF. In models.py, an Entity has been created for the user model using AbstractBaseUser class. In managers.py, a custom user manager has been created using BaseUserManager. Only the fields required for login and registration is added. views.py has UserDetailAPI class that gets user details using token authentication and RegisterUserAPIView class that registers user.

Output: 
The root directory takes to the Login page. Log in with email "*****@gmail.com" and password "****".
this will direct you to home page. Click the add button to register new user.

Task2:

Code: In models.py class SalesModel has been created and in migration/0001_initial.py necessary data has been loaded into sales_salesmodel table. load_csv is a command created in sales/migrations/commands. In pdfGenerator app, a pdf is generated in views.py and shown in report.html. In sales/views.py the method generate_chart() generates the pie and the line chart. show_query_result() executes all the queries for the information of the pdf report.


Output: The root directory will show some URL patterens. In "/data_insertion/" directory click the options button and scroll down. It will show the data insertion form. For data manupulation go to "/data_manipulation/1/". And finally, "/report" will show the query results and pie, line chart.

OutputImages: This folder contains all the screenshots of the outputs.
