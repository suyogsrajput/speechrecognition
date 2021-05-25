## import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr


################### Initialized window####################

root = Tk()
root.geometry('450x400')
root.resizable(0,0)
root.config(bg = 'slate blue')
root.title('Speech Recognization')


##heading
Label(root, text = 'Text to Speech' , font='times 20 bold' , bg ='slate blue').pack()
Label(root, text ='Suyog Singh Rajput' , font ='times 12 bold', bg = 'slate blue').pack(side = BOTTOM)
Label(root, text ='LN18BTCS1020' , font ='times 10 bold', bg = 'slate blue').pack(side = BOTTOM)




#label
Label(root, text ='Enter Text', font ='times 15 bold', bg ='slate blue').place(x=20,y=60)


##text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width ='60')
entry_field.place(x=20 , y=100)


###################define function##############################
def texttospeech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('speech.mp3')
    playsound('speech.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button
Button(root, text = "PLAY" , font = 'times 15 bold', command = texttospeech, bg = 'MediumOrchid1').place(x=25, y=150)
Button(root,text = 'EXIT',font = 'times 15 bold' , command = Exit, bg = 'firebrick1').place(x=190 , y =150)
Button(root, text = 'RESET', font='times 15 bold', command = Reset, bg = 'MediumOrchid1').place(x=102,y=150)


#infinite loop to run program
root.mainloop()
