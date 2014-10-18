# coding=utf-8
from flask import Flask
from flask import request
app = Flask(__name__)

import codecs
import run_tomita
import web_search_utils
import post_facts_parser

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

@app.route('/')
def hello_world():
    return 'Hello World! :3'
	
@app.route('/search', methods=['POST', 'GET'])
def search():	
	query = (request.args['q']).encode('utf-8')

	relatedUrls = web_search_utils.getTopDuck2GoUrls(query)	
	facts_urls = web_search_utils.printToFile(relatedUrls)

	run_tomita.tomita()
	result_json = post_facts_parser.parser('/srv/http/app/facts/', query, facts_urls)
	return result_json

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')