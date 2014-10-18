# coding=utf-8
import os
import re
import codecs
import subprocess

def tomita():
	tomita_directory = (u'/srv/http/app/tomita/')
	texts_directory = (u'/srv/http/app/texts/') 
	facts_directory = (u'/srv/http/app/facts/') 
	tomita_config_path = (tomita_directory + u'config.proto')
	tomita_parser_path = (tomita_directory + u'tomitaparser')

	config_pattern = codecs.open(tomita_config_path, 'r', "utf-8").read()

	files = os.listdir(texts_directory) #dynamic tomita configuration
	for file in files:  
		config_file = codecs.open(tomita_config_path,'w', "utf-8")
		config_pattern = re.sub(u'Input = {File = ".*?"',u'Input = {File = "' + texts_directory + file + u'"',config_pattern) 
		config_pattern = re.sub(u'Output = {File = ".*?"',u'Output = {File = "' + facts_directory + file + u'"',config_pattern)
		config_file.write(config_pattern)
		config_file.close()
		
		result = subprocess.call([tomita_parser_path, tomita_config_path])

