from zipfile import *
files = ZipFile("images.zip",'w',ZIP_DEFLATED)
files.write("/Users/maheshyadav/Documents/python/17_FILES PERATION/ZIPfie/compiler.png")
files.write("/Users/maheshyadav/Documents/python/17_FILES PERATION/ZIPfie/digital.jpg")
files.write("/Users/maheshyadav/Documents/python/17_FILES PERATION/ZIPfie/python1.jpg")
files.write("/Users/maheshyadav/Documents/python/17_FILES PERATION/ZIPfie/xiami1.jpg")
files.close()