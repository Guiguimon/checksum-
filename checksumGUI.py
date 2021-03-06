from tkinter import *
from tkinter import filedialog
import tkinter as tk
import sys
import hashlib


#fonction lecture et comparaison hash SHA256/MD5
def hashfile(file):

    buffersize = 65536
    
    if var.get() == 'SHA256':
        sha256 = hashlib.sha256()

        with open(file, 'rb') as f:

            while True:

                data = f.read(buffersize)

                if not data:
                    break
            
                sha256.update(data)

        return sha256.hexdigest()
    
    else:
        md5 = hashlib.md5()
        with open(file, 'rb') as f:

            while True:

                data = f.read(buffersize)

                if not data:
                    break
            
                md5.update(data)

        return md5.hexdigest()



# fonction relative bouton selection de fichier
def btnFileClk():
    root.filename = filedialog.askopenfilename(
        initialdir="/", title="Select A File")
    hashfileinput.delete(0, END)
    hashfileinput.insert(0, root.filename)
    

# fonction relative verification checksum
def checkClk():
    hashkey = hashinput.get()
    fileHash = hashfile(hashfileinput.get())

    if hashkey == fileHash:
        resultlabel.configure(text="Checksum match !", fg="green")
    else:
        resultlabel.configure(text="Checksum do not match !", fg="red")



root = tk.Tk()
root.title('Checksum analyze')

var = tk.StringVar()
var.set('MD5')

hashlabel = Label(root, text="Checksum to compare :")
hashlabel.grid(row = 0)
hashinput = Entry(root, width=60)
hashinput.grid(row = 0, column = 1)

hashfilelabel = Label(root, text="File to check :")
hashfilelabel.grid(row = 1)
hashfileinput = Entry(root, width=60)
hashfileinput.grid(row = 1, column = 1)
button = Button(root, text = "Select file", command = btnFileClk )
button.grid(row = 1, column = 2, padx = 5)

radMD5 = Radiobutton(root, text="MD5 Checksum", variable = var, value = 'MD5')
radMD5.grid(row = 2)

radSHA256 = Radiobutton(root, text="SHA256 Checksum", variable = var, value = 'SHA256')
radSHA256.grid(row = 2, column = 1)

button2 = Button(root, text = "Verify", command = checkClk )
button2.grid(row = 4, pady = 5)

resultlabel = Label(root, text='')
resultlabel.grid (row = 4, column = 1)


root.mainloop()
