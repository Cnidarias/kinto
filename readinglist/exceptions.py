class InvalidUsage(Exception):
    status_code = 400
    description = "Bad Request"

    def __init__(self, message, status_code=None,
                 error_number=None, description=None):
        super(InvalidUsage, self).__init__()
        self.message = message
        self.error_number = error_number or 0
        if status_code is not None:
            self.status_code = status_code
        if description is not None:
            self.description = description

    def to_dict(self):
        return {
            "code": self.status_code,
            "errno": self.error_number,
            "error": self.description,
            "message": self.message
        }
