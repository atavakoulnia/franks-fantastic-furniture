# CS340DB
~~UPDATED: 8/3 - 9:00pm~~

~~UPDATED: 8/4 - 1:18pm~~

UPDATED: 8/4 - 7:00pm


What works:

- SELECT for Customers, Orders, Transactions, Products, Employees
- INSERT for Customers, Products, Employees
- UPDATE not yet implemented (requirements say we only need an UPDATE for just one table/page)
- DELETE for Customers, Orders, Transactions, Products, Employees
- Search/filter is fully functional for Customers (only need one)

What we need:
- INSERT for Transactions
- Fix INSERT for Orders
- Fix DELETE relationship between Transactions/Orders (not too important)

More info:
- The INSERT function works for Orders sometimes. I'm pretty sure it's something to do with the foreign keys.
- I attempted writing the code for UPDATE (see file 'example-code-for-update-customers(temp).html')
- The DELETE function works for all the tables but for example, if I delete a row from the Transactions table (page), it does not delete the row associated with the order_id in the Orders table (page). I don't think it's a big deal? Not sure if we will get points off. 


--------------------------------------------------------------------------------------------------------------------------------------------


Steps on how to run app.py

Before Starting 
- Basically a watered down version of (https://github.com/osu-cs340-ecampus/flask-starter-app)
- Make sure to download and start ‘MySQL Server’ (https://dev.mysql.com/downloads/mysql/


1. Open terminal and type “cd /Users/<username>/Documents" (or wherever else you want to save the project)
2. Then type “git clone https://github.com/Armonymon/CS340DB.git” to clone the project into that folder
3. Open the CS340DB folder in VScode
4. Click the “.gitignore” file and delete the text ‘.env’ then save the file
5. Make a new file called “.env” and copy and paste this… then save the file

340DBHOST=localhost

340DBUSER=root
  
340DBPW=<The password you set for MySQL when you downloaded it (in system preferences)>
  
340DB=CS340DB

6. Now open the “.gitignore” file again and add back the text ‘.env’ then save and close the file
7. Open a new terminal in VScode and make sure you are in the root project directory (cd /Users/<username>/Documents/CS340DB)
8. Run “pip3 install virtualenv” to install the virtual environment
9. Then run "python3 -m venv ./venv”
10. Now, activate the virtual environment by running “source ./venv/bin/activate”
11. Run “pip3 install -r requirements.txt” to install the packages required to run the project
12. Then, completely close out (command-Q) VScode and reopen it
13. Run “source ./venv/bin/activate” again to activate the virtual environment
14. Finally, run “python3 app.py” and boom it should work! 


After this, the only thing you have to remember to do every time before coding is to activate the virtual environment and start the MySQL server. 


--------------------------------------------------------------------------------------------------------------------------------------------


If the database is empty…

1. Open terminal in VScode and navigate to the database folder directory “cd /Users/<username>/Documents/CS340DB/database”
2. Run “mysql -u root -p”
3. Might have to type in the password you used to in step 5 from above
4. Run “USE CS340DB”
5. Run “source /Users/<username>/Documents/CS340DB/database/database.sql”
6. If you want to check if the database was added, run “SHOW TABLES;” to see tables
7. When you’re done run “quit”

Useful commands:

source ./venv/bin/activate

python3 app.py

mysql -u root -p

SET FOREIGN_KEY_CHECKS=0;
