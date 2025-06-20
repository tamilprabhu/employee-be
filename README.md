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

## 🧪 Example: `cURL` Command

```bash
curl --location --request POST 'https://127.0.0.1:5000/query' \
--header 'Content-Type: application/json' \
--data '{
    "prompt": "Who is the current manager of Customer Service department ?"
}'
```
### 📥 Request Body

| Field  | Type   | Description                          |
| ------ | ------ | ------------------------------------ |
| prompt | string | Natural language question to the API |

---

### 📤 Sample Response

```json
{
    "answer": "The current manager of the Customer Service department is Jane Doe."
}
```

## 🧪 Example: `cURL` Command

```bash
curl --location --request GET 'http://127.0.0.1:5000/employees'
```
