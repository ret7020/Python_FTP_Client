#!/usr/bin/python3
"""
Tannishpage is the developer of this script. All rights go to Tannishpage

Purpose:
    A useless project. This project is a simple ftp client.
    opps i just realised Android has no default way to connect to FTP, so this script will be used as a ftp client on android in the android terminal. (SL4A or Scripting Layer for Android)

Basic Functions:
    *Upload Files
    *Download Files
    *List all files and folders on the server and in local directory
    *Change directory on server and local

Update Notes:
    -All basic functions have been completed (Date: 21 January 2017, Day: Saturday, Time: 17:19:20)
    -Logic Part is still in development. (Date: 21 January 2017, Day: Saturday, Time: 20:15:00)
    -Added 2 new commands help and clear. Self explaiatory. (Date: 22 January 2017, Day: Sunday, Time: 09:06:30)
    -Added 3 new commands send, download, zip. Send will send files, download will get files from FTP and zip will zip a folder and then send that to ftp. (Date: 22 January 2017, Day: Sunday, Time: 11:24:50)
    -Script Tested on Android. Works flawlessly only a few errors that will occur or any platform need fixing. (Date: 22 January 2017, Day: Sunday, Time: 11:50:50)
    ------Initial Released------- (Date: 22 January 2017, Day: Sunday, Time: 11:50:50) (Version 0.4)

    -Added authentication just incase someone tries to do something bad to my ftp. (Date: 23 January 2017, Day: Monday, Time: 09:41:40)
    -Now password is saved in a variable using getpass.getpass(). It is understoood that this is a security risk but if this is undone another security risk emerges. that is someone could send malicious files to an ftp on someother persons account.
        Eg: you login to your ftp and then you leave the computer to go and get a glass of wather. But then your friend uploads a malicious file on to the FTP on your name before you come back.
            If the authentication is in place then your firend cannot upload or download files from that ftp with out the password.
            But someone who gets access to the source code could make some samll changes to make it a security risk. But at this stage that is not as big of an issue.
    -Zipfolder function has been hot fixed. The issue was that an extra dot was added during opening the file in the send function. So the sending when the unzip option is selected is done speratly outside the send function.
    -Function delete() has been added. It will delete a file on the FTP when called. Function not tested (Date: 25 January 2017, Day: Wednesday, Time: 13:39:40)
    -Function delete() has been tested. It works perfectly fine. (Date: 25 January 2017, Day: Wednesday, Time: 16:19:40)
    -Function authenticate needs to be tested. (Date: 27 January 2017, Day: Friday, Time: 14:53:40)
    -Function authenticate has been tested and works fine. (Date: 27 January 2017, Day: Friday, Time: 18:05:50)
    -Function authenticate has been added to commands delete, download and send. (Date: 27 January 2017, Day: Friday, Time: 19:23:09)
    -Function Connect has been added, it takes over the connection process, it is used twice which seemed very inefficient. (It is not tested yet) (Date: 31 January 2017, Day: Tuesday, Time: 08:40:38)
    -Excepted crash when lcd/scd to a directory that does not exist. Needs testing. (Date: 1 Febuary 2017, Day: Wednesday, Time: 10:55:21)
    -Wrong ip connection has been excepted but needs testing (I did not realise that i did this was already in function connect). (Date: 1 Febuary 2017, Day: Wednesday, Time: 11:14:30)
    -Function connect has excepted incorrect/invalid ip addresses. It has been tested. And works. But when an incorrect ip is entered it halts and looks like it does not do anything
        at the moment the only way to get out is to ^C (CTRL + C). This will be fixed in the next update. (Date: 1 Febuary 2017, Day: Wednesday, Time: 17:46:08)
    -Crash with lcd/scd to an invalid directory has been tested and it works. (Date: 1 Febuary 2017, Day: Wednesday, Time: 17:46:08)
    ------Released Update------- (Date: 1 Febuary 2017, Day: Wednesday, Time: 17:46:08) (Version 0.5.5)

    -License command was created. But is called copyright. (Date: 4 Febuary 2017, Day: Saturday, Time: 22:01:20)
    -Copyright command is now in use. (Date: 7 Febuary 2017, Day: Tuesday, Time: 12:53:30)
    -Invalid ip halting is fixed. Issue was there was a return but nothing was being returned so it halted. (Date: 7 Febuary 2017, Day: Tuesday, Time: 12:53:30)
    -When no command is entered program crashes. It is now fixed. (Date: 7 Febuary 2017, Day: Tuesday, Time: 12:53:30)
    -Authentication failed because password was not a global variable. So now password and username are global variables They are declared like this: global username and global password.(Date: 7 Febuary 2017, Day: Tuesday, Time: 17:25:40)
    -Tested on windows program works. Connection is successful and everything is compatible. (Date: 9 Febuary 2017, Day: Thursday, Time: 10:52:37)
    -----Released Update------- (Date: 9 Febuary 2017, Day: Thursday, Time: 10:54:24)
    
    -All further development is now in windows for the time being. I reinstalled windows on the 9th feb and it corrupted grub, so i could not go into ubuntu so i took backup of all scripts and deleted ubuntu. Untill i reinstall ubuntu windows will be used to develop. (Date: 10 Febuary 2017, Day: Friday, Time: 07:09:58)
    -Now authentication is not asked if connection to ftp is not open. Previously authentication will be asked regardless of an open connection to ftp. (Date: 11 Febuary 2017, Day: Saturday, Time: 21:40:55)
    -Made a delete command for dirs. Yes file deletion and dir deletion is different. (Date: 11 Febuary 2017, Day: Saturday, Time: 21:40:55)
    -Made a command that makes folders on ftp. Now user will have more accessablity to to make changes to ftp. (Date: 11 Febuary 2017, Day: Saturday, Time: 21:40:55)
    -----Released Update--------- (Date: 11 Febuary 2017, Day: Saturday, Time: 21:50:45)
    
    -Zip folder function has been fixed, the issue was that 2 unknown variables were being used. Insted of foldername filename was being used and undeclared variable extention was used. (Date: 11 Febuary 2017, Day: Satuary, Time: 22:35:05)
    -The size command has been successfully implimented. It works fine. It gives a prediction so not to be 100% trusted. (Date: 12 Febuary 2017, Day: Sunday, Time: 12:20:50)
    -The send and download functions have been modified so that they show the time it took to transfer the file. They now also give a hint that the transfer started. (Date: 12 Febuary 2017, Day: Sunday, Time: 12:20:50)
    -----Released Final---------- (Date: 12 Febuary 2017, Day: Sunday, Time: 12:20:50)

    -Development is completed. Any updates after this are to fix unknown errors. Regular updates will stop from this point onwards. (Date: 12 Febuary 2017, Day: Sunday, Time: 12:20:50)
    -Excepted ^C input. (Date: 13 Febuary 2017, Day: Monday, Time: 07:11:44)
    -Size command had an issue, it was throwing the attribute error which crashed the program. Turns out it did not care even if user did not open a connection and just moved on. So ya. fixed! (Date: 13 Febuary 2017, Day: Monday, Time: 07:23:20) 


Development Progress:
    -Script In Development 0.1v (Date: 21 January 2017, Day: Saturday, Time: 20:15:00)
    -Script In Development 0.4v (Date: 22 January 2017, Day: Sunday, Time: 11:24:50)
    -Script In Development 0.4.5v (Date: 23 January 2017, Day: Monday, Time: 09:41:40)
    -Script In Development 0.5.5v (Date: 1 Febuary 2017, Day: Wednesday, Time: 17:46:08)
    -Script In Development 0.6.5v (Date: 9 Febuary 2017, Day: Thursday, Time: 19:57:34)
    -Script In Development 0.8v (Date: 11 Febuary 2017, Day: Saturday, Time: 21:40:55)
    -Script Fully Developed 1.0v (Date: 12 Febuary 2017, Day: Sunday, Time: 12:24:50)

Planned Additions or fixes: 
    *Organize all command outputs.
    *Add a size command for local files. Predict upload speeds. Time to upload the file.

All that need testing:

Plan (temporary):

"""

