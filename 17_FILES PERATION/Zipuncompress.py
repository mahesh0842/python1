from zipfile import *
f= ZipFile('images.zip','r')
f.extractall()
f.close()