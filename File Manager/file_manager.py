import shutil
import os
import time
import subprocess
from file_read  import *
from file_write  import *
from file_add  import *
from file_delete  import *
from list_files  import *
from check_exist_file  import *
from move_file  import *
from copy_file  import *
from make_directory  import *
from remove_directory  import *
from open_file  import *


def main():
    run=1
    while(run==1):
        try:
            os.system('clear')
        except OSError:
            os.system('cls')
        print('\n>>>>>>>>>>Python 3 File Manager<<<<<<<<<<\n')
        print('The current time and date is:',time.asctime())
        print('\nChoose the option number: \n')
        dec=int(input('''
        1.Read a file
        2.Write to a file
        3.Append text to a file
        4.Delete a file
        5.List files in a directory
        6.Check file existence
        7.Move a file
        8.Copy a file
        9.Create a directory
        10.Delete a directory
        11.Open a program
        12.Exit
        '''))
        if dec==1:
            Read()
        if dec==2:
            Write()
        if dec==3:
            Add()
        if dec==4:
            Delete()
        if dec==5:
            Dirlist()
        if dec==6:
            Check()
        if dec==7:
            Move()
        if dec==8:
            Copy()
        if dec==9:
            Makedir()
        if dec==10:
            Removedir()
        if dec==11:
            Openfile()
        if dec==12:
            exit()
        run=int(input("1.Return to menu\n2.Exit \n"))
        if run==2:
            exit()


if __name__ == "__main__":
    main()