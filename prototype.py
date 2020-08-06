import requests
from siaskynet import Skynet

# build quick GUI
# parse json results and offer clean output
# add skynet functionalities ( upload, download ) [X]

def check_mail(name,domain):
    mailbox = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+name+"&domain="+domain)
    mailbox_json = mailbox.json()
    return mailbox_json

def fetch_msg(name,domain,mid):
    msg = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login="+name+"&domain="+domain+"&id="+mid)
    msg_json = msg.json()
    return msg_json

def download_file(name,domain,mid,filen):
    attach = requests.get("https://www.1secmail.com/api/v1/?action=download&login="+name+"&domain="+domain+"&id="+mid+"&file="+filen)
    attach_json = attach.json()
    return attach_json


# allow easy upload via selection
# for any messages to be uploaded, save msg to file and upload file to skylink

#upload
skylink = Skynet.upload_file("path")
print(skylink)

#download
def sky_download(filen,skylink):
	try:
		Skynet.download_file(filen,skylink)
		print("Downloaded!")
	except:
		print("Skylink does not exist or could not be generated.")


