# coding=utf-8
from flask import Flask
from flask import request
from flask import render_template

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
   return render_template("index.html",
		title = 'Factrix',
		description = 'Введите в строку любую фразу и мы найдём наиболее связанные с ней сведения.',
		descriptionshort = 'Любое слово или фраза',
		inputsubmit = 'Узнать',
		buttonText = 'Узнать',
		forExample = 'Например, ',
		footer = '<p>Создано в рамках <a href="http://vk.com/vladivostokhackathon">VL Hackathon II</a></p>'
		)

@app.route('/search', methods=['POST', 'GET'])
def search():
	query = (request.args['q'])

	relatedUrls = web_search_utils.getTopDuck2GoUrls(query)
	facts_urls = web_search_utils.printToFile(relatedUrls)

	run_tomita.tomita()
	result_json = post_facts_parser.parser('/srv/http/app/facts/', query, facts_urls)
	return result_json

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
