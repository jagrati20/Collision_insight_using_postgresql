Collisions Insight Project
This project utilizes four relational datasets and one non-relational dataset. For non-relational database, this project makes use of XML.

What's in the application
The directory contains the following files:

requirements.txt: Run this file to install all the dependencies that are required for the project. It should be run as 
                    pip install -r requirements.txt
                    
datasets.txt: This file contains the URLs for all the datasets that are required for the successful execution of this 
              project

retrieve_data.py: The execution of this file generates a directory named Datasets and will fetch the datasets in the .csv 
                  format from the URLs present in the datasets.txt file 
                  
load_data.py: This file contains the code that accomplishes data loading. All datasets from the created Datasets directory are 
               loaded into their respective tables

schema.sql: This Postgres SQL file contains the schema for all datasets.

application.py: This file is the main file that needs to be run in order to run the project application.

database.py: This file contains the code that consists of all the queries that a user can run on the datasets.

database-setup.sql: This file contains the SQL which sets up the required database for usage.

Setup

1) The requirements.txt file should be run first followed by the database-setup.sql file. lxml, which is a key component of
the project, which relies on the libxml2 library needs to be installed as well if not done so already.

Running pip install -r requirements.txt will run the requirements.txt file and  

Running
As with homework 5, this makes use of the python unittest module. You can run the tests by running python -m unittest 
query_tool_test.py from the homework-6 directory.