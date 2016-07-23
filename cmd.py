############################################################################
##  MagicQ Remote Commands
##  July 22, 2016
##  Austin Tyler
##
##  Reference: MagicQ Manual - Chapter 31. ChamSys Remote Protocol Commands
##             http://chamsys.co.uk
############################################################################

#====================================================
# Constants
#====================================================
MIN_PLAYBACK = 1
MAX_PLAYBACK = 10 # 202 on console

MIN_LEVEL    = 0
MAX_LEVEL    = 100

MIN_PAGE     = 0
MAX_PAGE     = 100

MIN_CHANNEL  = 1
MAX_CHANNEL  = 32769

MIN_CUE      = 1
MAX_CUE      = 65536

MIN_DEC      = 0
MAX_DEC      = 99

#-----------------------
# Attribute Numbers
#-----------------------

# (see INTENSITY.py, POSITION.py, COLOR.py, BEAM.py, FX.py, MACROS.py, and CONT.py)

#====================================================
# Remote Protocol Comands
#====================================================
def activate_playback(pb):
    'activate playback'
    if __validate_playback(pb) == True:
        return  str(pb) + "A"

def release_playback(pb):
    'release playback'
    if __validate_playback(pb) == True:
        return str(pb) + "R"

def test_playback(pb):
    'activate playback with level 100%'
    if __validate_playback(pb) == True:
        return str(pb) + "T"

def untest_playback(pb):
    'release playback with level 0%'
    if __validate_playback(pb) == True:
        return str(pb) + "U"

def go_playback(pb):
    'starts playback execution'
    if __validate_playback(pb) == True:
        return str(pb) + "G"

def stop_playback(pb):
    'stops or steps back a cue on playback'
    if __validate_playback(pb) == True:
        return str(pb) + "S"

def fastback_playback(pb):
    'steps back playback without fade'
    if __validate_playback(pb) == True:
        return str(pb) + "B"

def fastfwrd_playback(pb):
    'steps forward playback without fade'
    if __validate_playback(pb) == True:
        return str(pb) + "F"

def set_playback_level(pb, level):
    'sets playback to level'
    if __validate_playback(pb) == True and __validate_level(level) == True:
        return str(pb) + "," + str(level) + "L"

def playback_jump_to_cue(pb, cue):
    'jumps to cue on playback'
    id = int(cue)
    dec = int(cue * 100) - (id*100)
    if __validate_playback(pb) == True and __validate_cue(id) == True:
        return str(pb) + "," + str(id) + "," + str(dec) + "J"

def change_page(page):
    'changes page'
    if __validate_page(page) == True:
        return str(page) + "P"

def set_channel_level(chan, level):
    'sets channel intensity to level'
    if __validate_channel(chan) == True and __validate_level(level) == True:
        return str(chan) + "," + str(level) + "I"

#------------------------------
# Remote Programmer Commands
#------------------------------
# (see prog.py)

#======================================================
# Helper functions
#======================================================
def __validate_playback(pb):
    global MIN_PLAYBACK, MAX_PLAYBACK
    if pb < MIN_PLAYBACK or pb > MAX_PLAYBACK:
        raise ValueError('Invalid Playback')
    else:
        return  True

def __validate_level(level):
    global MIN_LEVEL, MAX_LEVEL
    if level < MIN_LEVEL or level > MAX_LEVEL:
        raise ValueError('Invalid Level')
    else:
        return True

def __validate_page(page):
    global MIN_PAGE, MAX_PAGE
    if page < MIN_PAGE or page > MAX_PAGE:
        raise ValueError('Invalid Page Number')
    else:
        return True

def __validate_channel(chan):
    global MIN_CHANNEL, MAX_CHANNEL
    if chan < MIN_CHANNEL or chan > MAX_CHANNEL:
        raise ValueError('Invalid Channel')
    else:
        return True

def __validate_cue(cue):
    global MIN_CUE, MAX_CUE
    if cue < MIN_CUE or cue > MAX_CUE:
        raise ValueError('Invalid Cue Id')
    else:
        return True

def __validate_decimal(dec):
    global MIN_DEC, MAX_DEC
    if dec < MIN_DEC or dec > MAX_DEC:
        raise ValueError('Invalid Cue Decimal')
    else:
        return True
