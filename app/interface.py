import colorama

def clear_terminal():
    pass

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

    try: response = input("> Select a mode: ")
    #if anything else than number, find a way to re ask and clear user input till it works
    except TypeError: print("Input should be a number!")
    except Exception as e: print(f"Unknown error: {e}")
    finally: return response