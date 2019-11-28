from flask import Flask, jsonify, request, make_response #Flask modules used
from Controllers import prepareAssessment, showQuestion #Files from Controllers package
from Entities.Assessment import Assessment #Files from Entities package
from Utils import checkEmail #Files from Utils package

app = Flask(__name__) #Declare server

@app.route('/ping', methods = ['GET']) #Testing Route, for Server testing.
def ping():
    return jsonify({"message": 'Pong'})

@app.route('/test', methods = ['GET', 'POST']) #Test route. Get only for info. Post register and create asssesment
def manageTestEndpoint(): #Define response according to request method type.
    response = None #Empty response
    if request.method == 'GET': #Info about endpoint
        response = jsonify({"Message": "This is Test endpoint.Send POST request to this with user parameters to start assessment."})
    if request.method == 'POST': #Create a new User if needed. Create new Assemnt.
        if checkEmail.checkEmail(request.json['email']): #Check valid email
            asst = prepareAssessment.prepareAssessment(request) #Create a new User if needed. Create new Assemnt.
            response = make_response(jsonify({"Assessment created":asst.asstToJson()}),201) #Retrieve Assemnt data. Inform correctly created
        else:
            response = make_response(jsonify({"Message":"Not valid Email"}),400) #Not valid email. Inform bad request
    return response #Return request.

@app.route('/test/<string:assessment_key>/questions/<int:question_n>', methods=['GET']) #Get all the questions for current assessment
def getAsstQuestion(assessment_key,question_n):
    response = None
    if request.method == 'GET':
        question = showQuestion.showQuestion(assessment_key,question_n)
        if question != None:
            response = make_response(jsonify({"Question":question.qstnToJson()}),200)
        else:
            response = make_response(jsonify({"Message":"No Assessment found"}),404)
    return response

if __name__ == '__main__': 
    app.run(debug=True, port=5000)