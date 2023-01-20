from tkinter import *
import time, math
from PIL import Image , ImageTk
from playsound import playsound

from pygame import mixer
mixer.init()

def clockSound():
    mixer.music.load('clockTicking.wav')
    print("music started playing....")
    mixer.music.set_volume(0.2)
    mixer.music.play()
    while True:
        print("------------------------------------------------------------------------------------")
        print("Press 'p' to pause the music")
        print("Press 'r' to resume the music")
        print("Press 'e' to exit the program")

        userInput = input(" ")
        if userInput == 'p':
            mixer.music.pause()	
            print("music is paused....")
        elif userInput == 'r':
            mixer.music.unpause()
            print("music is resumed....")
        elif userInput == 'e':
            mixer.music.stop()
            print("music is stopped....")
            break


def updateClock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    # x = r * sin(t)
    # y = -r * cos(t) # here we use minus coz change the direction of y 

    # updating seconds hand per second 
    seconds_x = seconds_hand_len * math.sin(math.radians(6 * seconds)) + center_x
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(6 * seconds)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)


    # updating minutes hand per second 
    minutes_x = minutes_hand_len * math.sin(math.radians(6 * minutes)) + center_x
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(6 * minutes)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)


    # updating hours hand per second 
    hours_x = hours_hand_len * math.sin(math.radians(30 * hours)) + center_x
    hours_y = -1 * hours_hand_len * math.cos(math.radians(30 * hours)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)


    root.after(1000, updateClock)

    
root = Tk()
root.title("Analog Clock")
root.geometry("400x400")


#create a canvas
canvas = Canvas(root, width=400, height=400, bg="black")
canvas.pack(expand=True, fill='both') # Here both is used for maximize and minimize window

# load an image
bg_image = Image.open('clock.png')
resize_image = bg_image.resize((430,430), Image.ANTIALIAS) 
new_image = ImageTk.PhotoImage(resize_image)
canvas.create_image(200, 200, image= new_image)

#create clock hands
center_x = 200
center_y = 200
seconds_hand_len = 120
minutes_hand_len = 90
hours_hand_len = 60

#drawing clock hands

seconds_hand = canvas.create_line(200,200,200 + seconds_hand_len, 200 + seconds_hand_len, width = 1.5, fill="red")
minutes_hand = canvas.create_line(200,200,200 + minutes_hand_len, 200 + minutes_hand_len, width = 1.5, fill="white")
hours_hand = canvas.create_line(200,200,200 + hours_hand_len, 200 + hours_hand_len, width = 1.5, fill="white")





updateClock()
clockSound()
root.mainloop()