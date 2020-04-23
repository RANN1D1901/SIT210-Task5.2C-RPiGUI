from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led1=LED(17)
led2=LED(4)
led3=LED(21)

win=Tk()
win.title("FIRST GUI")
myFont=tkinter.font.Font(family='Helvetica',size=12,weight='bold')


def led1Toggle():
    if led1.is_lit:
        led1.off()
        led1Button["text"]="Turn LED ON"
    else:
        led1.on()
        led1Button["text"]="Turn LED OFF"
def led2Toggle():
    if led2.is_lit:
        led2.off()
        led2Button["text"]="Turn LED ON"
    else:
        led2.on()
        led2Button["text"]="Turn LED OFF"
def led3Toggle():
    if led3.is_lit:
        led3.off()
        led3Button["text"]="Turn LED ON"
    else:
        led3.on()
        led3Button["text"]="Turn LED OFF"
def close():
    RPi.GPIO.cleanup()
    win.destroy()
led1Button=Button(win,text="Turn LED ON ",font=myFont,command=led1Toggle,bg='white',height=1,width=24)
led1Button.grid(row=0,column=1)
led2Button=Button(win,text="Turn LED ON ",font=myFont,command=led2Toggle,bg='blue',height=1,width=24)
led2Button.grid(row=1,column=1)
led3Button=Button(win,text="Turn LED ON ",font=myFont,command=led3Toggle,bg='white',height=1,width=24)
led3Button.grid(row=2,column=1)
exitButton=Button(win,text="Exit ",font=myFont,command=close,bg='red',height=1,width=10)
exitButton.grid(row=3,column=1)
win.protocol("WM_DELETE_WINDOW",close)
win.mainloop() 