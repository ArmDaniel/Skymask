import requests
from siaskynet import Skynet
import random
import string

##########################################
#										 #
#            TEMPORARY EMAIL             #
#                                        #
##########################################

def generate_alias(length):
    letters = string.ascii_lowercase
	alias_domain = ["@1secmail.org","@1secmail.com"]
    alias_name = ''.join(random.choice(letters) for i in range(length))
	alias = alias_name + random.choice(alias_domain)
    return alias

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

##########################################
#                                        #
#        SYKNET FUNCTIONALITIES          #  
#                                        #
##########################################

def upload_f(path):
	skylink = Skynet.upload_file(path)
	return skylink

def sky_download(filen,skylink):
	skylink = upload_f(filen)
	try:
		Skynet.download_file(filen,skylink)
		print("Downloaded!")
	except:
		print("Skylink does not exist or could not be generated.")


