# ETL Pipeline v1
by Sarah Haq

## Introduction
This code contains the steps to build an ETL pipeline that carries out the following tasks:
- Extracts 400k transactions from Redshift
- Identifies and removes duplicates
- Loads the transformed data to a s3 bucket

## Requirements
The minimum requirements:
- Python 3+

## Instructions on how to execute the code

1.Clone the repository, and go to week19 folder
````
 git clone 
````
2. Install the libraries
````
pip3 install -r requirements.text
````
3. Copy the `env.example` file to `.env` and fill out the environment
4. Run the `main.py` script
````
pyhton main.py
````