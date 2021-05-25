## import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr


################### Initialized window####################

root = Tk()
root.geometry('450x400')
root.resizable(0,0)
root.config(bg = 'SlateBlue1')
root.title('Speech Recognization')


##heading
Label(root, text = 'Main Menu' , font='times 25 bold underline' , bg ='SlateBlue1').pack()
Label(root, text ='Suyog Singh Rajput' , font ='times 12 bold', bg = 'SlateBlue1').pack(side = BOTTOM)
Label(root, text ='LN18BTCS1020' , font ='times 10 bold', bg = 'SlateBlue1').pack(side = BOTTOM)




#label
Label(root, text ='!!Choose!!', font ='times 20 bold underline', bg ='SlateBlue1').place(x=152,y=100)


###################define function##############################
def texttospeech():
    import texttospeech as ts
    ts.texttospeech

def Exit():
    root.destroy()

def speechtotext():
    import speechtotext as st
    st.rec

#Button
Button(root, text = "Text To Speech" , font = 'times 16 bold', command = texttospeech, bg = 'medium orchid').place(x=137, y=150)
Button(root,text = 'EXIT',font = 'times 16 bold' , command = Exit, bg = 'firebrick1').place(x=180 , y =250)
Button(root, text = 'Speech To Text', font='times 16 bold', command = speechtotext, bg = 'medium orchid').place(x=137,y=200)


#infinite loop to run program
root.mainloop()
