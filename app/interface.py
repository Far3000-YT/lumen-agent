import colorama, sys, os
from types import Dict

def add_to_env(elements: Dict):
    #if .env, skip this step
    #else ask input for each element ? (maybe only have gemini api key as input, so maybe not dict)
    for element in elements:
        pass
        #add each element to env for initial config

def clear_terminal():
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


def print_home():
    print("""______                                      _______                    _____ 
___  / ____  ________ _______________       ___    |______ ______________  /_
__  /  _  / / /_  __ `__ \  _ \_  __ \________  /| |_  __ `/  _ \_  __ \  __/
_  /___/ /_/ /_  / / / / /  __/  / / //_____/  ___ |  /_/ //  __/  / / / /_  
/_____/\__,_/ /_/ /_/ /_/\___//_/ /_/       /_/  |_|\__, / \___//_/ /_/\__/  
                                                   /____/                    
lumen.onl - @0xFar3000 (X) - v0.0
""")


def ask_mode() -> int:
    print("""
[1] Code Mode   -  Analyze, refactor, and write code.
[2] Web Mode    -  Automate tasks in a browser.
[3] Paper Mode  -  Draft and format documents.
[x] Soon        -  More modes soon.
[0] Exit

""")

    #if anything else than number, find a way to re ask and clear user input till it works
    try:
        response = input("> Select a mode: ")

    except TypeError: print("Input should be a number!")
    except Exception as e: print(f"Unknown error: {e}")

    finally:
        return response