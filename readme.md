# Collisions Insight Project

This project utilizes four relational datasets and one non-relational dataset. For the non-relational database, this project makes use of XML.

## What's in this application

The directory contains the following files:

`requirements.txt` : This file is to install all the dependencies required for this project. 
                    
`datasets.txt` : This file contains all the URLs required for the datasets for the successful execution of this project

`retrieve_data.py` : This file will generate a directory named `datasets`, and it will fetch the datasets from the URLs present in `datasets.txt` to .CSV format.
                  
`load_data.py` : This file contains the code that accomplishes data loading. It will load all the datasets from the created Datasets directory into their respective tables.

`schema.sql` : This PostgreSQL file contains the schema required for all datasets.

`application.py` : This file is the main file that needs to be run to execute the project.

`database.py` : This file contains the code that sets up a connection with the Postgres database and consists of different functions to executes queries.

`database-setup.sql` : This file contains the database set up code for the user and grants appropriate permissions to the user

## Setup

1. Run the `requirements.txt` file from the terminal as
```
pip install -r requirements.txt 
```
2. Run the `database-setup.sql` file as 
```
psql -U postgres postgres < database-setup.sql   
```               
3. Run the `retrieve-data.py` file to set up the datasets directory.
