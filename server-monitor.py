### AUTHOR: https://github.com/Seelachsfilet
### AUTHOR-MAIL: seelachsfilet.all@web.de
### VERSION: 1.0
### LANGUAGE: [DE][EN]
### If you record a video with this file, I want me to be involved, that means that you have to add my name!
### Republication is prohibited!
###
import os


print("Es wird bis jetzt nur auf 3 Protokollen einen server-monitor geben: ftp, ssh, http, https")
variable_de = input("Bitte gebe das Script an: \n")
language = input("Bitte Geb deine sprache in DE oder EN an \n")
ip = input("Geb die IP des clients an den du monitoren willst: \n")
if os.system("ping -c 1 " + ip) == 0:
    print ("IP ist erreichbar")
else:
    print ("IP ist NICHT erreichbar")



if(language == "DE" or "de"):
    print(f"Das programm wurde auf |{language}| gestellt")


    if(variable_de == "http"):
        print(f"Du hast das Protokoll: |{variable_de}| gewählt")
        print(f"Es wird nun probiert ob das Endgerät Pings animmt!")


    if(variable_de == "ssh" or "SSH"):
        print(f"Du hast das Protokoll: |{variable_de}| gewählt")
        print(f"Es wird nun probiert ob das Endgerät Pings animmt!")
        os = input("Bitte gebe deinen Betriebssystemnamen ein: ")
        if(os == "windows" or "Windows"):
            print(f"Dein Betriebssystem ist : {os}")
            print("Windoiw")


    if(variable_de == "ftp"):
        print(f"Du hast das Protokoll: |{variable_de}| gewählt")
        print(f"Es wird nun probiert ob das Endgerät Pings animmt!")

