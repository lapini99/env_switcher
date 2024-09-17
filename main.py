import subprocess
import projects
import os

def chooseProject():
    print("Choose a project to switch on: ")
    
    projecstMap = projects.projects
    
    for project in projecstMap.keys():
        print(f"- {project}")

    selectedProject = input("Enter project name: ")
    
    if selectedProject not in projecstMap.keys():
        print(f"Project doesn't exist!")
        return
    elif selectedProject != "z":
        print(f"Arrancando -{selectedProject} ...")
        try:
            subprocess.Popen(["make", "all_remove"], cwd = projecstMap["z"])
            subprocess.Popen(["make", "start"], cwd = os.path.expanduser("~/development/x/"))
            subprocess.Popen(["make", "start"], cwd = projecstMap[selectedProject])

        except Exception as e:
            print(f"{e}")
    else:
        try:
            print(f"Arrancando -{selectedProject}")
            subprocess.Popen(["make", "stop"], cwd = os.path.expanduser("~/development/x/"))
            subprocess.Popen(["make", "all"], cwd = projecstMap["z"])
        except Exception as e:
            print(f"{e}")   
    
chooseProject()