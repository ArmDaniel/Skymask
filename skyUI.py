from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from prototype import *



root = Tk()
root.geometry("350x350")
root.title(" Skymask Service ")

title = Label(root,text = "S K Y M A S K")
title.config(font=("Courier",15))
title.pack()

#######################################
#                                     #
#             TEMPMAIL                #  
#                                     #
#######################################

def alias_manager():
        messagebox.showinfo(title="Your current temporary mails",message=alias_manage())

manager = Button(root,text="Check current temporary mail addresses",command=alias_manager)
manager.pack()

def alias_gen():
        messagebox.showinfo(title="Your new temporary mail",message=generate_alias(6))


alias = Button(root,text="Generate Temporary Mail",command=alias_gen)
alias.pack()

# Handling input

def ret_in():
        ret_in.filen = filenBox.get("1.0","end-1c")

nameBox = Text(root,height=2,width=15)
nameBox.pack()

domBox = Text(root,height=2,width=15)
domBox.pack()

midBox = Text(root,height=2,width=15)
midBox.pack()

filenBox = Text(root,height=2,width=15)
filenBox.pack()

# Checking mail and retrieving functions

ret_in()

def mail_check():
        name = nameBox.get("1.0","end-1c")
        domain = domBox.get("1.0","end-1c")
        messagebox.showinfo(title = "Current Inbox", message=check_mail(name,domain))

inbox = Button(root,text="Check Inbox", command=mail_check)
inbox.pack()

def msg_fetch():
        name = nameBox.get("1.0","end-1c")
        domain = domBox.get("1.0","end-1c")
        mid = midBox.get("1.0","end-1c")
        messagebox.showinfo(title= "Message", message=fetch_msg(name,domain,mid))

crtMsg = Button(root,text="Retrieve specific message",command=msg_fetch)
crtMsg.pack()

def download_f():
        name = nameBox.get("1.0","end-1c")
        domain = domBox.get("1.0","end-1c")
        mid = midBox.get("1.0","end-1c")
        filen = filenBox.get("1.0","end-1c")
        messagebox.showinfo(title="Downloaded!", message=download_file(name,domain,mid,filen))

downloaded = Button(root,text="Download file",command=download_f)
downloaded.pack()
        


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






