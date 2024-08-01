# import pyjokes
#this pyjokes is the external modules so first we have to install it using the command  "pip install pyjokes"  in terminals 
#similarly  pyttsx3 is the external modules so install it using "pip install pyttsx" that converts the text into speech
import pyttsx3

# jokes=pyjokes.get_joke()

# print(jokes)
# for single line comment use # symbol
# for multiple line commens use """ here the statements goes on """
"""
 this is multiline comments
   """


# text to speech
engine=pyttsx3.init()
engine.say("hello bikash how are you")
engine.runAndWait