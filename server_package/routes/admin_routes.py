from server_package import app
from server_package.controllers.admin_controller import AdminController as AC


@app.delete("/delete/all")
def delete_all():
    """Deletes all tables in the database"""
    AC.drop_all()
    return {"message": "Deleted all tables in database"}


@app.post("/create/tables")
def create_tables():
    """Create tables from Models"""
    AC.create_tables()
    return {"message": "Created User and Promotions tables"}
