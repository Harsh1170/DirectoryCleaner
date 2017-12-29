import os
import threading
import shutil

root = input('Enter the root directory to process:')
print("reading files...")
files = [file for file in os.listdir(root) if os.path.isfile(os.path.join(root,file))]

dest = input("Enter the name of the destination folder:")
target = os.path.join(root,dest)
os.makedirs(target,exist_ok=True)
extlist = []

for file in files:
    filename,fileext = os.path.splitext(file)
    if fileext in extlist:
        try:
            shutil.copy(os.path.join(root,file),os.path.join(target,fileext[1:]))
            os.remove(os.path.join(root,file))
        except IOerror as e:
            print('Unable to copy file')
        except:
            print('unexpected error')
    elif fileext not in extlist:
        os.makedirs(os.path.join(target,fileext[1:]),exist_ok = True)
        try:
            shutil.copy(os.path.join(root,file),os.path.join(target,fileext[1:]))
            os.remove(os.path.join(root,file))
        except IOerror as e:
            print('Unable to copy file')
        except:
            print('unexpected error')
        extlist.append(fileext)

extlist = []
print("Done!")
