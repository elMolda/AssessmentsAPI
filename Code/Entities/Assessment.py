import uuid 
import json
class Assessment:
    def __init__(self, email, startTime, deadlineTime, endTime):
        self.email = email
        self.assessment_key = str(uuid.uuid4()) #Create unique key
        self.startTime = startTime
        self.deadlineTime = deadlineTime
        self.endTime = endTime
    
    def asstToJson(self):
        return({'Assessment Key': self.assessment_key,
                'User email': self.email,
                'Start Time': str(self.startTime),
                'End Time': str(self.endTime),
                'Deadline Time': str(self.deadlineTime)})
        