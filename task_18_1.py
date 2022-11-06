import string
class EmailValidation:
    def __init__(self, email):
        self.email = email


    def is_valid_email_address(self):
        self.email = self.email.lower()
        parts = self.email.split('@')
        if len(parts) != 2:
            return False
        allowed = set(string.ascii_lowercase + string.digits + '.-_')
        for part in parts:
            if not set(part) <= allowed:
                return False
        return True

        # Valid
        # test@example.org
        # user123@subdomain.example.org
        # john.doe@email.example.org

        # Invalid
        # not valid@example.org
        # john.doe
        # john,doe@example.org
mail = EmailValidation('john.doe')
print(mail.is_valid_email_address())
