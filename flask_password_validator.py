def validate_password(self, password):
        import re
        message = 'Password should contain at least '
        error_log = []
        errors = {
            '1 digit': re.search(r'\d', password.data) is None,
            '1 uppercase letter': re.search(r'[A-Z]', password.data) is None,
            '1 lowercase letter': re.search(r'[a-z]', password.data) is None,
            '1 special character': re.search(r'\W', password.data) is None,
        }
        for err_msg, error in errors.items():
            if error:
                error_log.append(err_msg)
        if error_log:
            raise ValidationError(message + ', '.join(err for err in error_log))
