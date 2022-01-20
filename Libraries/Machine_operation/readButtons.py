from . import function_number
from . import movements
from . import variables
from . import condition_checker
from . import motor_control
from . import warning
from time import sleep
from ..IO_definitions.IO_definitions import *

def start():
    if read(btn_START):
        for i in range(1000):
            sleep(0.001)
            if read(btn_START)==0:
                i=0
                break
        
        if i==999:      #return to default position
            variables.stopped_with_reset=0
            fault = condition_checker.startingCondition(0)
            if fault: 
                movements.default_position_return()
                motor_control.motor_off()
            
            variables.starting_pos=function_number.UPPER_PLATE_press_budle

        elif variables.stopped_with_reset:       #stopped with reset
            variables.stopped_with_reset=0
            variables.starting_pos = movements.normalStart(variables.starting_pos)
        
        else:       #normal start
            fault = condition_checker.startingCondition(0)
            if fault != warning.all_ok:
                movements.default_position_return()
                motor_control.motor_off()
            
            else:   variables.starting_pos = movements.normalStart(function_number.UPPER_PLATE_press_budle)
    
def bail_plate_down():
    if read(btn_BALE_PLATE_down):
        fault = movements.bring_bail_plate_down()
        if fault==warning.reset_pressed:
            variables.starting_pos = function_number.BALE_PLATE_bring_down

        motor_control.motor_off()