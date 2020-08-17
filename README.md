# Skymask

Link to demo:
* Skylink: [Skymask on Skynet!](https://siasky.net/AABkmA-oiWNCpiZAcHIVPhPfYh2pJj5titWTK4BejXlwvw)
* Youtube: [Skymask](https://youtu.be/QeifhNZ95_U)

## Description

Skymask is an application you can use to generate a temporary email address and manage the content.
Moreover, it allows you to upload (or retrieve) any files or messages to a decentralized storage platform called Skynet ( powered by Sia ).
This is easily performed and the user is handed a link to use on the [skynet site](https://siasky.net).

Thus, the application aims at being a temporary mail client which uses decentralized storage for sending and receiving attachments.  

## Motivation & Utility

Considering today's information overload and lack of management, I found it extremely useful to be able to filter the noise.  
As such, an application like Skymask allows you to handle all the information in a clean way, while also avoiding spam.  

Not only this, but it is privacy preserving as well, since the email is temporary and is destroyed ( along with the content ) after a period of time.  
Add to this the use of Skynet as a storage means and it allows you to still keep anything you want in a safe and decentralized way.

Therefore, the main advantages of using it are:
* Privacy
* Filters online noise and spam
* Reduces information overload
* Decentralized storage using Skynet ensures a **safe** and *transparent* management of content.

Using Skynet for storage ensures a new decentralized future for mail clients, where attachments are replaced with skylinks.

## Further development

I seek to integrate a mail sending feature as well, with the added capability to GPG encrypt the messages.  
I am going to use Skynet for sending any attachments. Thus, the user only has to send the skylink associated with the file.

Also, using a Natural Language analysis API that tells the user a short description of the overall mail sentiment and present entities is also in my TODO list.  
Moreover, I aim at polishing the user interface for a smoother experience.

## Why Sia?

* Easy to integrate into your application. This is an empowering feature that allows developers to easily add decentralization and transparency into their apps using
a simple and easily manageable SDK.
* It is very user friendly, as the skylink is the only thing needed from the user to provide in order to view their content.

## Install and use

The application was written in Python, so make sure to install version 3.7+

1. Install syknet SDK: `pip install siaskynet`
2. Clone the repo on your machine
3. Run "skyUI.py" and enjoy :)

#### This application is made with <3 for the 'Own the Internet' hackathon on Gitcoin! -For Sia and Namebase
