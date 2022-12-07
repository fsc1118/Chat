# change directory to flasks and run python -m flask run
import os
def execute():
    os.chdir("main")
    os.system("python -m flask run")

if __name__ == "__main__":
    execute()