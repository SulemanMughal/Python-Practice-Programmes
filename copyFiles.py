# Copy files from a source directory to a destination directory.
import shutil; 
s1 = input("Enter source directory: ")
s2 = input("Enter destination directory: ")
shutil.copyfile(s1, s2)