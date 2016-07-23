############################################################################
##  MagicQ Remote Programmer Commands
##  July 22, 2016
##  Austin Tyler
##
##  Reference: MagicQ Manual - Chapter 31. ChamSys Remote Protocol Commands
##             http://chamsys.co.uk
############################################################################

#====================================================
# Constants
#====================================================
MIN_LEVEL    = 0
MAX_LEVEL    = 100

MIN_PALETTE  = 1
MAX_PALETTE  = 1024

MIN_CUE      = 1
MAX_CUE      = 5000

MIN_GROUP    = 1
MAX_GROUP    = 200

MIN_HEAD     = 1
MAX_HEAD     = 6145

MIN_SHOWFILE = 0
MAX_SHOWFILE = 9999

MIN_TIME = 0

TOGGLE = 2

#======================================================
# Remote Programmer Commands
#======================================================
def select_heads(start, end = 0):
    'select heads from start to end'
    if end == 0:
        if __validate_head(start) == True:
            return "01," + str(start) + "H"
    elif __validate_head(start) == True and __validate_head(end) == True:
        return "01," + str(start) + "," + str(end) + "H"

def deselect_heads(start, end = 0):
    'deselect heads from start to end'
    if end == 0:
        if __validate_head(start) == True:
            return "02," + str(start) + "H"
    elif __validate_head(start) == True and __validate_head(end) == True:
        return "02," + str(start) + "," + str(end) + "H"

def deselect_all_heads():
    'deselect all heads'
    return "03H"

def select_group(group):
    'select group'
    if __validate_group(group) == True:
        return "04," + str(group) + "H"

def set_intensity(level, time = 0):
    'set intensity of selected heads'
    if __validate_time(time) == True and __validate_level(level) == True:
        string =  "05," + str(level)
        if time != 0:
            string +=  "," + str(time)
        string += "H"
        return string

def set_attribute(attribute, value, time = 0):
    'set attribute of selected heads'
    string = "06," + str(attribute) + "," + str(value)
    if time != 0 and __validate_time(time) == True:
        string += "," + str(time)
    string += "H"
    return string

def increase_attribute(attribute, value, fine = None):
    'increase attribute'
    string = "07," + str(attribute) + "," + str(value)
    if fine == 1 or fine == 0:
        string += "," + str(fine)
    string += "H"
    return string

def decrease_attribute(attribute, value, fine = None):
    'decrease attribute'
    string = "08," + str(attribute) + "," + str(value)
    if fine == 1 or fine == 0:
        string += "," + str(fine)
    string += "H"
    return string

def clear_programmer():
    'clear programmer'
    return "09H"

def include_position_palette(palette):
    'include postion palette'
    if __validate_palette(palette) == True:
        return "10," + str(palette) + "H"

def include_color_palette(palette):
    'include color palette' 
    if __validate_palette(palette) == True:
        return "11," + str(palette) + "H"

def include_beam_palette(palette):
    'include beam palette' 
    if __validate_palette(palette) == True:
        return "12," + str(palette) + "H"

def include_cue(cue):
    'include cue'
    if __validate_cue(cue) == True:
        return "13," + str(cue) + "H"

def update():
    'update included cue'
    return "14H"

def record_position_palette(palette):
    'record postion palette' 
    if __validate_palette(palette) == True:
        return "20," + str(palette) + "H"

def record_color_palette(palette):
    'record color palette'
    if __validate_palette(palette) == True:
        return "21," + str(palette) + "H"

def record_beam_palette(palette):
    'record beam palette'
    if __validate_palette(palette) == True:
        return "22," + str(palette) + "H"

def record_cue(cue):
    'record cue'
    if __validate_cue(cue) == True:
        return "23," + str(cue) + "H"

def next_head():
    'next head in selection'
    return "30H"

def previous_head():
    'previous head in selection'
    return "31H"

def all_heads():
    'all heads in selection'
    return "32H"

def locate():
    'locate selected heads'
    return "40H"

def lamp_on():
    'lamp on selected heads'
    return "41H"

def lamp_off():
    'lamp off selected heads'
    return "42H"

def reset():
    'reset'
    return "43H"

def remote_trigger(state):
    'set trigger state'
    if state >= 0 and state <= TOGGLE:
        return "71," + str(state) + "H"
    else:
        raise ValueError('Invalid State')

def test_cue(cue):
    'test/activate cue'
    if __validate_cue(cue) == True:
        return "80," + str(cue) + "H"

def untest_cue(cue):
    'untest/release cue'
    if __validate_cue(cue) == True:
        return "81," + str(cue) + "H"

def test_cue_stack(cue_stack):
    'test/activate cue stack'
    if __validate_stack(cue_stack) == True:
        return "82," + str(cue_stack) + "H"

def untest_cue_stack(cue_stack):
    'untest/release cue stack'
    if __validate_stack(cue_stack) == True:
        return "83," + str(cue_stack) + "H"

def save_show(file_id):
    'save showXXXX.shw'
    if __validate_showfile(file_id) == True:
        return "90," + str(file_id) + "H"

def load_show(file_id):
    'load showXXXX.shw'
    if __validate_showfile(file_id) == True:
        return "91," + str(file_id) + "H"

#======================================================
# Helper functions
#======================================================
def __validate_level(level):
    global MIN_LEVEL, MAX_LEVEL
    if level < MIN_LEVEL or level > MAX_LEVEL:
        raise ValueError('Invalid Level')
    else:
        return True

def __validate_palette(pal):
    global MIN_PALETTE, MAX_PALETTE
    if pal < MIN_PALETTE or pal > MAX_PALETTE:
        raise ValueError('Invalid Palette Id')
    else:
        return True

def __validate_cue(cue):
    global MIN_CUE, MAX_CUE
    if cue < MIN_CUE or cue > MAX_CUE:
        raise ValueError('Invalid Cue Id')
    else:
        return True

def __validate_group(grp):
    global MIN_GROUP, MAX_GROUP
    if grp < MIN_GROUP or grp > MAX_GROUP:
        raise ValueError('Invalid Group Id')
    else:
        return True

def __validate_head(hd):
    global MIN_HEAD, MAX_HEAD
    if hd < MIN_HEAD or hd > MAX_HEAD:
        raise ValueError('Invalid Head Id')
    else:
        return True

def __validate_showfile(file):
    global MIN_SHOWFILE, MAX_SHOWFILE
    if file < MIN_SHOWFILE or file > MAX_SHOWFILE:
        raise ValueError('Invalid Showfile Id')
    else:
        return True

def __validate_time(time):
    global MIN_TIME
    if time < MIN_TIME:
        raise ValueError('Invalid Time')
    else:
        return True

def __validate_stack(stack):
    'no validation data provided from manual'
    return True