'''-------------------------------------------------------Libraries--------------------------------------------------'''

import os
from ftplib import FTP
import zipfile
import sys
import getpass
import datetime

'''-------------------------------------------------------Functions-------------------------------------------------------------------------'''

def zipfolder(foldername, target_dir):#This function is used to Zip a folder and then send it over to the ftp
    query1 = input("Would you like to unzip it on the server?(y/n): ")
    if query1 == 'y':
        zipobj = zipfile.ZipFile(foldername + 'Unzip.zip', 'w', zipfile.ZIP_DEFLATED)#I did not make this function for the record
        rootlen = len(target_dir) + 1
        for base, dirs, files in os.walk(target_dir):
            for file in files:
                fn = os.path.join(base, file)
                zipobj.write(fn, fn[rootlen:])
        file = open('%sUnzip.zip' % foldername , 'rb')#This is taken off the Send() function so that it does not cause an error. (Date: 23 January 2017, Day: Monday, Time: 15:20:03)
        ftp.storbinary('STOR %sUnzip.zip' % (foldername), file)
        file.close()
        print("Sent to ", ftp.pwd())
    else:
        zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)#I did not make this function for the record
        rootlen = len(target_dir) + 1
        for base, dirs, files in os.walk(target_dir):
            for file in files:
                fn = os.path.join(base, file)
                zipobj.write(fn, fn[rootlen:])
        send(foldername, "zip")


