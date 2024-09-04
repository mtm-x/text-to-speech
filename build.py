import sys
import subprocess
import time 

#install pyinstaller
def install() :
   try :
        subprocess.check_call([sys.executable, "-m", "pip", "install",'pyinstaller']) 
        subprocess.check_call([sys.executable, "-m", "pip", "install",'customtkinter']) 
   except : 
       print("error installing packages")
#create bin or exe
def command():
    subprocess.check_call(['pyinstaller','--onefile','t2s.py']) 
    print("making executables....!!!")
    
if (sys.platform == "linux" or sys.platform == "win32" ) :
    try :
        install()
        print("Installing pyinstaller........!!!!")
        time.sleep(2)
        command()
        
    except:
        print("Error!!!!")