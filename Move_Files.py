import os
import shutil

from_dir = "C:/Users/vinay/Downloads"
to_dir = "C:/Users/vinay/Desktop/project112"
listOfFiles = os.listdir(from_dir)

#print(listOfFiles)

for fileName in listOfFiles:
    name,extension = os.path.splitext(fileName)
    #print(name)
    #print(extension)
    if extension =='':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1=from_dir+'/'+fileName
        path2=to_dir+'/'+"DocumentFiles"
        path3=to_dir+'/'+"DocumentFiles"+'/'+fileName
        #print("path1", path1)
        #print("path3", path3)

        if os.path.exists(path2):
            print("Moving"+fileName+"....")
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving"+fileName+"....")
            shutil.move(path1, path3)
