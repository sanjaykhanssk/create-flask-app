# {{APPNAME}}
### Author - {{USERNAME}}
{{DESCRIPTION}}



## Basic configuration

#### Activate Virtuval enviroment

source bin/activate

#### Enviroment Variables

export DB_HOST=localhost DB_USER={yourUserName} DB_PASSWORD={yourpassword} DB_NAME={databaseName} FLASK_ENV=development FLASK_APP=app.py 

#### DB migrations

> python migrate.py db init

> python migrate.py db migrate 

> python migrate.py db upgrade 

In case migration error

> python migrate.py db stamp head 

> python migrate.py db current 

> python migrate.py db migrate 

> python migrate.py db upgrade 

---
> created with create-flask-app