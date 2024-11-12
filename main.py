import random
import Base.Listen as Listen
import Base.Speak as Speak
import Functions.weather as weather
import Functions.time as time
import Functions.internet_speed as internet_speed
import Functions.tell_joke as joke
from MainBrain.brain import *
from DATA.DLG import *
from BRAIN.welcome_greatings import *
from BRAIN.wish_greatings import *
from Automation._intregation_automation import Automation

# Main function to listen and process commands continuously
def comain():
    while True:
        text = Listen.listen().lower()
        text = text.replace(" jar","jarvis")
        Automation(text)
        # Function_cmd(text)
        Greating(text)

        if text in bye_key_word:
            x = random.choice(res_bye)
            Speak.speak(x)
            break
        elif "jarvis" in text:
            response = brain(text)
            Speak.speak(response)
        else:
            response = brain(text)
            Speak.speak(response)

def main():
    while True:
        wake_cmd = Listen.listen().lower()
        if wake_cmd in wake_key_word:
            welcome()
            comain()
        else:
            pass

# Run the main function
main()
