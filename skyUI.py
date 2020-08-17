from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from prototype import *



root = Tk()
root.geometry("350x420")
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

nameTitle = Label(root, text="Insert name here")
nameTitle.config(font=("Courier",8))
nameTitle.pack()

nameBox = Text(root,height=2,width=15)
nameBox.pack()

domTitle = Label(root, text="Domain name(without @)")
domTitle.config(font=("Courier",8))
domTitle.pack()

domBox = Text(root,height=2,width=15)
domBox.pack()

msgTitle = Label(root, text="Message id(optional)")
msgTitle.config(font=("Courier",8))
msgTitle.pack()

midBox = Text(root,height=2,width=15)
midBox.pack()

fTitle = Label(root, text="Filename for download(optional)")
fTitle.config(font=("Courier",8))
fTitle.pack()

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
    f = "Skylinks.txt"
    with open(f,"wt") as o_file:
            o_file.write(upload_f(filename))
            o_file.write("\n")
            o_file.close()



    
browsebutton = Button(root, text="Upload", command=browsefunc)
browsebutton.pack()


        

#prototype
pathlabel = Label(root)






