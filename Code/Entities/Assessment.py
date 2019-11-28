import uuid 
import json
class Assessment:
    def __init__(self, email, startTime, deadlineTime):
        self.email = email
        self.assessment_key = str(uuid.uuid4())
        self.startTime = startTime
        self.deadlineTime = deadlineTime
    
    def asstToJson(self):
        return({'Assessment Key': self.assessment_key,
                'User email': self.email,
                'Start Time': str(self.startTime),
                'Deadline Time': str(self.deadlineTime)})
        