import pyttsx3

username = ""
password = ""

engine = pyttsx3.init('sapi5')

voices = engine.getProperty("voices")

engine.setProperty('voice',voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()
