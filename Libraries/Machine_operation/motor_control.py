from . import parameters
from . import variables
from ..IO_definitions.IO_definitions import *

def motor_on():
    variables.motor_running=1
    high(relay_MOTOR)
    sleep(parameters.DELAY_MOTOR_ON)

def motor_off():
    low(relay_MOTOR)
    variables.motor_running=0
    sleep(parameters.DELAY_MOTOR_OFF)