# Functions/tell_joke.py
import random

def tell_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
    "Why don't programmers like nature? It has too many bugs.",
    "Why was the math book sad? It had too many problems.",
    "I told my computer I needed a break, now it won’t stop sending me Kit-Kats.",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "Why don’t oysters donate to charity? Because they are shellfish!",
    "What’s orange and sounds like a parrot? A carrot.",
    "I asked my dog what’s two minus two. He said nothing.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I’m reading a book on anti-gravity. It’s impossible to put down."
    ]
    return random.choice(jokes)
