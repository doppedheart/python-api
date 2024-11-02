from app.services.employee_service import EmployeeService
from app.schemas.employee_schema import EmployeeSchema
from flask import jsonify

class EmployeeController:
    @staticmethod
    def create_employee(data):
        validation_errors = EmployeeSchema.validate_create(data)
        if validation_errors:
            return jsonify({'errors': validation_errors}), 400

        if EmployeeService.check_email_exists(data.get('email')):
            return jsonify({'error': 'Email already exists'}), 400

        employee = EmployeeService.create_employee(data)
        return jsonify(employee.to_dict()), 201

    @staticmethod
    def list_employees(page, per_page, department, role):
        pagination = EmployeeService.get_employees(page, per_page, department, role)
        return jsonify({
            'employees': [emp.to_dict() for emp in pagination.items],
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page
        }), 200

    @staticmethod
    def get_employee(id):
        employee = EmployeeService.get_employee_by_id(id)
        return jsonify(employee.to_dict()), 200

    @staticmethod
    def update_employee(id, data):
        employee = EmployeeService.get_employee_by_id(id)
        
        if 'email' in data and data['email'] != employee.email:
            validation_errors = EmployeeSchema.validate_create({'email': data['email']})
            if validation_errors:
                return jsonify({'errors': validation_errors}), 400
            if EmployeeService.check_email_exists(data['email']):
                return jsonify({'error': 'Email already exists'}), 400

        updated_employee = EmployeeService.update_employee(employee, data)
        return jsonify(updated_employee.to_dict()), 200

    @staticmethod
    def delete_employee(id):
        employee = EmployeeService.get_employee_by_id(id)
        EmployeeService.delete_employee(employee)
        return '', 204