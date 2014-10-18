from flask import Flask
from flask import request
app = Flask(__name__)

import run_tomita

@app.route('/')
def hello_world():
    return 'Hello World!'
	
@app.route('/search', methods=['POST', 'GET'])
def search():
    error = None
    if request.method == 'POST':
        return "post" + request.form['q'];
    else:
        return "get" + request.args['q']

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')