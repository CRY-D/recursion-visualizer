import flask 
from flask import request

app = flask.Flask(__name__) 

app.config["DEBUG"] = True

# for each flask request, we need: 
# - data in the body to represent function logic
# - data in the parameters to represent function name and function call
# if either is missing, we send back an error message. If the remote 
# code execution raises an error, we send back that error message as well. 

@app.route('/execute', methods=['GET', 'POST'])
def execute(): 
    if 'funcName' in request.args and 'funcCall' in request.args: 
        funcName = request.args['funcName'] 
        funcCall = request.args['funcCall']
        return "<h1>Congrats! You entered " + funcName + " as function name and " + funcCall + " as your function call. </h1>"
    else: 
        return "<h1> Please specify both the function name and the initial function call. </h1>"

if __name__ == "__main__": 
    app.run()