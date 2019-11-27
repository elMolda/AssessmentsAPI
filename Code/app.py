from flask import Flask, jsonify, request

app = Flask(__name__) 

@app.route('/ping', methods = ['GET'])
def ping():
    return jsonify({"message": 'Pong'})

@app.route('/test', methods = ['GET'])
def manageTestEndpoint():
    if request.method == 'GET': #Main endpoint of API
        return jsonify({"message": """This is Test endpoint.Send POST request to this with user parameters to start assessment."""})

if __name__ == '__main__': 
    app.run(debug=True, port=5000)