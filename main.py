from lib.Status import create_Presence
from win32gui import GetWindowText, GetForegroundWindow
import time

while True:
    title = GetWindowText(GetForegroundWindow())
    if(title):
        create_Presence(title)
    time.sleep(5)