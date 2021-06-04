#import libraries
import speech_recognition as sr
import tkinter as tk
from tkinter import *
import os


#Initialized window
obj = tk.Tk()
obj.title("Speech Recognition")
obj.geometry('450x400')
obj.iconbitmap('voice.ico')
obj.resizable(False, False)
obj.config(bg = 'SlateBlue1')


#heading
Label(obj, text = 'Speech To Text' ,cursor="xterm", font='times 25 bold underline' , bg ='SlateBlue1').pack()
Label(obj, text ='Suyog Singh Rajput' ,cursor="xterm", font ='times 12 bold', bg = 'SlateBlue1').pack(side = BOTTOM)
Label(obj, text ='LN18BTCS1020' ,cursor="xterm", font ='times 10 bold', bg = 'SlateBlue1').pack(side = BOTTOM)


#text variable
msg = tk.Label(obj, bg ='white')

msg.place(x=20 , y=100)


#define function
def rec():
    r = sr.Recognizer()
    speech = sr.Microphone(device_index=0)

    # for recognizing speech
    while True:
        with speech as source: 
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
        try:
            txt = r.recognize_google(audio, language = 'en-US')
            msg.configure(text=txt)        
            print(txt)
        except Exception as ex:
            print(ex)
            break
def texttospeech():
    obj.destroy()
    import texttospeech as ts
    ts.texttospeech
def main():
    obj.destroy()
    import main
def Exit():
    obj.destroy()


#Button
Button(obj, text = "Start" ,cursor="hand2", font = 'times 16 bold', command = rec, bg = 'medium orchid').place(x=180, y=140)
Button(obj, text = 'Text To Speech',cursor="hand2", font='times 14 bold', command = texttospeech, bg = 'medium orchid',fg  = "white").place(x=37,y=190)
Button(obj, text = "Main Menu" ,cursor="hand2", font = 'times 14 bold', command = main, bg = 'medium orchid',fg  = "white").place(x=243, y=190)
Button(obj,text = 'EXIT',cursor="hand2",font = 'times 16 bold' ,relief=SUNKEN, command = Exit, bg = 'firebrick1',fg  = "yellow").place(x=180 , y =240)


#infinite loop to run program
obj.mainloop()
