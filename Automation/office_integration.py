from Office.ConnectionStringchange import *
import Base.Speak as Speak
from DATA.office import *

def office_cmd(text):
    if "mdms connection to bhopal" in text:
        # Update the configuration for the specified file path and bhopal_prod values
        update_config_values(path["mdms"], bhopal_prod)
        Speak.speak("Updated successfully")
    elif "mdms connection to jabalpur" in text:
        # Update the configuration for the specified file path and bhopal_prod values
        update_config_values(path["mdms"], bhopal_prod)
        Speak.speak("Updated successfully")
    elif "mdms connection to jabalpur tnd" in text:
        # Update the configuration for the specified file path and bhopal_prod values
        update_config_values(path["mdms"], bhopal_prod)
        Speak.speak("Updated successfully")
    else:
        pass
