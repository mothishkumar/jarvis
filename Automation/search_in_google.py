import pywhatkit
import random
from DATA.DLG import search_result
from Base.Speak import speak


def search_google(text):
    dlg = random.choice(search_result)
    pywhatkit.search(text)
    speak(dlg)
