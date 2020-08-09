from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from prototype import *


root = Tk()

#######################################
#                                     #
#             TEMPMAIL                #  
#                                     #
#######################################

# get user input when calling func


def mail_check():
	messagebox.showinfo(title = "Current Inbox", message=check_mail("name","@1secmail.org"))

inbox = Button(root,text="Check Inbox", command=mail_check)
inbox.pack()

def msg_fetch():
        messagebox.showinfo(title= "Message", message=fetch_msg("example","domain","mid"))

crtMsg = Button(root,text="Retrieve specific message",command=msg_fetch())
crtMsg.pack()



########################################
#                                      #
#          Skynet Specifics            #
#                                      #
########################################

def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)
    messagebox.showinfo(title="Skylink", message = "Your Skylink: " + upload_f(filename))
     

browsebutton = Button(root, text="Upload", command=browsefunc)
browsebutton.pack()

#prototype
pathlabel = Label(root)


