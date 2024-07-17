import pyttsx3

def text_to_speech(text, rate=600):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

# Example usage
text = "Hello, this is a text-to-speech conversion example."
text_to_speech(text)
