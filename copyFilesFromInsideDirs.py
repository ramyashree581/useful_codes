for i in os.listdir():
    for j in os.listdir(i):
        shutil.copy(path+"\\"+i+"\\"+j, destination)
path = "dir_name"
