from Automation.common_intregation import *
from Automation.google_intregation_main import *
from Automation.battery_intregation_main import *
from Automation.youtube_intregation_main import *
from Automation.office_integration import *


def Automation(text):
    office_cmd(text)
    youtube_cmd(text)
    google_cmd(text)
    battery_cmd(text)
    common_cmd(text)

