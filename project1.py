import pyttsx3
import os
pyttsx3.speak("Hello user. How can I help you? plz write what you want to do")
while True:
   print("pls write what you want to do:", end=' ')
   x=input()
   if("dont" in x)or ("not" in x):
       continue
   elif(("run" in x) or ("open" in x) or ("launch" in x))and(("browser"in x)or ("chrome" in x)): 
       os.system("chrome")
   elif (("run" in x) or ("open" in x) or ("launch" in x) or ("use" in x))and(("editor"in x)or("notepad" in x)):
       os.system("notepad")
   elif ("fuck off" in x) or ("bye" in x) or ("stop" in x) or ("quit" in x):
       pyttsx3.speak("It was plasure helping you. See you soon!!")
       break
   elif (("run" in x) or ("open" in x) or ("launch" in x))and(("media"in x)or ("player" in x) ):
       os.system("wmplayer")
   elif (("capture") or ("take")) and (("screen" in x) or ("screenshot" in x)):
       os.system("quickshot")
   elif (("capture") or ("take") or (record)) and (("screen" in x) or ("something" in x)):
       os.system("recorder")
   elif ("aws" in x) or ("cloud" in x) or ("instance" in x):
       os.system("chrome https://aws.amazon.com/console/")
   elif ("check" in x) or ("send" in x) or ("email" in x):
       os.system("chrome mail.google.com")
   elif  ("python" in x):
       os.system("jupyter notebook")
   elif  ("java" in x):
       os.system("eclipse")
   elif (("virtual") in x):
       os.system("vmware")
   
   elif("profile" in x):
       os.system("chrome https://www.linkedin.com/in/aditi-sinha-b063171a8/")
   elif("calculate" in x) or ("calculations" in x):
       os.system("calc")
   elif("hardware" in x) and ("information" in x):
       os.system("msinfo32")
   else:
       pyttsx3.speak("Sorry! I didnt recognize. plz try again!")
   
   
    
    
    
       
   
