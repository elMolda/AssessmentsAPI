import uuid 
class Assessment:
    def __init__(self, email):
        self.email = email
        self.assessment_key = str(uuid.uuid4())