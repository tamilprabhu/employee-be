# employee-be

## Install Required Packages

```bash
pip install flask mysql-connector-python flask_cors
```

## Run the Python File

```bash
python main.py
```

# MySQL Database Setup

## Create Database

```sql
CREATE DATABASE `employee`;
```

## Create Table

```sql
CREATE TABLE `employee` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(25) NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    `position` VARCHAR(15) NOT NULL,
    `department` VARCHAR(15) NOT NULL
);
```

## Insert Sample Data

```sql
INSERT INTO employee (id, name, email, position, department) VALUES
(1, 'Alice', 'alice@gmail.com', 'Software Dev', 'Engineering'),
(2, 'Bob', 'bob@fmail.com', 'BA', 'Marketing'),
(3, 'Charlie', 'charlie.98@yahoo.in', 'Associate', 'HR');
```


pip install langchain openai mysql-connector-python sqlalchemy

pip install langchain-experimental

https://github.com/datacharmer/test_db.git