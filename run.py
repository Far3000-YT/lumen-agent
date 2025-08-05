from app.interface import *
from app.base import *
from app.paper_mode import *
import sys

print_home()

load = load_gemini()
if load == False:
    sys.exit()

user_input = ask_mode()

match user_input:
    case 0:
        sys.exit()
    case 1:
        print("Mode not available yet.")
    case 2:
        print("Mode not available yet.")
    case 3:
        paper_input()