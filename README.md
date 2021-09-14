# CS340DB

## Specifications
*The CS340 Project that you will submit at the end of this course should satisfy all these specifications:*

1. Your database should be pre-populated with sample data. At least three rows per table is expected. The sample data should illustrate a table's functionality, e.g. if the table is part of a many-to-many relationship, the sample data should depict M:M.
2. When planning, your database should have at least 4 entities and at least 4 relationships, 2  of which must be a many-to-many relationship.  The entities and relationships should implement the operational requirements of your project, see individual project steps for weekly instruction.
*Note for this project you will be asked to identify 2 M:M relationships in the planning phase, however will only be required one for your final project execution. You will still need 4 - relationships for final implementation - two - 1:M, one - M:M and the last relationship can be any other relationship of your choice.* 
3. It should be possible to INSERT entries into every table individually.
4. Every table should be used in at least one SELECT query. For the SELECT queries, it is fine to just display the content of the tables, but your website needs to also have the ability to search using text or filter using a dynamically populated list of properties. This search/filter functionality should be present for at least one entity. It is generally not appropriate to have only a single query that joins all tables and displays them.
5. You need to include one DELETE and one UPDATE function in your website, for any one of the entities. In addition, it should be possible to add and remove things from at least one many-to-many relationship and it should be possible to add things to all relationships. This means you need INSERT functionality for all relationships as well as entities. And DELETE for at least one many-to-many relationship.
6. At least one 1:M relationship must be NULL-able (like bsg_people to bsg_planets); that is to say, you should be able to set the foreign key value to NULL (such as on a person in bsg_people), that removes the relationship. In case none of the one-to-many relationships in your database has partial participation, you would need to change that to make sure at least one can have NULL values. 
7. In a many-to-many relationship, to remove a relationship one would need to delete a row from a table. That would be the case with bsg_people and bsg_certifications. One should be able to add and remove certifications for a person without deleting either bsg_people rows or bsg_certification rows. If you implement DELETE functionality on at least (1) many-to-many relationship table, such that the rows in the relevant entity tables are not impacted, that is sufficient.
 
## General Rules and Grading
1. Can be developed using any technology platform which serves content over the web.
2. Should use MySQL/MariaDB as the database back end.
3. You should write all the queries and not depend on an ORM or similar mechanism to generate any queries.

--------------------------------------------------------------------------------------------------------------------------------------------

Steps on how to run app.py

Before Starting 
- Basically a watered down version of (https://github.com/osu-cs340-ecampus/flask-starter-app)
- Make sure to download and start ‘MySQL Server’ (https://dev.mysql.com/downloads/mysql/


1. Open terminal and type “cd /Users/<username>/Documents" (or wherever else you want to save the project)
2. Then type “git clone https://github.com/Armonymon/cs340-database-project.git” to clone the project into that folder
3. Open the cs340-database-project folder in VScode
4. Click the “.gitignore” file and delete the text ‘.env’ then save the file
5. Make a new file called “.env” and copy and paste this… then save the file

340DBHOST=localhost

340DBUSER=root
  
340DBPW=<The password you set for MySQL when you downloaded it (in system preferences)>
  
340DB=CS340DB

6. Now open the “.gitignore” file again and add back the text ‘.env’ then save and close the file
7. Open a new terminal in VScode and make sure you are in the root project directory (cd /Users/<username>/Documents/cs340-database-project)
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
5. Run “source /Users/<username>/Documents/cs340-database-project/database/database.sql”
6. If you want to check if the database was added, run “SHOW TABLES;” to see tables
7. When you’re done run “quit”

Useful commands:

source ./venv/bin/activate

python3 app.py

mysql -u root -p

SET FOREIGN_KEY_CHECKS=0;
