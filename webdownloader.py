### AUTHOR: https://github.com/Seelachsfilet
### AUTHOR-MAIL: seelachsfilet.all@web.de
### VERSION: 1.0
### LANGUAGE: [DE][EN]
### If you record a video with this file, I want me to be involved, that means that you have to add my name!
### Republication is prohibited!
###
import os
import pytube

###START OF SCRIPT

uname = input("Username: ")#SET A VARABLE TO USERNAME

###VARIABLEN
path = ''.join(('C:/Users/', os.getlogin(), '/Downloads/'))#PATH TO VIDEO DOWNLOAD LOCATION
###


print("This is an version for [DE] and [EN]")#HELPER
print("Give URL:")#URL VARIABLE
url = input()#URL VARIABLE
print("Wird Heruntergeladen[DE], Downloading[EN]")#
pytube.YouTube(url).streams.get_highest_resolution().download((f"C:/Users/{uname}/Downloads/"))#DOWNLOADING PROCESS
print (f"Das Video wurde in {path} abgelegt![DE], The video is in {path}!")#PATH TO DOWNLOAD LOCATION

###END OF SCRIPT
