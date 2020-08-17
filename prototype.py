import requests
from siaskynet import Skynet
import random
import string
import json


##########################################
#			                 #
#            TEMPORARY EMAIL             #
#                                        #
##########################################

alias_list = []


def generate_alias(length):
    letters = string.ascii_lowercase
    alias_domain = ["1secmail.org","1secmail.com"]
    alias_name = ''.join(random.choice(letters) for i in range(length))
    alias = alias_name + '@' + random.choice(alias_domain)
    
    new = alias.split('@')
    alias_tuple = (new[0],new[1])
    alias_list.append(alias_tuple)
    
    return alias

def alias_manage():
    return alias_list

def check_mail(name,domain):
    mailbox = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login="+name+"&domain="+domain)
    mailbox_json = mailbox.json()
    return mailbox_json

def fetch_msg(name,domain,mid):
    msg = requests.get("https://www.1secmail.com/api/v1/?action=readMessage&login="+name+"&domain="+domain+"&id="+mid)
    msg_json = msg.json()
    return msg_json

def download_file(name,domain,mid,filen):
    try:
        attach = requests.get("https://www.1secmail.com/api/v1/?action=download&login="+name+"&domain="+domain+"&id="+mid+"&file="+filen)

        f = filen
        with open(f, 'wb') as o_file:
            o_file.write(attach.content)
        return "Downloaded file!"
    except:
        return "No such file or server is down :("
    

##########################################
#                                        #
#        SYKNET FUNCTIONALITIES          #  
#                                        #
##########################################

def upload_f(path):
	skylink = Skynet.upload_file(path)
	return skylink

def sky_download(filen,skylink):
	
	try:
		Skynet.download_file(filen,upload_f.skylink)
		print("Downloaded!")
	except:
		print("Skylink does not exist or could not be generated.")


