from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.controllers.employee_controller import EmployeeController
from flasgger import swag_from

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/api/employees/', methods=['POST'])
@jwt_required()
@swag_from('docs/create_employee.yml')
def create_employee():
    return EmployeeController.create_employee(request.get_json())


@employee_bp.route('/api/employees/', methods=['GET'])
@jwt_required()
@swag_from('docs/list_employee.yml')
def list_employees():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    department = request.args.get('department')
    role = request.args.get('role')
    return EmployeeController.list_employees(page, per_page, department, role)


@employee_bp.route('/api/employees/<int:id>/', methods=['GET'])
@jwt_required()
@swag_from('docs/get_employee.yml')
def get_employee(id):
    return EmployeeController.get_employee(id)


@employee_bp.route('/api/employees/<int:id>/', methods=['PUT'])
@jwt_required()
@swag_from('docs/update_employee.yml')
def update_employee(id):
    return EmployeeController.update_employee(id, request.get_json())


@employee_bp.route('/api/employees/<int:id>/', methods=['DELETE'])
@jwt_required()
@swag_from('docs/delete_employee.yml')
def delete_employee(id):
    return EmployeeController.delete_employee(id)