## marketing-dashboard-server

Simple REST API server made with Flask and SQLAlchemy.

### Get Started

Create a Python virtual enviroment. This app is built with `Python 3.11.2`.

```
cd <project-root>
py -m venv venv
```

Start the virtual enviroment and upgrade `pip`. On windows from root of project, run the following commands.

```
source venv/Scripts/activate
py -m pip install --upgrade pip
```

From project root, run the following command to download the modules and libraries from `requirements.txt`.

```
pip install -r requirements.txt
```

When adding new modules and packages to the project, update the `requirements.txt`.

```
pip freeze > requirements.txt
```

### Resources

[Column keys](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Column.__init__)

[SQL Data Types](https://docs.sqlalchemy.org/en/20/core/types.html)

[Column Options](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Column.params.*args)

[Relationships Config](https://docs.sqlalchemy.org/en/20/orm/relationships.html)

[Relationships API](https://docs.sqlalchemy.org/en/20/orm/relationship_api.html)

[Model](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/api/#flask_sqlalchemy.model.Model)

[Session.execute()](https://docs.sqlalchemy.org/en/20/orm/session_api.html#sqlalchemy.orm.Session.execute)
