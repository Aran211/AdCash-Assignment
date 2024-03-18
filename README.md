The Bitcoin Wallet REST API project is a web application built using Flask and Python. This was a new task for me since the python course at school didn't cover OOP or api-s. I learned OOP in Java, but a couple of youtube videos and examples gave me a good idea.
To test the API-s and get to know what exatly they where I used postman.


I used Pycharm when creating this project so I suggest to use that.
First thing after opening the project also open PgAdmin4 and create a PostgreSQL database, and change the config.py file that it can connect to the database.
A flaw is that some times it didn't want to create the table transactions on the first try then i ran this: #main class #with app.app_context(): #db.create_all().
Make sure the SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost/Adcash_db' change postgres:123 according to the username and password you set when creating the database
Next thing make sure the IDE has the necessary imports, for Windows I used 'pip install flask' and so on for flask_sqlalchemy...
After these steps if there are no more module errors the project should be ready to compile.
Go to the app.py which is the main class for this application. The application should show this text in the console:  * Serving Flask app 'app'
'Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
Running on http://127.0.0.1:5000
Press CTRL+C to quit'.
Now in pyCharm if the http is clicked it automatically opens the page, but if other IDE-s don't then just copy the line where http:// is to your browser. It should open the html file that represents the backend part of the application.
Now the pretty simple and bland page should show the Bitcoin and Eur balance and below that the transactions. I also included the script that I used for sample data in the models.py file. I inserted 1000 samples so the page is pretty long.
Now the application should run fine and show my work.:)
The html and css files should work fine and don't need to be touched.


Used sources:
https://www.youtube.com/watch?v=q2SGW2VgwAM&t=272s
https://www.youtube.com/watch?v=GMppyAPbLYk
https://courses.cs.ut.ee/2023/programmeerimine/fall/Main/Oop2
