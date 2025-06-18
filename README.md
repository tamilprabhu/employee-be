# employee-be

## Install Required Packages

```bash
pip install flask mysql-connector-python flask_cors
pip install langchain openai mysql-connector-python sqlalchemy
pip install langchain-experimental
```

# MySQL Database Setup

## Clone the repository:

```bash
git clone https://github.com/datacharmer/test_db.git
cd test_db
```

## **Login to MySQL** and run the provided SQL script:

```bash
mysql -uroot -proot < employees.sql
```


## Run the Python File

```bash
python main.py
```