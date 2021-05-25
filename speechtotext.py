import speech_recognition as sr
import tkinter as tk
from tkinter import *


obj = tk.Tk()
obj.title("Speech Recognization")
obj.geometry('450x400')
obj.resizable(0,0)
obj.config(bg = 'SlateBlue1')

##heading
Label(obj, text = 'Speech To Text' , font='times 25 bold underline' , bg ='SlateBlue1').pack()
Label(obj, text ='Suyog Singh Rajput' , font ='times 12 bold', bg = 'SlateBlue1').pack(side = BOTTOM)
Label(obj, text ='LN18BTCS1020' , font ='times 10 bold', bg = 'SlateBlue1').pack(side = BOTTOM)

##text variable
msg = tk.Label(obj, bg ='white')

msg.place(x=20 , y=100)

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
    import texttospeech as ts
    ts.texttospeech
    
def Exit():
    root.destroy()
#Button
Button(obj, text = "Start" , font = 'times 16 bold', command = rec, bg = 'medium orchid').place(x=180, y=140)
Button(obj,text = 'EXIT',font = 'times 14 bold' , command = Exit, bg = 'firebrick1').place(x=180 , y =240)
Button(obj, text = 'Text To Speech', font='times 14 bold', command = texttospeech, bg = 'medium orchid').place(x=137,y=190)
obj.mainloop()
