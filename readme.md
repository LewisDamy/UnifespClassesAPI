# Unifesp Course Catalog Platform

**Brief disclaimer:**
- This is a practice project that covers:
    - Developing API
    - Coding with Django Framework
    - Using technology to solve real-life problems
    

I started this project to learn new technologies, improve coding skills in Python (more
specifically with [Django REST Framework](https://github.com/encode/django-rest-framework), ORM & API. This is a continuation of the
[UnifespTables](https://github.com/LewisDamy/Tabelas_de_UCs_Unifesp) project.
The focus here is to demonstrate the
power of Django as a backend framework, while learning about and starting
my first open-source project tha focuses on building a better system to help Unifesp students
when selecting their subjects in each semester.



***

### About the tool:

Firstly this code starts after the conversion from a .csv file to the .db file 
from the [database.py](https://github.com/LewisDamy/Tabelas_de_UCs_Unifesp/blob/main/database.py) file.


## Django REST API
![Postman Request API](https://github.com/LewisDamy/UnifespClassesAPI/blob/main/images/PostmanRequestAPI.png)

### **Features**

**HTTP Methods**
- `GET` - Request retrieve resource information
- `POST` - The server creates a new entry in a database
- `PUT` - Updates an existing resource
- `DELETE` - Deletes resource or related component 

Usage
---
- Creating virtual environment:
```python
python -m venv venv
```
- Installing requirements:
```makefile
make install
```
- Running the server:
```python
python manage.py runserver
```
Open the browser or Postman tool and start making http requests!

### Connection between projects
I've made a copy from the [unifespSubjects.db](https://github.com/LewisDamy/Tabelas_de_UCs_Unifesp/blob/main/unifespSubjects.db)
from the [UnifespTables](https://github.com/LewisDamy/Tabelas_de_UCs_Unifesp) project into the Django database by using the following commands:

#### Inside the [unifespSubjects.db](https://github.com/LewisDamy/Tabelas_de_UCs_Unifesp/blob/main/unifespSubjects.db):
```sqlite
.output ucs.sql
.dump ucs
.quit
```

#### Inside the db.sqlite3 from Django:
```sqlite
.read .read ucs.sql
INSERT INTO unifespClasses_subject SELECT * FROM ucs;
```

<p>
After that, the data from the previous project has been insert into our Django application.
</p>

***
### Goals:
<p>
The goal is to improve and grow the project in order to make the lives of our Undergrads easier.
</p>

- Some improvements/features on the horizon:
    - Features:
        - Better UI
        - Platform with Auth
    - Code improvements:
    - Implement Docker containerization
    - Automated testing