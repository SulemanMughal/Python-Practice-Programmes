import os
def Delete():
    path=input("Enter the path of file for deletion:")
    if os.path.exists(path):
        print('File Found')
        os.remove(path)
        print("File has been deleted")
    else:
        print("File Does not exist")