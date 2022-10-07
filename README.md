# Data Extraction and Conversion using Python

A python connector to convert MySQL data to CSV file using Python

## Installation

Download the Folder

Install the following libraries before execution(Ignore if already installed)

```bash
pip install mysql-connector-python
```

```bash
pip install pandas
```

## Running the Program
##### After performing the necessary steps mentioned above, run the main.py file

It will prompt you to enter your MySQL server details like,

HOST, USER, PASSWORD, PORT, DATABASE(on which the table is stored)

##### Once verified it will ask you to upload the path of your SQL FILE that contains the query for execution

Example path(Windows): C:\Users\DELL\Documents\My Docs\testsql.sql

Then the program will print the executed operation on the console

##### For converting to CSV

Prompt will appear with Y/N option, choose Y for converting else N otherwise