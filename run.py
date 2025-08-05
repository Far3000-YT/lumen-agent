from app.interface import *
from app.base import *
import sys

print_home()

load = load_gemini()
if load == False:
    sys.exit()

ask_mode()