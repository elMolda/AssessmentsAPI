from DatabaseAccess import retrieveAsstDates
import datetime
def getAsstTimes(assessment_key):
    startTime, deadlineTime = retrieveAsstDates.retrieveAsstDates(assessment_key)#Get start and dealine time of assessment
    #Parse as date objects
    startTime = datetime.datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S.%f') 
    deadlineTime = datetime.datetime.strptime(deadlineTime, '%Y-%m-%d %H:%M:%S.%f')
    return startTime, deadlineTime
