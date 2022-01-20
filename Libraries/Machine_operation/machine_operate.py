import threading
from . import readButtons
import time

def machineOperate():
    while(1):
        readButtons.start()
        readButtons.bail_plate_down()

def start_machineOperate_thread():
        thread = threading.Thread(target=machineOperate)
        thread.daemon = 1
        thread.start()