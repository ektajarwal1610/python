import os
import pyttsx3
print("welcome to my toolkit")
pyttsx3.speak("how can i help you ,tell me ")
while True:
    pyttsx3.speak("tell me your requirement")
    print("enter your requirement ->>",end=' ')
    p=input()
    if (("run" in p)or("execute" in p)or("launch" in p)) and (("editor" in p    )or("notepad" in p)) : 
        pyttsx3.speak("notepad opening")
        os.system("vi")
    elif (("run" in p)or("execute" in p)or("open" in p)or("launch" in p))and    ("firefox"in p) :
        pyttsx3.speak("opening firefox")
        os.system("firefox")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in     p)) and (("google" in p) or ("chrome" in p)) :
        pyttsx3.speak("opening chrome")
        os.system("google-chrome-stable")
    elif (("run" in p) or("open" in p) or ("launch" in p) or ("install" in     p)) and (("vlc" in p) or ("media" in p) or ("player" in p)) :
        pyttsx3.speak("opening vlc and if not installed I will install it")
        os.system("vlc") and (os.system("sudo snap install vlc") or os.system        ("vlc"))
    elif ("calender" in p)or("cal" in p    ) :
        pyttsx3.speak("opening calender")
        os.system("cal")
    elif ("date" in p) :
        d=os.system("date")
    elif ("exit" in p) or ("close" in p) or ("quit" in p) :
        break
    else :
        print("sorry")
    print()