def send(filename, extention):#This function is used to send files or .zip files to the ftp.
    file = open('%s.%s' % (filename, extention) , 'rb')
    startime = datetime.datetime.now()
    ftp.storbinary('STOR %s.%s' % (filename, extention), file)
    endtime = datetime.datetime.now()
    time = (endtime-startime).total_seconds()
    file.close()
    print("Sent to ", ftp.pwd(), " In ", time)

def download(filename, extention):#This function is to retrieve or download a file from the ftp.
    file = open("%s.%s" % (filename, extention), "wb")
    startime = datetime.datetime.now()
    ftp.retrbinary("RETR %s.%s" % (filename, extention), file.write)
    endtime = datetime.datetime.now()
    time = (endtime-startime).total_seconds()
    file.close()
    print("Downloaded to ", os.getcwd(), " In ", time)

def sls():#sls stands for Server List, it is the ls command but for server side. It lists all directories and files on the server.
    serverList = ftp.nlst()
    print("\n".rstrip())
    for fileN in serverList:
        print(fileN)
    print("\n".rstrip())

def lls():#lls stands for Local List, it is the ls command but on local mechine.
    localList = os.listdir(os.getcwd())
    print("\n".rstrip())
    for fileN in localList:
        print(fileN)
    print("\n".rstrip())

def scd(path):#scd stands for Server Change Directory. cd command but for server.
    print("Old Server Working Directory: {}".format(ftp.pwd()))
    ftp.cwd(path)
    print("New Server Working Directory: {}".format(ftp.pwd()))

def lcd(path):#lcd stands for Local Change Directory. cd command but for local mechine.
    print("Old Local Working Directory: {}".format(os.getcwd()))
    os.chdir(path)
    print("New Local Working Directory: {}".format(os.getcwd()))

def delete(filename):
    try:
        ftp.delete(filename)
        print("{} has been deleted.".format(filename))
    except:
        print("Some error has been raised.")# Add the actual errors in the except.

def authenticate():# Makes things safer. Like sending or reciving files. and deleting.
    tries = 0
    while tries <= 3:
        authenticate = getpass.getpass("Password Authentication: ") 
        if password == authenticate:
            return True
            break
        tries = tries + 1
        print("Wrong Password")
    else:
        return False

def connect(ipAddress, port): # The connect code was being repeted twice, so i made a function.
    try:
        ftp.connect(ipAddress, port)
    except:#Add the acctual error
        print("Some error occured check to see if the ip is correct.")
        return False
    global username
    username = input("Username: ")
    global password
    password = getpass.getpass("Password: ")
    try:
        ftp.login(username, password)
        print("Login Passed")
    except:
        print("Login failed")

def make(filename):#This function makes a folder on the server.
    try:
        ftp.mkd(filename)
    except:
        print("Check connection to ftp.")
def rmdir(filename):#There is a delete function but this one only deletes folders the other one does not.
    try:
        ftp.rmd(filename)
    except:
        print("Some error occured. Check connection to ftp.")

def size(filename):#This function returns the name, size, speed of the connection, and the estimated download time of the file.
    startime = datetime.datetime.now()
    filesize = ftp.size(filename)
    endtime = datetime.datetime.now()
    stringsize = sys.getsizeof(filesize)
    transfspeed = stringsize / ((((endtime - startime)/2).total_seconds())/1000) 
    transfTime = filesize/transfspeed
    print("\nFile Name: {0}\nFile Size: {1} bytes\nAvg Transfer Speed: {2} bytes/seconds\nAvg time of transfer: {3} seconds".format(filename, filesize, transfspeed, transfTime))
