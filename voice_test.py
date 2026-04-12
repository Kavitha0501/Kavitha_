import queue
import sounddevice as sd
import vosk
import json
import pyttsx3
from openai import OpenAI

# 🔑 Add your API key here
client = OpenAI(api_key="your_api_key")

import queue
import sounddevice as sd
import vosk
import json
import pyttsx3


# 🔊 Text to Speech
engine = pyttsx3.init()

def speak(text):
    print("Robot:", text)
    engine.say(text)
    engine.runAndWait()

# 🧠 AI function
def ask_ai(text):
    if "what is ai" in text:
        return "AI means artificial intelligence"
    elif "robot" in text:
        return "A robot is a programmable machine"
    elif "hello" in text:
        return "Hello, how can I help you"
    else:
        return "I am still learning"

# 🎤 Load Vosk model
model = vosk.Model(r"C:\Users\hp\Downloads\vosk-model-small-en-us-0.15")

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

# 🎤 Start listening
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):

    rec = vosk.KaldiRecognizer(model, 16000)

    print("Speak...")

    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result['text']
            print("You said:", text)

            # 🎯 Exit condition
            if "exit" in text:
                speak("Goodbye")
                break

            # 🧠 Ask AI
            if text != "":
                answer = ask_ai(text)
                speak(answer)