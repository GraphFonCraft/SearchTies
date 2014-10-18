# coding=utf-8
from flask import Flask
from flask import request
app = Flask(__name__)

import codecs
import run_tomita
import web_search_utils
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

@app.route('/')
def hello_world():
    return 'Hello World!'
	
@app.route('/search', methods=['POST', 'GET'])
def search():	
	arg = request.args['q']

	relatedUrls = web_search_utils.getTopDuck2GoUrls(arg.encode('utf-8'))	
	a_text =  web_search_utils.getArticleText(relatedUrls[0])
	
	web_search_utils.printToFile(relatedUrls)
	
	
	return "ok"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')