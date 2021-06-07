#import libraries
from tkinter import *
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os


#Initialized window
root = Tk()
root.geometry('450x400')
root.iconbitmap('voice.ico')
root.config(bg = 'SlateBlue1')
root.title('Speech Recognition')


#heading
Label(root, text = 'Main Menu' ,cursor="xterm", font='times 25 bold underline' , bg ='SlateBlue1').pack()
Label(root, text ='Suyog Singh Rajput' ,cursor="xterm", font ='times 12 bold', bg = 'SlateBlue1').pack(side = BOTTOM)
Label(root, text ='LN18BTCS1020' ,cursor="xterm", font ='times 10 bold', bg = 'SlateBlue1').pack(side = BOTTOM)


#label
Label(root, text ='!!Choose!!',cursor="xterm", font ='times 20 bold underline', bg ='SlateBlue1',fg  = "blue").pack(pady=20)


#define function
def texttospeech():
    root.destroy()
    import texttospeech as ts
    ts.texttospeech

def Exit():
    root.destroy()

def speechtotext():
    root.destroy()
    import speechtotext as st
    st.rec


#Button
Button(root, text = "Text To Speech" , font = 'times 16 bold', cursor="hand2", command = texttospeech, bg = 'medium orchid',fg  = "white").pack(pady=10)
Button(root, text = 'Speech To Text', cursor="hand2", font='times 16 bold', command = speechtotext, bg = 'medium orchid',fg  = "white").pack(pady=10)
Button(root,text = 'EXIT', cursor="hand2", font = 'times 16 bold' ,relief=SUNKEN, command = Exit, bg = 'firebrick1',fg  = "yellow").pack(pady=10)


#infinite loop to run program
root.mainloop()
