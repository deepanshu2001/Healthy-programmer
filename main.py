from pygame import mixer
import datetime
import time
import sys

now=datetime.datetime.now()
def Water():
    time.sleep(2400)#stores in seconds
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.set_volume(0.7)
    
    while True:
        mixer.music.play()
        print(" REMINDER to drink water !")
        drinkwater=input("Enter whether you have drank water :")
        if drinkwater=='No':
            mixer.music.pause()
            time.sleep(5)
            print("REMINDER to drink water")
            mixer.music.unpause()
        elif drinkwater=='Yes':
            mixer.music.stop()
            break
    
    if drinkwater=="Yes":
        with open("waterlog.txt","a") as f:
            f.write("drank water drank at--" +now.strftime(" %d/%m/%Y %H:%M:%S")+"\n")
    
    
def Eyes():
    time.sleep(2700)
    mixer.init()
    mixer.music.load("eyes.mp3")
    mixer.music.set_volume(0.7)
   
    while True:
        mixer.music.play()
        print("You need to excersise your eyes!")
        eyesrest=input("Did you take rest ?")
        if eyesrest=='No':
            mixer.music.pause()
            time.sleep(5)
            print("REMINDER to do eye excersice")
            mixer.music.play()
        elif eyesrest=='Yes':
            mixer.music.stop()
            break
    if eyesrest=='Yes':
        with open("eyeslog.txt","a") as f:
            f.write("Did excersice for eyes at--"+now.strftime("%d/%m%Y %H:%M:%S")+"\n")    

    
def Physical():
    time.sleep(3600)
    mixer.init()
    mixer.music.load("physical.mp3")
    mixer.music.set_volume(0.7)
    
    while True:
        mixer.music.play()
        print("You need to excersise now for your health!")
        physical_exci=input("did you excercise?")
        if physical_exci=='No':
            mixer.music.pause()
            time.sleep(5)
            print("REMINDER to excersice for your health")
            mixer.music.unpause()
        elif physical_exci=='Yes':
            mixer.music.stop()
            break
    if physical_exci=='Yes':
        with open("physicallog.txt","a") as f:
            f.write("Performed excersice at--"+now.strftime("%d%m%Y %H:%M:%S")+"\n")

NoofGlasses=int(input("How many glasses of water did you have ?"))   
while NoofGlasses!=20:
    Exit=input('Would you like to exit?')
    if Exit=='Yes':
        sys.exit()
    else:
        Water()
        Eyes()
        Physical()
        NoofGlasses=int(input("How many glasses did you drink?"))
        if NoofGlasses<20:
            with open("waterdrinkinglog.txt","w") as f:
                f.write(str(NoofGlasses))
    NoofGlasses+=1
    
