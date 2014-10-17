import os
import subprocess

tomita_directory = ("/srv/http/app/tomita/")
#texts_directory = ('..\\texts\\') #for dynamic tomita configuration 

#files = os.listdir(texts_directory)
#for file in files: #for dynamic tomita configuration 

result = subprocess.call([tomita_directory + 'tomita-linux32', tomita_directory +'config.proto'])
