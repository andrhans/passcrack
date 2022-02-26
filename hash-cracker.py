import pyfiglet
import sys
import hashlib

welcome_banner=pyfiglet.figlet_format("Hash cracker")
print(welcome_banner)

hash=input("Hash of victim: ")

try:
    file=open(sys.argv[1], "r")
except:
    print("Password file missing")

for password in file:
    password=password.replace("\n","")
    enc=password.encode("utf-8")
    digest=hashlib.md5(enc.strip()).hexdigest()
    if hash==digest:
        print("\n"+"*"*50)
        print("Password found\n\n"+password+"::"+digest)
        print("*"*50)
        break
    