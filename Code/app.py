from flask import Flask, jsonify, request
from Controllers import prepareAssessment
import sqlite3
app = Flask(__name__) 

@app.route('/ping', methods = ['GET'])
def ping():
    return jsonify({"message": 'Pong'})

@app.route('/test', methods = ['GET', 'POST'])
def manageTestEndpoint():
    response = None
    if request.method == 'GET': #Main endpoint of API
        response = jsonify({"message": """This is Test endpoint.Send POST request to this with user parameters to start assessment."""})
    if request.method == 'POST': #Create a new User if needed. Create new Assemnt and Session.
        prepareAssessment.prepareAssessment(request)
        response = jsonify({"Users":"success"})
    return response
if __name__ == '__main__': 
    app.run(debug=True, port=5000)