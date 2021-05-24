import os
import shutil

audio = [".mp3", ".wma", ".aac"]
video = [".mp4", ".wmv", ".avi"]
docs = ["docx", ".doc", ".pdf"]
software = [".exe"]
zips = [".zip", ".rar", ".iso"]
others = []

def organizer(path):
    '''
    This function organize and structures files in folders.
    '''
    files = os.listdir(path)
    os.mkdir(path + "\\" + "Audio")
    os.mkdir(path + "\\" + "Video")
    os.mkdir(path + "\\" + "Documents")
    os.mkdir(path + "\\" + "Executables")
    os.mkdir(path + "\\" + "Compressed")
    os.mkdir(path + "\\" + "Unknown files")
    for file in files:
        extension = os.path.splitext(file)[1]
        #If there exist a folder in our path, then it will organize the files in it too
        # Folders have no extension
        if extension == "":
            files1 = os.listdir(path + "\\" + file)
            for file1 in files1:
                ext = os.path.splitext(file1)[1]
                newpath = path + "\\"+file+"\\"
                if ext in audio:
                    shutil.move(newpath + file1,path+"\\"+"audio")
                elif ext in video:
                    shutil.move(newpath + file1,path+"\\"+"video")
                elif ext in docs:
                    shutil.move(newpath + file1,path+"\\"+"documents")
                elif ext in software:
                    shutil.move(newpath + file1,path+"\\"+"executables")
                elif ext in zips:
                    shutil.move(newpath + file1,path+"\\"+"compressed")
                else:
                    shutil.move(newpath + file1,path+"\\"+"unknown files")
        elif extension in audio:
            shutil.move(path +"\\" + file,path+"\\"+"audio")
        elif extension in video:
            shutil.move(path +"\\" + file,path+"\\"+"video")
        elif extension in docs:
            shutil.move(path +"\\" + file,path+"\\"+"docs")
        elif extension in software:
            shutil.move(path +"\\" + file,path+"\\"+"executables")
        elif extension in zips:
            shutil.move(path +"\\" + file,path+"\\"+"compressed")
        else:
            shutil.move(path +"\\" + file,path+"\\"+"unknown files")
        print("Done...")
if __name__ == '__main__':
    #testing folder
    path = "D:\\Testing Folder"
    organizer(path)
    
                

                
                
