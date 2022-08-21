def Write():
    path=input("Enter the path of file to write or create:")
    if os.path.isfile(path):
        print("Rebuilding the existing file")
    else:
        print("Creating the new file")
    text=input("Enter text:")
    file=open(path,"w")
    file.write(text)
