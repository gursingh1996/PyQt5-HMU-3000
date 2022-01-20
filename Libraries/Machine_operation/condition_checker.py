from . import warning
from . import function_number
from . import variables
from Libraries.IO_definitions.IO_definitions import *
from . import parameters

def startingCondition(conditionFor):
    if conditionFor == function_number.GOTO_default: #for baling plate while going down so that lock doesnot interfere
        if not read(limit_LOCK_out) and read(limit_LOWER_PLATE_back) and read(limit_UPPER_PLATE_back):  
            return warning.lock_not_out

    elif not read(limit_BAIL_PLATE_down):		#if bail plate is not down
        return warning.BAIL_PLATE_not_down
    
    elif not read(limit_LOWER_PLATE_back):
        return warning.LOWER_PLATE_not_back

    elif not read(limit_LOCK_out):		#if lock is not in initial position
        return warning.lock_not_out
    
    elif not read(limit_UPPER_PLATE_back):		#if upper plate is not in initial position
        return warning.UPPER_PLATE_not_up

    return warning.all_ok		#if every thing is fine return ok


def runningConditions(operation):
    if read(btn_RESET): return warning.reset_pressed

    if operation == function_number.UPPER_PLATE_forward:
        if variables.pressureSense >= parameters.UPPER_PLATE_forward_pressure:
            return warning.upper_plate_forward_pressure_reached
        
    elif operation == function_number.LOWER_PLATE_backward:
        if variables.pressureSense >= parameters.LOWER_PLATE_backward_pressure:
            return warning.lower_plate_back_pressure_reached

    elif operation == function_number.LOCK_OUT:
        return 0
    
    elif operation == function_number.UPPER_PLATE_back:
        if variables.pressureSense >= parameters.UPPER_PLATE_backward_pressure:
            return warning.upper_plate_back_pressure_reached

    elif operation == function_number.LOCK_APPLY:
        return 0

    elif operation == function_number.LOWER_PLATE_forward:
        if variables.pressureSense >= parameters.LOWER_PLATE_forward_pressure:
            return warning.lower_plate_forward_pressure_reached
    
    elif operation == function_number.BALE_PLATE_up:
        if variables.pressureSense >= parameters.BALE_PLATE_up_pressure:
            return warning.bale_plate_up_pressure_reached
 
    elif operation == function_number.BALE_PLATE_down:
        return 0

    return 0