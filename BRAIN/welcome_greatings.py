import random
from DATA.DLG import welcomedlg
from Base.Speak import speak


def welcome():
    result = random.choice(welcomedlg)
    speak(result)
