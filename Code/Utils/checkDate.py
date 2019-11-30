def checkDate(sentTime, startTime, deadlineTime):
    if startTime <= sentTime <= deadlineTime:
        return True
    return False