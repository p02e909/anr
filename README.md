# ANR

This program allows users to input element_master.csv and menu_master.csv file, then generate 10 menu with 5 element each menu. 

## Table of Contents

- [Usage](#usage)

## Installation

### Clone the Repository

Clone the repository to your local machine using Git:


```
git clone https://github.com/p02e909/anr.git
```
Change branch to new_req_22082024
```
git checkout new_req_22082024
```
## Usage
Please create Database postgresql with parameter in .env

This source using python3.8.0
### Run the Development Server

Export environment variables from .env file
```
export $(grep -v '^#' .env | xargs)
```
Create the database
```
psql -h $DB_HOST -U $DB_USER -c "CREATE DATABASE $DB_NAME;"
```

Start the development server:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
The application will be available at http://localhost:8000

Data show at:
http://localhost:8000/data/