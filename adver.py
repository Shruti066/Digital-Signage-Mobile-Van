import tkinter
from tkinter import *
from tkinter import messagebox
import urllib.request
import base64
import time
from threading import Thread
from PIL import Image, ImageTk
import os
import socket
import webbrowser

flag = 1
tkWindow = Tk()
tkWindow.geometry('480x250')
tkWindow.title('Ads Broadcast')

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(hostname)

path = "image.jpg"
image_squre_size = 180

def getResponseCode(url):
    conn = urllib.request.urlopen(url)
    return conn.read()

def dothis():
    t1 = Thread(target=showMsg)
    t1.start()
   
def showMsg():
    global flag
    while(1):
        a = getResponseCode("http://localhost/viewDetails.php")
        s = str(a)
        r = s.split("@@")
        info = r[0]
        link = r[1]
        imge = r[2]
        if(imge != "NULL'"):
            flag = 1
            os.system("pkill chromium")    
            content = imge.replace("\\n","")
            content += "=" * ((4 - len(content) % 4) % 4)
            decoded_data=base64.b64decode((content))
            with open(path, 'wb') as f:
                f.write(decoded_data)
            image1 = Image.open(path)
            new_image = image1.resize((image_squre_size, image_squre_size))
            test = ImageTk.PhotoImage(new_image)           
            label1["image"] = test
            time.sleep(4)
        
        elif(info != "b'NULL"):
            flag = 1
            os.system("pkill chromium")
            infotext = (info.split("b")[1]).replace("'","")
            lbl["text"] = infotext
            time.sleep(4)
            lbl["text"] = "."
            time.sleep(0.5)
            lbl["text"] = ".."
            time.sleep(0.5)
            lbl["text"] = "..."          
        else:
            if(flag != 0):
                flag = 0
                os.system("pkill chromium")
                infotext = link
                lbl["text"] = "Opening Link In Browser."
                time.sleep(0.5)
                lbl["text"] = "."
                time.sleep(0.5)
                lbl["text"] = ".."
                time.sleep(0.5)
                lbl["text"] = "..."
                webbrowser.open_new(infotext)
            
lbl=Label(tkWindow, text="", fg='red', font=("Helvetica", 16))
lbl.place(x=150, y=70)
lbl.pack()


test = ""
label1 = tkinter.Label(image=test,height = image_squre_size,width=image_squre_size)
label1.image = test
label1.place(x=150, y=50)
label1.pack()

dothis()
tkWindow.mainloop()

