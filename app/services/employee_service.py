from app import db
from app.models.employee import Employee

class EmployeeService:
    @staticmethod
    def create_employee(data):
        employee = Employee(**data)
        db.session.add(employee)
        db.session.commit()
        return employee

    @staticmethod
    def get_employees(page, per_page, department=None, role=None):
        query = Employee.query
        if department:
            query = query.filter_by(department=department)
        if role:
            query = query.filter_by(role=role)
        return query.paginate(page=page, per_page=per_page)

    @staticmethod
    def get_employee_by_id(id):
        return Employee.query.get_or_404(id)

    @staticmethod
    def update_employee(employee, data):
        for key, value in data.items():
            setattr(employee, key, value)
        db.session.commit()
        return employee

    @staticmethod
    def delete_employee(employee):
        db.session.delete(employee)
        db.session.commit()

    @staticmethod
    def check_email_exists(email):
        return Employee.query.filter_by(email=email).first() is not None