import os
from functions.create_secrect_key import secrectKey
import getpass
username = getpass.getuser()

Filepath = __file__
Filepath = Filepath.replace("main.py" ,"")
templates = Filepath+"templates/"

def setupVirtuvalEnv(app_directory):
    print("-"*20)
    print("creating Vitruval env")
    print("-"*20)
    cwd = os.getcwd()
    os.system("pip install virtualenv")
    os.system(f"virtualenv {app_directory}")
    # os.chdir(f"{app_directory}")
    # os.system(f"source bin/activate")
    # os.system('/bin/bash  --rcfile bin/activate')
    # os.chdir(f"{cwd}")

def createFolder(name):
    if not os.path.exists(name):
        os.makedirs(name)

def writeFile(path , data):
    with open(path , "w") as f:
        f.writelines(data)

def readFiles(path , read_file_template_replace = {} , json = False):
    with open(path) as f:
        datas = f.readlines()
    try:
        for key in read_file_template_replace.keys():
            for id ,data in enumerate(datas):
                if json:
                    datas[id]= data.replace("{{"+key+"}}", '"'+read_file_template_replace[key]+'"')
                else:
                    datas[id]= data.replace("{{"+key+"}}", read_file_template_replace[key])

    except Exception as e:
        print(e)
    return datas

def createFiles(level, filename, prefix, level_count, read_file_template_replace = {}):
    json = False
    if prefix.lower() == "json":
        json=True
    writeFile(f"{level}{filename}.{prefix}" , readFiles(f"{templates}level{level_count}/{filename.lower()}.txt" , read_file_template_replace, json) )

# level 1 create project directory

def createBasedonLevels(level = 0,files = [], folders = [], level_count=0):
    for file in files:
        createFiles(level, file[0] , file[1],level_count)

    for folder in folders:
        createFolder(f"{level}/{folder}")


def installBasicRequirments(path, pip="pip"):
    with open(path) as f:
        packages = f.readlines()
    
    for package in packages:
        os.system(f"{pip} install {package}")


level1 = input("Enter Project Name :").replace(" ","_")
description = input("Project Description (What your project will do):")
username_ = input(f"Enter Author name (press enter if you're {username}):")
if username_ is not None:
    username = username_



createFolder(level1)
setupVirtuvalEnv(level1)


"""Level 2 - Creates Dockerfile, app.py, migrate.py, app Folder"""

level2 = level1+"/"

files = [("app","py"),("Dockerfile","txt"),("migrate", "py") , ("requirements","txt")]
folders = ["app"]
createBasedonLevels( level = level2, files = files, folders= folders,level_count = 2)
createFiles( level2, "readme", "md" , 2 , {"APPNAME":level1 , "USERNAME":username , "DESCRIPTION":description})

folders = files = []



"""Level 3 - Creates files and folders in app folder
    __init__.py, errors.py, Models Directory, Configure directory, 
    Blueprints Directory, thirdparty Directory, gloabal directory

"""
level3 = level2+"app/"
files = [("__init__","py"), ("errors", "py")]
folders = ["Configure","Blueprints","Thirdparties", "Globals","Models"]
createBasedonLevels( level = level3, files =files, folders = folders, level_count = 3)
folders = files = []



"""Level 4 - Creating files and folders in Configure directory - config.py, app_config.json"""

level4 = level3+"Configure/"
files = [("config","py"),("__init__","py")]
createBasedonLevels(level = level4, files = files,level_count =  4)
folders = files = []

createFiles( level4, "app_config", "json" , 4 , {"SECRECTKEY":secrectKey(20)})


"""Level 5 - Creating files and folders in Models directory - users.py"""

level5 = level3+"Models/"
files = [("users","py"),("__init__","py")]
createBasedonLevels( level = level5, files = files,level_count = 5)
folders = files = []

"""Level 6 - Creating files and folders in Blueprints directory - users folder"""

level6 = level3+"/Blueprints/"
files = [("__init__","py")]
folders = ["users"]
createBasedonLevels( level = level6, folders= folders, level_count=6)
folders = files = []

"""Level 7 - Creating files and folders in users directory - routes.py"""
level7 = level6+"users/"
files = [("routes","py"),("__init__","py")]
folders = ["Classes"]
createBasedonLevels( level = level7, files = files, folders=folders,level_count = 7)
folders = files = []

"""Level 8 - Creating files and folders in users directory - routes.py"""
level8 = level7+"Classes/"
files = [("users","py"),("__init__","py")]

createBasedonLevels( level = level8, files = files,level_count = 8)
folders = files = []

"""Level 9 - Creating files and folders in Thirparties Folder"""

level9 = level3+"Thirdparties/"
files = [("__init__","py")]

createBasedonLevels( level = level9, files = files,level_count = 9)
folders = files = []

"""Level 10 - Creating files and folders in Globals Folder"""

level10 = level3+"Globals/"
files = [("__init__","py")]

createBasedonLevels( level = level9, files = files,level_count = 9)
folders = files = []

print("-"*20)
print("Files created successfully.")
print("Installing Basic requirments")

# os.system(f"/bin/bash  {os.getcwd()}/{level1}/bin/activate")

installBasicRequirments(Filepath+"templates/level2/requirements.txt" , "pip3")
# os.system("pip freeze requirements.txt")
# os.system(f"cd {level1}")

print("-"*40)
print("Switch to working directory\n\n\n")
print(f"cd {os.getcwd()}/{level1}")
print("copy the above code and run to change folder")

print("source bin/activate")
print("copy the above code and run for activate virtuval-env")
print("\n\n\n Happy coding")
print("\n\n\n Created with create-flask-app")
