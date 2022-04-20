import os
import re
import hashlib
from tkinter import filedialog


def get_Desktop():
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    return desktop
rootDir=str(filedialog.askdirectory(initialdir=get_Desktop(), title='Select a directory to hash')).strip()

SubDirs = os.listdir(rootDir)[1::]
ReGex = re.compile(r'[A-Za-z0-9]*.pdf|[A-Za-z0-9]*.jpg|[A-Za-z0-9]*.JPG|[A-Za-z0-9]*.png|[A-Za-z0-9]*.PNG|[A-Za-z0-9]*.docx')
filesNotProcessed = ''
filesCounter=0
filesWithAbslutePath = []
for root, dirs, files in os.walk(rootDir):
        for i in files:
            filesWithAbslutePath.append(os.path.join(root,i))
            filesNotProcessed+=os.path.join(rootDir,i)
            filesCounter+=1

filesProcessed = re.findall(ReGex,filesNotProcessed)
print(f"[+]========================== Files Discovered in {rootDir} ========================== [+]")
print(filesProcessed)
print(f"[+] Number of files: {filesCounter}")
print(f"[+]========================== Files Discovered in {rootDir} ========================== [+]")

hashingProcess =''
while hashingProcess != 'y' and hashingProcess != 'Y' and hashingProcess != 'n' and hashingProcess != 'N':
    hashingProcess = input("[+] start hasing ? (y/N): ")



if hashingProcess == 'y' or hashingProcess == 'Y':
    dict_hash = {}
    for i in range(len(filesProcessed)):
        dict_hash[filesProcessed[i]] = hashlib.md5(open(filesWithAbslutePath[i],'rb').read()).hexdigest()


        with open(f'{get_Desktop()}/(Hashes).txt','w+') as output:
            output.write(f"Files in {rootDir}\n\n")
            for k, v in dict_hash.items():
                output.write(k+" : "+v+"\n\n")
                print(k," : ", v)


    print(f'[+] Saved in {get_Desktop()}/(Hashes).txt\n\n\n')
    print("Goodbye :)")

else:
    print("Goodbye :)")


