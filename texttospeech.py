#import libraries
from tkinter import *
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os


#Initialized window
root = Tk()
root.geometry('450x400')
root.config(cursor="hand2")
root.config(bg = 'slate blue')
root.title('Speech Recognition')


##heading
Label(root, text = 'Text to Speech' , font='times 20 bold underline' , bg ='slate blue').pack()
Label(root, text ='Suyog Singh Rajput' , font ='times 12 bold', bg = 'slate blue').pack(side = BOTTOM)
Label(root, text ='LN18BTCS1020' , font ='times 10 bold', bg = 'slate blue').pack(side = BOTTOM)


#label
Label(root, text ='Enter Text-', font ='times 15 bold', bg ='slate blue').place(x=20,y=60)


#text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width ='60')
entry_field.place(x=20 , y=100)


#define function
def texttospeech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('speech.mp3')
    playsound('speech.mp3')

def Exit():
    root.destroy()
    os.remove('speech.mp3')

def Reset():
    Msg.set("")
    os.remove('speech.mp3')
    
def texttospeech():
    root.destroy()
    import texttospeech as ts
    ts.texttospeech
    
def main():
    root.destroy()
    import main
#Button
Button(root, text = "PLAY" , font = 'times 15 bold', command = texttospeech, bg = 'MediumOrchid1').place(x=25, y=150)
Button(root,text = 'EXIT',font = 'times 15 bold' ,relief=SUNKEN, command = Exit, bg = 'firebrick1',fg  = "yellow").place(x=190 , y =150)
Button(root, text = 'RESET', font='times 15 bold', command = Reset, bg = 'MediumOrchid1').place(x=102,y=150)
Button(root, text = "Text To Speech" , font = 'times 16 bold', command = texttospeech, bg = 'MediumOrchid1',fg  = "white").place(x=25, y=200)
Button(root,text = 'Main Menu',font = 'times 15 bold' , command = main, bg = 'MediumOrchid1',fg  = "white").place(x=190 , y =200)

#infinite loop to run program
root.mainloop()
