import pyfiglet
import sys
import subprocess
import time
from termcolor import colored

welcome_banner=pyfiglet.figlet_format("Zip Cracker")
print(welcome_banner)

#   file=input("[+] Enter file to crack: ")
#   wordlist=input("[+] Enter wordlist: ")

file=sys.argv[1]

def crack(file,wordlist):
    try:
        wordlist=open(sys.argv[2], 'r')
        for password in wordlist:
            password=password.replace("\n","")
            cmd="unzip -P "+password+" "+file
            print("\n"+cmd)
            return_value=subprocess.call(cmd, shell=True)
            time.sleep(0.1)
            if return_value == 0:
                print("\n")
                print("*"*60)
                print(colored("Password found: "+password,'green'))
                print("*"*60)
                quit()
    except KeyboardInterrupt:
        print("\n\nPausing...\n")
        time.sleep(1)
        print("Program exited")
        quit()
    except subprocess.SubprocessError:
        print("Subprocess Error...")

try:
    crack(sys.argv[1],sys.argv[2])
except IndexError:
    print("Usage:\n\n$python pass-cracker.py file.zip wordlist.txt")
