
import os


def get_filez ():
    direct = os.getcwd()
    for file in os.listdir(direct):
        time = os.path.getmtime(file)
        abPath=os.path.join(direct,file)
        if file.endswith(".txt"):
            print (abPath,time)
        








if __name__ == "__main__":
    get_filez()


