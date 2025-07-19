f=open("Xiaomi-Car-Logo.webp",'rb')
data=f.read()

copyfile=open('xiami.jpg','wb')
copyfile.write(data)

f.close()
copyfile.close()