'''---------------------------------------------------------------Logic-------------------------------------------------------------------'''
#os.system("cls" if os.name == "nt" else "clear") Don't initially clear screen. That is bad. Let user determine.
version = "1.0"
print("Welcom to FTP Made with python. Type help for command list. (Version %s)" % version)
help = ['Version 1.0v: ','copyright - prints developer info and version.','lls - command to get local directory list','connect <ip or url to ftp> - command to connect to ftp via port 21','sls - command to get server directory list','exit, bye - to quit','scd <path to directory> - to change directroy on server or vew current server directory','lcd <path to directory> - to change directory on local mechine or view the current working directory.', 'send <filename> - to send file.', 'size <file name> - Prints the detials of the specified file and tells the estimated time to download the file.', 'zip <filename> - to zip a folder and send it.', 'download, get, retrieve <filename> - Downloads a file from the server', 'delete, remove <filename> - Deletes a specified file on the ftp', 'clear - clear screen', 'make <foldername> - makes a folder on the ftp', 'rmdir <foldername> - deletes a folder on the ftp', 'help - to display this list', 'To contact me about any issues or giving feedbck: Email: tannishpage1@gmail.com']                 
ftp = FTP()
while True:
    try:
        command = input("ftp$ ")
    except KeyboardInterrupt:
        continue

    if command == "":
        continue
    else:
        pass
    command = command.split()
    command[0] = command[0].lower()
    if command[0] == "lls":
        lls()

    elif command[0] == "connect":
        try:
            connect(command[1], 21)
        except IndexError:
            connect(input("Enter ip: "), 21)
    elif command[0] == "sls":
        try:
            sls()
        except:
            print("Some error has occurred, try to re/connect to the ftp.")

    elif command[0] == "exit" or command[0] == "bye":#Program exits regardless of connection to ftp if command is typed.
        try:
            ftp.quit()
        except AttributeError:
            pass
        exit()

    elif command[0] == "copyright":
        print("\nFTP Client made by Aravind Venkata Punugu. (Other names: Tannishpage). All code belongs to Developer Aravind Venkata Punugu.\nIf redistributing please do so with crediting the original developer Aravind Venkata Punugu. Use at your own risk.\n")
        print("Version: %s" % version)

    elif command[0] == "scd":
        try:
            scd(command[1])
        except:
            try:
                print("Current server working directory: ",ftp.pwd())
                print("The directory was not found or no directory was given")
            except:
                print("Some error has occurred, try to re/connect to the ftp.")

    elif command[0] == "lcd":
        try:
            lcd(command[1])
        except:
            print("The directory was not found or no directory was given")
            print("Current local working directory: ", os.getcwd())

    elif command[0] == "clear":
        os.system("cls" if os.name == "nt" else "clear")

    elif command[0] == "help":
        print("\n".rstrip())
        for cm in help:
            print(cm)
        print("\n".rstrip())

    elif command[0] == "send":
        filex = command[1].replace(".", " ")
        filex = filex.split()
        try:
            ftp.voidcmd("NOOP")
        except:
            print("Connection to server is not open.")
            continue   
        authResult = authenticate()
        if authResult == True:
            try:
                print("Sending File...")
                send(filex[0], filex[1])
            except:
                print("Some error occured. Make sure that the file name is correct and that you are connected to the ftp.")
    elif command[0] == "zip":
        try:
            ftp.voidcmd("NOOP")
        except:
            print("Connection to server is not open.")
            continue   
        authResult = authenticate()
        if authResult == True:
            zipfolder(command[1], command[1])
                #print("Some error occured. Make sure the folder name is correct and that you are connected to the ftp.")

    elif command[0] == "retrieve" or command[0] == "get" or command[0] == "download":
        filex = command[1].replace(".", " ")
        filex = filex.split()
        try:
            ftp.voidcmd("NOOP")
        except:
            print("Connection to server is not open.")
            continue 
        authResult = authenticate()
        if authResult == True:
            try:
                print("Downloading File...")
                download(filex[0], filex[1])
            except:
                print("Some error occured. Make sure that the file name is correct and that you are connected to the ftp.")
        else:
            print("Authentication failed.")

    elif command[0] == "delete" or command[0] == "remove":
        try:
            ftp.voidcmd("NOOP")
        except:
            print("Connection to server is not open.")
            continue 
        authResult = authenticate()
        if authResult == True:
            try:
                delete(command[1])
            except IndexError:
                print("Specify a file to delete.")
        else:
            print("Authentication failed.")
    
    elif command[0] == "make":
        try:
            make(command[1])
        except IndexError:
            print("Specify a folder name.")
    
    elif command[0] == "rmdir":
        try:
            rmdir(command[1])
        except IndexError:
            print("Specify the folder to delete.")
    
    elif command[0] == "size":
        try:
            ftp.voidcmd("NOOP")
        except:
            print("Connection to server is not open.")
            continue
        try:
            size(command[1])
        except IndexError:
            print("Please specify a file.")

    else:
        print("{} command not found. Type help for command list.".format(command[0]))
