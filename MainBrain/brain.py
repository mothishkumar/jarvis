from BRAIN.google_big_data import *
from BRAIN.google_small_data import *
from LLM.llm1 import llm1
from LLM.llm2 import llm2
from MainBrain.load_file import *

def brain(text):
    if "jarvis" in text:
        text = text.replace("jarvis","")
        text = text.strip()
        if text in qa_dict:
            ans = qa_dict[text]
            print("fetched from Load_file")
        elif "jarvis define" in text or "jarvis brief" in text or "jarvis research" in text or "jarvis teach me" in text:
           ans = deep_search(text)
           print("fetched from deep_search")
        elif "jarvis real time data" in text or "jarvis give me real time data" in text or "jarvis who is " in text or "jarvis where is" in text :
            ans = search_brain(text)
            print("fetched from search_brain")
        elif "jarvis write a python code" in text or "jarvis make" in text or "jarvis step by step" in text or "jarvis explain" in text:
            ans= llm2(text)
            print("fetched from llm2")
        else:
            ans = llm1(text)
            print("fetched from llm1")
        return ans

    else:
        pass