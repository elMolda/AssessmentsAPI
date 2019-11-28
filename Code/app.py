from flask import Flask, jsonify, request, make_response
from Controllers import prepareAssessment
from Entities.Assessment import Assessment
from Utils import checkEmail
import sqlite3
app = Flask(__name__) 

@app.route('/ping', methods = ['GET'])
def ping():
    return jsonify({"message": 'Pong'})

@app.route('/test', methods = ['GET', 'POST'])
def manageTestEndpoint():
    response = None
    if request.method == 'GET': #Main endpoint of API
        response = jsonify({"Message": """This is Test endpoint.Send POST request to this with user parameters to start assessment."""})
    if request.method == 'POST': #Create a new User if needed. Create new Assemnt.
        if checkEmail.checkEmail(request.json['email']):
            asst = prepareAssessment.prepareAssessment(request)
            response = make_response(jsonify({"Assessment created":asst.asstToJson()}),201)
        else:
            response = make_response(jsonify({"Message":"Not valid Email"}),400)
    return response
if __name__ == '__main__': 
    app.run(debug=True, port=5000)