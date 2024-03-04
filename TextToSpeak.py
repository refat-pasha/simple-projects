#import os
import pyttsx3




if __name__ == '__main__':
    print("Welcome to RoboSpeaker. Created by Refat!")

    engine = pyttsx3.init()
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech, words per minute
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

    while True:
        x = input("Enter what you want me to speak: ")
        if x == "x":
            break
        engine.say(x)
        engine.runAndWait()




