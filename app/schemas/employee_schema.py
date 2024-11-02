from email_validator import validate_email, EmailNotValidError

class EmployeeSchema:
    @staticmethod
    def validate_create(data):
        errors = {}
        
        if not data.get('name'):
            errors['name'] = 'Name is required'
            
        try:
            if data.get('email'):
                validate_email(data.get('email'))
        except EmailNotValidError:
            errors['email'] = 'Invalid email format'
            
        return errors