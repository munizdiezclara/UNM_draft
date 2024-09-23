#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on septiembre 05, 2023, at 09:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'UNM04_3'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '',
    'age': '',
    'gender': ["male","female", "non-binary", "other"],
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Clara\\OneDrive - Lancaster University\\Experiments\\UNM05\\UNM05_4_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "counterbalance" ---

# --- Initialize components for Routine "information" ---
continue_info = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='continue_info',
     autoLog=False,
)
mouse_info = event.Mouse(win=win)
x, y = [None, None]
mouse_info.mouseClock = core.Clock()
image_info = visual.ImageStim(
    win=win,
    name='image_info', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.45, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "consent" ---
c1 = visual.TextBox2(
     win, text='I agree to participate in the study on learning the predictive value of cues as described. I understand that my responses will be treated confidentially and that I have the option to withdraw from the study.', font='Trebuchet MS',
     pos=(-0.2, 0.35),     letterHeight=0.028,
     size=(0.7, 0.2), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='c1',
     autoLog=False,
)
c2 = visual.TextBox2(
     win, text='I understand my participation is completely voluntary.', font='Trebuchet MS',
     pos=(-0.2, 0.20),     letterHeight=0.028,
     size=(0.7, 0.2), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='c2',
     autoLog=False,
)
c3 = visual.TextBox2(
     win, text='I understand I have the right to withdraw from the study at any time during or at the end of the study without giving a reason and with no adverse consequences.', font='Trebuchet MS',
     pos=(-0.2, 0.05),     letterHeight=0.028,
     size=(0.7, 0.2), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='c3',
     autoLog=False,
)
c4 = visual.TextBox2(
     win, text='I have been given full information about what the study entails.', font='Trebuchet MS',
     pos=(-0.2, -0.125),     letterHeight=0.028,
     size=(0.7, 0.2), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='c4',
     autoLog=False,
)
c5 = visual.TextBox2(
     win, text='I have been given contact information for the research team.', font='Trebuchet MS',
     pos=(-0.2, -0.25),     letterHeight=0.028,
     size=(0.7, 0.2), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='c5',
     autoLog=False,
)
c6 = visual.TextBox2(
     win, text='I understand my responses will be fully anonymized.', font='Trebuchet MS',
     pos=(-0.2, -0.35),     letterHeight=0.028,
     size=(0.7, 0.2), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='c6',
     autoLog=False,
)
slider_1 = visual.Slider(win=win, name='slider_1',
    startValue=None, size=(0.065, 0.02), pos=(0.37, 0.35), units=None,
    labels=['Yes', 'No'], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, ori=0.0, depth=-6, readOnly=False)
slider_2 = visual.Slider(win=win, name='slider_2',
    startValue=None, size=(0.065, 0.02), pos=(0.37, 0.2), units=None,
    labels=['Yes', 'No'], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, ori=0.0, depth=-7, readOnly=False)
slider_3 = visual.Slider(win=win, name='slider_3',
    startValue=None, size=(0.065, 0.02), pos=(0.37, 0.05), units=None,
    labels=['Yes', 'No'], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, ori=0.0, depth=-8, readOnly=False)
slider_4 = visual.Slider(win=win, name='slider_4',
    startValue=None, size=(0.065, 0.02), pos=(0.37, -0.125), units=None,
    labels=['Yes', 'No'], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, ori=0.0, depth=-9, readOnly=False)
slider_5 = visual.Slider(win=win, name='slider_5',
    startValue=None, size=(0.065, 0.02), pos=(0.37, -0.25), units=None,
    labels=['Yes', 'No'], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, ori=0.0, depth=-10, readOnly=False)
slider_6 = visual.Slider(win=win, name='slider_6',
    startValue=None, size=(0.065, 0.02), pos=(0.37, -0.35), units=None,
    labels=['Yes', 'No'], ticks=(1,2), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, ori=0.0, depth=-11, readOnly=False)
mouse_consent = event.Mouse(win=win)
x, y = [None, None]
mouse_consent.mouseClock = core.Clock()
consent_box = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='consent_box',
     autoLog=False,
)

# --- Initialize components for Routine "instructions_1" ---
cont_train_instr = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='cont_train_instr',
     autoLog=False,
)
cont_train_instr_mouse = event.Mouse(win=win)
x, y = [None, None]
cont_train_instr_mouse.mouseClock = core.Clock()
train_instructions = visual.ImageStim(
    win=win,
    name='train_instructions', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.4, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "comprehension1" ---
comp1_resp1 = visual.TextBox2(
     win, text='Learn which mutant would result of each chemicals combination', font='Trebuchet MS',
     pos=(-0.71, -0.2),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp1_resp1',
     autoLog=False,
)
comp1_resp2 = visual.TextBox2(
     win, text='Predict which mutant would take over the world', font='Trebuchet MS',
     pos=(-0.71, -0.26),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp1_resp2',
     autoLog=False,
)
comp1_resp3 = visual.TextBox2(
     win, text='Decide if the chemicals are organic or inorganic', font='Trebuchet MS',
     pos=(-0.71, -0.32),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp1_resp3',
     autoLog=False,
)
comp1_mouse = event.Mouse(win=win)
x, y = [None, None]
comp1_mouse.mouseClock = core.Clock()
check1 = visual.ImageStim(
    win=win,
    name='check1', 
    image='instructions/check1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.45, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "instructions_1" ---
cont_train_instr = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='cont_train_instr',
     autoLog=False,
)
cont_train_instr_mouse = event.Mouse(win=win)
x, y = [None, None]
cont_train_instr_mouse.mouseClock = core.Clock()
train_instructions = visual.ImageStim(
    win=win,
    name='train_instructions', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.4, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "comprehension1_2" ---
comp1_resp1_2 = visual.TextBox2(
     win, text='Learn which mutant would result of each chemicals combination', font='Trebuchet MS',
     pos=(-0.71, -0.2),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp1_resp1_2',
     autoLog=False,
)
comp1_resp2_2 = visual.TextBox2(
     win, text='Predict which mutant would take over the world', font='Trebuchet MS',
     pos=(-0.71, -0.26),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp1_resp2_2',
     autoLog=False,
)
comp1_resp3_2 = visual.TextBox2(
     win, text='Decide if the chemicals are organic or inorganic', font='Trebuchet MS',
     pos=(-0.71, -0.32),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp1_resp3_2',
     autoLog=False,
)
comp1_mouse_2 = event.Mouse(win=win)
x, y = [None, None]
comp1_mouse_2.mouseClock = core.Clock()
check1_2 = visual.ImageStim(
    win=win,
    name='check1_2', 
    image='instructions/check1_2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.45, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "cue_o__trial" ---
# Run 'Begin Experiment' code from cue_random
cues = ["stimuli/cue_a1.png", "stimuli/cue_a2.png", "stimuli/cue_a3.png", "stimuli/cue_a4.png", "stimuli/cue_a5.png", "stimuli/cue_a6.png", "stimuli/cue_a7.png", "stimuli/cue_a8.png"]
distractors_vsubtle = ["stimuli/cue_b1.png", "stimuli/cue_b2.png", "stimuli/cue_b3.png", "stimuli/cue_b4.png", "stimuli/cue_b5.png", "stimuli/cue_b6.png", "stimuli/cue_b7.png", "stimuli/cue_b8.png"]
distractors_subtle = ["stimuli/cue_c1.png", "stimuli/cue_c2.png", "stimuli/cue_c3.png", "stimuli/cue_c4.png", "stimuli/cue_c5.png", "stimuli/cue_c6.png", "stimuli/cue_c7.png", "stimuli/cue_c8.png"]
distractors_nosubtle = ["stimuli/cue_d1.png", "stimuli/cue_d2.png", "stimuli/cue_d3.png", "stimuli/cue_d4.png", "stimuli/cue_d5.png", "stimuli/cue_d6.png", "stimuli/cue_d7.png", "stimuli/cue_d8.png"]
order = [1, 2, 3, 4, 5, 6, 7, 8]
shuffle (order)

reorder_cues = [cues[i-1] for i in order]
reorder_vsubtle = [distractors_vsubtle[i-1] for i in order]
reorder_subtle = [distractors_subtle[i-1] for i in order]
reorder_nosubtle = [distractors_nosubtle[i-1] for i in order]
blank_training = visual.TextStim(win=win, name='blank_training',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
predictive_cue = visual.ImageStim(
    win=win,
    name='predictive_cue', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
non_predictive_cue = visual.ImageStim(
    win=win,
    name='non_predictive_cue', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
o1_image = visual.ImageStim(
    win=win,
    name='o1_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.16, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
o2_image = visual.ImageStim(
    win=win,
    name='o2_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.16, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
cue_o_mouse = event.Mouse(win=win)
x, y = [None, None]
cue_o_mouse.mouseClock = core.Clock()
timeout_text = visual.TextStim(win=win, name='timeout_text',
    text='TIMEOUT - TOO SLOW',
    font='Trebuchet MS',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "cue_selection" ---
predictive_cue_selection = visual.ImageStim(
    win=win,
    name='predictive_cue_selection', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
non_predictive_cue_selection = visual.ImageStim(
    win=win,
    name='non_predictive_cue_selection', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
o1_image_selection = visual.ImageStim(
    win=win,
    name='o1_image_selection', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.16, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
o2_image_selection = visual.ImageStim(
    win=win,
    name='o2_image_selection', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.16, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
yellow_frame = visual.ImageStim(
    win=win,
    name='yellow_frame', 
    image='stimuli/yellow_frame.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.16, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "feedback" ---
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Trebuchet MS',
    pos=(0, -0.05), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
predictive_cue_feedback = visual.ImageStim(
    win=win,
    name='predictive_cue_feedback', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
non_predictive_cue_feedback = visual.ImageStim(
    win=win,
    name='non_predictive_cue_feedback', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
o1_image_feedback = visual.ImageStim(
    win=win,
    name='o1_image_feedback', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.16, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
o2_image_feedback = visual.ImageStim(
    win=win,
    name='o2_image_feedback', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.16, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "test1_vsubtle_inst" ---
cont_test1_vsubtle = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='cont_test1_vsubtle',
     autoLog=False,
)
cont_mouse_test1_vsubtle = event.Mouse(win=win)
x, y = [None, None]
cont_mouse_test1_vsubtle.mouseClock = core.Clock()
instructions_test1_vsubtle = visual.ImageStim(
    win=win,
    name='instructions_test1_vsubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.4, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "comprehension2" ---
comp2_resp2 = visual.TextBox2(
     win, text='Click on the mutant that would result of each chemicals combination', font='Trebuchet MS',
     pos=(-0.71, -0.2),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp2_resp2',
     autoLog=False,
)
comp2_resp1 = visual.TextBox2(
     win, text='Select the chemical you have seen before', font='Trebuchet MS',
     pos=(-0.71, -0.26),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp2_resp1',
     autoLog=False,
)
comp2_resp3 = visual.TextBox2(
     win, text='Rate how beautiful the chemicals presented are', font='Trebuchet MS',
     pos=(-0.71, -0.32),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp2_resp3',
     autoLog=False,
)
comp2_mouse = event.Mouse(win=win)
x, y = [None, None]
comp2_mouse.mouseClock = core.Clock()
check2 = visual.ImageStim(
    win=win,
    name='check2', 
    image='instructions/check2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.45, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "test1_vsubtle_choice" ---
blank_test1_vsubtle = visual.TextStim(win=win, name='blank_test1_vsubtle',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
target_test1_vsubtle = visual.ImageStim(
    win=win,
    name='target_test1_vsubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
distractor_test1_vsubtle = visual.ImageStim(
    win=win,
    name='distractor_test1_vsubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
mouse_test1_vsubtle = event.Mouse(win=win)
x, y = [None, None]
mouse_test1_vsubtle.mouseClock = core.Clock()

# --- Initialize components for Routine "test1_vsubtle_rate" ---
slider_text_test1_vsubtle = visual.TextStim(win=win, name='slider_text_test1_vsubtle',
    text='How confident are you of your response?',
    font='Trebuchet MS',
    pos=(0, -0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_test1_vsubtle = visual.Slider(win=win, name='slider_test1_vsubtle',
    startValue=5.5, size=(0.5, 0.025), pos=(0, -0.2), units=None,
    labels=["I am guessing", "I am certain"], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.5,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Trebuchet MS', labelHeight=0.028,
    flip=False, ori=0.0, depth=-1, readOnly=False)
slider_target_test1_vsubtle = visual.ImageStim(
    win=win,
    name='slider_target_test1_vsubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
slider_distractor_test1_vsubtle = visual.ImageStim(
    win=win,
    name='slider_distractor_test1_vsubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
continue_rate_test1_vsubtle = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='continue_rate_test1_vsubtle',
     autoLog=False,
)
mouse_continue_test1_vsubtle = event.Mouse(win=win)
x, y = [None, None]
mouse_continue_test1_vsubtle.mouseClock = core.Clock()

# --- Initialize components for Routine "test2_vsubtle_inst" ---
cont_test2_vsubtle = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='cont_test2_vsubtle',
     autoLog=False,
)
cont_mouse_test2_vsubtle = event.Mouse(win=win)
x, y = [None, None]
cont_mouse_test2_vsubtle.mouseClock = core.Clock()
instructions_test2_vsubtle = visual.ImageStim(
    win=win,
    name='instructions_test2_vsubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.4, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "comprehension3" ---
comp3_resp2 = visual.TextBox2(
     win, text='Click on the mutant that would result of each chemicals combination', font='Trebuchet MS',
     pos=(-0.71, -0.2),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp3_resp2',
     autoLog=False,
)
comp3_resp1 = visual.TextBox2(
     win, text='Select the chemical you have seen in Task 1', font='Trebuchet MS',
     pos=(-0.71, -0.26),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp3_resp1',
     autoLog=False,
)
comp3_resp3 = visual.TextBox2(
     win, text='Rate how beautiful the chemicals presented are', font='Trebuchet MS',
     pos=(-0.71, -0.32),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp3_resp3',
     autoLog=False,
)
comp3_mouse = event.Mouse(win=win)
x, y = [None, None]
comp3_mouse.mouseClock = core.Clock()
check3 = visual.ImageStim(
    win=win,
    name='check3', 
    image='instructions/check3.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.45, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "test2_vsubtle_choice" ---
blank_test2_vsubtle = visual.TextStim(win=win, name='blank_test2_vsubtle',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
target_test2_vsubtle = visual.ImageStim(
    win=win,
    name='target_test2_vsubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
distractor_test2_vsubtle = visual.ImageStim(
    win=win,
    name='distractor_test2_vsubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
mouse_test2_vsubtle = event.Mouse(win=win)
x, y = [None, None]
mouse_test2_vsubtle.mouseClock = core.Clock()

# --- Initialize components for Routine "test2_vsubtle_rate" ---
slider_text_test2_vsubtle = visual.TextStim(win=win, name='slider_text_test2_vsubtle',
    text='How confident are you of your response?',
    font='Trebuchet MS',
    pos=(0, -0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_test2_vsubtle = visual.Slider(win=win, name='slider_test2_vsubtle',
    startValue=5.5, size=(0.5, 0.025), pos=(0, -0.2), units=None,
    labels=["I am guessing", "I am certain"], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.5,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Trebuchet MS', labelHeight=0.028,
    flip=False, ori=0.0, depth=-1, readOnly=False)
slider_target_test2_vsubtle = visual.ImageStim(
    win=win,
    name='slider_target_test2_vsubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
slider_distractor_test2_vsubtle = visual.ImageStim(
    win=win,
    name='slider_distractor_test2_vsubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
continue_rate_test2_vsubtle = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='continue_rate_test2_vsubtle',
     autoLog=False,
)
mouse_continue_test2_vsubtle = event.Mouse(win=win)
x, y = [None, None]
mouse_continue_test2_vsubtle.mouseClock = core.Clock()

# --- Initialize components for Routine "test1_subtle_inst" ---
cont_test1_subtle = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='cont_test1_subtle',
     autoLog=False,
)
cont_mouse_test1_subtle = event.Mouse(win=win)
x, y = [None, None]
cont_mouse_test1_subtle.mouseClock = core.Clock()
instructions_test1_subtle = visual.ImageStim(
    win=win,
    name='instructions_test1_subtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.4, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "comprehension2" ---
comp2_resp2 = visual.TextBox2(
     win, text='Click on the mutant that would result of each chemicals combination', font='Trebuchet MS',
     pos=(-0.71, -0.2),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp2_resp2',
     autoLog=False,
)
comp2_resp1 = visual.TextBox2(
     win, text='Select the chemical you have seen before', font='Trebuchet MS',
     pos=(-0.71, -0.26),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp2_resp1',
     autoLog=False,
)
comp2_resp3 = visual.TextBox2(
     win, text='Rate how beautiful the chemicals presented are', font='Trebuchet MS',
     pos=(-0.71, -0.32),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp2_resp3',
     autoLog=False,
)
comp2_mouse = event.Mouse(win=win)
x, y = [None, None]
comp2_mouse.mouseClock = core.Clock()
check2 = visual.ImageStim(
    win=win,
    name='check2', 
    image='instructions/check2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.45, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "test1_subtle_choice" ---
blank_test1_subtle = visual.TextStim(win=win, name='blank_test1_subtle',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
target_test1_subtle = visual.ImageStim(
    win=win,
    name='target_test1_subtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
distractor_test1_subtle = visual.ImageStim(
    win=win,
    name='distractor_test1_subtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
mouse_test1_subtle = event.Mouse(win=win)
x, y = [None, None]
mouse_test1_subtle.mouseClock = core.Clock()

# --- Initialize components for Routine "test1_subtle_rate" ---
slider_text_test1_subtle = visual.TextStim(win=win, name='slider_text_test1_subtle',
    text='How confident are you of your response?',
    font='Trebuchet MS',
    pos=(0, -0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_test1_subtle = visual.Slider(win=win, name='slider_test1_subtle',
    startValue=5.5, size=(0.5, 0.025), pos=(0, -0.2), units=None,
    labels=["I am guessing", "I am certain"], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.5,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Trebuchet MS', labelHeight=0.028,
    flip=False, ori=0.0, depth=-1, readOnly=False)
slider_target_test1_subtle = visual.ImageStim(
    win=win,
    name='slider_target_test1_subtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
slider_distractor_test1_subtle = visual.ImageStim(
    win=win,
    name='slider_distractor_test1_subtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
continue_rate_test1_subtle = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='continue_rate_test1_subtle',
     autoLog=False,
)
mouse_continue_test1_subtle = event.Mouse(win=win)
x, y = [None, None]
mouse_continue_test1_subtle.mouseClock = core.Clock()

# --- Initialize components for Routine "test2_subtle_inst" ---
cont_test2_subtle = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='cont_test2_subtle',
     autoLog=False,
)
cont_mouse_test2_subtle = event.Mouse(win=win)
x, y = [None, None]
cont_mouse_test2_subtle.mouseClock = core.Clock()
instructions_test2_subtle = visual.ImageStim(
    win=win,
    name='instructions_test2_subtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.4, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "comprehension3" ---
comp3_resp2 = visual.TextBox2(
     win, text='Click on the mutant that would result of each chemicals combination', font='Trebuchet MS',
     pos=(-0.71, -0.2),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp3_resp2',
     autoLog=False,
)
comp3_resp1 = visual.TextBox2(
     win, text='Select the chemical you have seen in Task 1', font='Trebuchet MS',
     pos=(-0.71, -0.26),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp3_resp1',
     autoLog=False,
)
comp3_resp3 = visual.TextBox2(
     win, text='Rate how beautiful the chemicals presented are', font='Trebuchet MS',
     pos=(-0.71, -0.32),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp3_resp3',
     autoLog=False,
)
comp3_mouse = event.Mouse(win=win)
x, y = [None, None]
comp3_mouse.mouseClock = core.Clock()
check3 = visual.ImageStim(
    win=win,
    name='check3', 
    image='instructions/check3.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.45, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "test2_subtle_choice" ---
blank_test2_subtle = visual.TextStim(win=win, name='blank_test2_subtle',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
target_test2_subtle = visual.ImageStim(
    win=win,
    name='target_test2_subtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
distractor_test2_subtle = visual.ImageStim(
    win=win,
    name='distractor_test2_subtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
mouse_test2_subtle = event.Mouse(win=win)
x, y = [None, None]
mouse_test2_subtle.mouseClock = core.Clock()

# --- Initialize components for Routine "test2_subtle_rate" ---
slider_text_test2_subtle = visual.TextStim(win=win, name='slider_text_test2_subtle',
    text='How confident are you of your response?',
    font='Trebuchet MS',
    pos=(0, -0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_test2_subtle = visual.Slider(win=win, name='slider_test2_subtle',
    startValue=5.5, size=(0.5, 0.025), pos=(0, -0.2), units=None,
    labels=["I am guessing", "I am certain"], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.5,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Trebuchet MS', labelHeight=0.028,
    flip=False, ori=0.0, depth=-1, readOnly=False)
slider_target_test2_subtle = visual.ImageStim(
    win=win,
    name='slider_target_test2_subtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
slider_distractor_test2_subtle = visual.ImageStim(
    win=win,
    name='slider_distractor_test2_subtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
continue_rate_test2_subtle = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='continue_rate_test2_subtle',
     autoLog=False,
)
mouse_continue_test2_subtle = event.Mouse(win=win)
x, y = [None, None]
mouse_continue_test2_subtle.mouseClock = core.Clock()

# --- Initialize components for Routine "test1_nosubtle_inst" ---
cont_test1_nosubtle = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='cont_test1_nosubtle',
     autoLog=False,
)
cont_mouse_test1_nosubtle = event.Mouse(win=win)
x, y = [None, None]
cont_mouse_test1_nosubtle.mouseClock = core.Clock()
instructions_test1_nosubtle = visual.ImageStim(
    win=win,
    name='instructions_test1_nosubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.4, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "comprehension2" ---
comp2_resp2 = visual.TextBox2(
     win, text='Click on the mutant that would result of each chemicals combination', font='Trebuchet MS',
     pos=(-0.71, -0.2),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp2_resp2',
     autoLog=False,
)
comp2_resp1 = visual.TextBox2(
     win, text='Select the chemical you have seen before', font='Trebuchet MS',
     pos=(-0.71, -0.26),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp2_resp1',
     autoLog=False,
)
comp2_resp3 = visual.TextBox2(
     win, text='Rate how beautiful the chemicals presented are', font='Trebuchet MS',
     pos=(-0.71, -0.32),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp2_resp3',
     autoLog=False,
)
comp2_mouse = event.Mouse(win=win)
x, y = [None, None]
comp2_mouse.mouseClock = core.Clock()
check2 = visual.ImageStim(
    win=win,
    name='check2', 
    image='instructions/check2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.45, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "test1_nosubtle_choice" ---
blank_test1_nosubtle = visual.TextStim(win=win, name='blank_test1_nosubtle',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
target_test1_nosubtle = visual.ImageStim(
    win=win,
    name='target_test1_nosubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
distractor_test1_nosubtle = visual.ImageStim(
    win=win,
    name='distractor_test1_nosubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
mouse_test1_nosubtle = event.Mouse(win=win)
x, y = [None, None]
mouse_test1_nosubtle.mouseClock = core.Clock()

# --- Initialize components for Routine "test1_nosubtle_rate" ---
slider_text_test1_nosubtle = visual.TextStim(win=win, name='slider_text_test1_nosubtle',
    text='How confident are you of your response?',
    font='Trebuchet MS',
    pos=(0, -0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_test1_nosubtle = visual.Slider(win=win, name='slider_test1_nosubtle',
    startValue=5.5, size=(0.5, 0.025), pos=(0, -0.2), units=None,
    labels=["I am guessing", "I am certain"], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.5,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Trebuchet MS', labelHeight=0.028,
    flip=False, ori=0.0, depth=-1, readOnly=False)
slider_target_test1_nosubtle = visual.ImageStim(
    win=win,
    name='slider_target_test1_nosubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
slider_distractor_test1_nosubtle = visual.ImageStim(
    win=win,
    name='slider_distractor_test1_nosubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
continue_rate_test1_nosubtle = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='continue_rate_test1_nosubtle',
     autoLog=False,
)
mouse_continue_test1_nosubtle = event.Mouse(win=win)
x, y = [None, None]
mouse_continue_test1_nosubtle.mouseClock = core.Clock()

# --- Initialize components for Routine "test2_nosubtle_inst" ---
cont_test2_nosubtle = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='cont_test2_nosubtle',
     autoLog=False,
)
cont_mouse_test2_nosubtle = event.Mouse(win=win)
x, y = [None, None]
cont_mouse_test2_nosubtle.mouseClock = core.Clock()
instructions_test2_nosubtle = visual.ImageStim(
    win=win,
    name='instructions_test2_nosubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.4, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "comprehension3" ---
comp3_resp2 = visual.TextBox2(
     win, text='Click on the mutant that would result of each chemicals combination', font='Trebuchet MS',
     pos=(-0.71, -0.2),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp3_resp2',
     autoLog=False,
)
comp3_resp1 = visual.TextBox2(
     win, text='Select the chemical you have seen in Task 1', font='Trebuchet MS',
     pos=(-0.71, -0.26),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp3_resp1',
     autoLog=False,
)
comp3_resp3 = visual.TextBox2(
     win, text='Rate how beautiful the chemicals presented are', font='Trebuchet MS',
     pos=(-0.71, -0.32),     letterHeight=0.035,
     size=(1.5, 0.05), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center-left',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='comp3_resp3',
     autoLog=False,
)
comp3_mouse = event.Mouse(win=win)
x, y = [None, None]
comp3_mouse.mouseClock = core.Clock()
check3 = visual.ImageStim(
    win=win,
    name='check3', 
    image='instructions/check3.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.45, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "test2_nosubtle_choice" ---
blank_test2_nosubtle = visual.TextStim(win=win, name='blank_test2_nosubtle',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
target_test2_nosubtle = visual.ImageStim(
    win=win,
    name='target_test2_nosubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
distractor_test2_nosubtle = visual.ImageStim(
    win=win,
    name='distractor_test2_nosubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
mouse_test2_nosubtle = event.Mouse(win=win)
x, y = [None, None]
mouse_test2_nosubtle.mouseClock = core.Clock()

# --- Initialize components for Routine "test2_nosubtle_rate" ---
slider_text_test2_nosubtle = visual.TextStim(win=win, name='slider_text_test2_nosubtle',
    text='How confident are you of your response?',
    font='Trebuchet MS',
    pos=(0, -0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_test2_nosubtle = visual.Slider(win=win, name='slider_test2_nosubtle',
    startValue=5.5, size=(0.5, 0.025), pos=(0, -0.2), units=None,
    labels=["I am guessing", "I am certain"], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.5,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='white', markerColor='Red', lineColor='white', colorSpace='rgb',
    font='Trebuchet MS', labelHeight=0.028,
    flip=False, ori=0.0, depth=-1, readOnly=False)
slider_target_test2_nosubtle = visual.ImageStim(
    win=win,
    name='slider_target_test2_nosubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
slider_distractor_test2_nosubtle = visual.ImageStim(
    win=win,
    name='slider_distractor_test2_nosubtle', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
continue_rate_test2_nosubtle = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='continue_rate_test2_nosubtle',
     autoLog=False,
)
mouse_continue_test2_nosubtle = event.Mouse(win=win)
x, y = [None, None]
mouse_continue_test2_nosubtle.mouseClock = core.Clock()

# --- Initialize components for Routine "debrief" ---
cont_debrief = visual.TextBox2(
     win, text='CONTINUE', font='Trebuchet MS',
     pos=(0, -0.45),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='cont_debrief',
     autoLog=False,
)
cont_debrief_mouse = event.Mouse(win=win)
x, y = [None, None]
cont_debrief_mouse.mouseClock = core.Clock()
debrief_image = visual.ImageStim(
    win=win,
    name='debrief_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.4, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "no_comprehension" ---
no_compr_textbox = visual.TextBox2(
     win, text="You did not pass the comprehension check.\nPlease, click the button below to leave the experiment and return the experiment clicking 'Stop Without Completing' on Prolific.", font='Trebuchet MS',
     pos=(0, 0),     letterHeight=0.03,
     size=(0.65, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='no_compr_textbox',
     autoLog=False,
)
exit_box_no_compr = visual.TextBox2(
     win, text='EXIT', font='Trebuchet MS',
     pos=(0, -0.4),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='exit_box_no_compr',
     autoLog=False,
)
mouse_exit_no_compr = event.Mouse(win=win)
x, y = [None, None]
mouse_exit_no_compr.mouseClock = core.Clock()

# --- Initialize components for Routine "no_consent_trial" ---
no_consent_textbox = visual.TextBox2(
     win, text='Thank you for considering our study. You did not consent to participate.', font='Trebuchet MS',
     pos=(0, 0),     letterHeight=0.03,
     size=(0.65, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='no_consent_textbox',
     autoLog=False,
)
exit_box = visual.TextBox2(
     win, text='EXIT', font='Trebuchet MS',
     pos=(0, -0.4),     letterHeight=0.03,
     size=(0.2, 0.065), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='darkgrey', borderColor='white',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='exit_box',
     autoLog=False,
)
mouse_exit = event.Mouse(win=win)
x, y = [None, None]
mouse_exit.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "counterbalance" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
counterbalanceComponents = []
for thisComponent in counterbalanceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "counterbalance" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in counterbalanceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "counterbalance" ---
for thisComponent in counterbalanceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "counterbalance" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
information_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('info.xlsx'),
    seed=None, name='information_loop')
thisExp.addLoop(information_loop)  # add the loop to the experiment
thisInformation_loop = information_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInformation_loop.rgb)
if thisInformation_loop != None:
    for paramName in thisInformation_loop:
        exec('{} = thisInformation_loop[paramName]'.format(paramName))

for thisInformation_loop in information_loop:
    currentLoop = information_loop
    # abbreviate parameter names if possible (e.g. rgb = thisInformation_loop.rgb)
    if thisInformation_loop != None:
        for paramName in thisInformation_loop:
            exec('{} = thisInformation_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "information" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    continue_info.reset()
    # setup some python lists for storing info about the mouse_info
    mouse_info.clicked_name = []
    gotValidClick = False  # until a click is received
    image_info.setImage(information)
    # keep track of which components have finished
    informationComponents = [continue_info, mouse_info, image_info]
    for thisComponent in informationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "information" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *continue_info* updates
        if continue_info.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            continue_info.frameNStart = frameN  # exact frame index
            continue_info.tStart = t  # local t and not account for scr refresh
            continue_info.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_info, 'tStartRefresh')  # time at next scr refresh
            continue_info.setAutoDraw(True)
        # *mouse_info* updates
        if mouse_info.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_info.frameNStart = frameN  # exact frame index
            mouse_info.tStart = t  # local t and not account for scr refresh
            mouse_info.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_info, 'tStartRefresh')  # time at next scr refresh
            mouse_info.status = STARTED
            mouse_info.mouseClock.reset()
            prevButtonState = mouse_info.getPressed()  # if button is down already this ISN'T a new click
        if mouse_info.status == STARTED:  # only update if started and not finished!
            buttons = mouse_info.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(continue_info)
                        clickableList = continue_info
                    except:
                        clickableList = [continue_info]
                    for obj in clickableList:
                        if obj.contains(mouse_info):
                            gotValidClick = True
                            mouse_info.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *image_info* updates
        if image_info.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_info.frameNStart = frameN  # exact frame index
            image_info.tStart = t  # local t and not account for scr refresh
            image_info.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_info, 'tStartRefresh')  # time at next scr refresh
            image_info.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in informationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "information" ---
    for thisComponent in informationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for information_loop (TrialHandler)
    # the Routine "information" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'information_loop'


# --- Prepare to start Routine "consent" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
c1.reset()
c2.reset()
c3.reset()
c4.reset()
c5.reset()
c6.reset()
slider_1.reset()
slider_2.reset()
slider_3.reset()
slider_4.reset()
slider_5.reset()
slider_6.reset()
# Run 'Begin Routine' code from show_consent_code
show_consent = False
# setup some python lists for storing info about the mouse_consent
mouse_consent.clicked_name = []
gotValidClick = False  # until a click is received
consent_box.reset()
# Run 'Begin Routine' code from consent_code
consent = 0
# keep track of which components have finished
consentComponents = [c1, c2, c3, c4, c5, c6, slider_1, slider_2, slider_3, slider_4, slider_5, slider_6, mouse_consent, consent_box]
for thisComponent in consentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "consent" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *c1* updates
    if c1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        c1.frameNStart = frameN  # exact frame index
        c1.tStart = t  # local t and not account for scr refresh
        c1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(c1, 'tStartRefresh')  # time at next scr refresh
        c1.setAutoDraw(True)
    
    # *c2* updates
    if c2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        c2.frameNStart = frameN  # exact frame index
        c2.tStart = t  # local t and not account for scr refresh
        c2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(c2, 'tStartRefresh')  # time at next scr refresh
        c2.setAutoDraw(True)
    
    # *c3* updates
    if c3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        c3.frameNStart = frameN  # exact frame index
        c3.tStart = t  # local t and not account for scr refresh
        c3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(c3, 'tStartRefresh')  # time at next scr refresh
        c3.setAutoDraw(True)
    
    # *c4* updates
    if c4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        c4.frameNStart = frameN  # exact frame index
        c4.tStart = t  # local t and not account for scr refresh
        c4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(c4, 'tStartRefresh')  # time at next scr refresh
        c4.setAutoDraw(True)
    
    # *c5* updates
    if c5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        c5.frameNStart = frameN  # exact frame index
        c5.tStart = t  # local t and not account for scr refresh
        c5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(c5, 'tStartRefresh')  # time at next scr refresh
        c5.setAutoDraw(True)
    
    # *c6* updates
    if c6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        c6.frameNStart = frameN  # exact frame index
        c6.tStart = t  # local t and not account for scr refresh
        c6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(c6, 'tStartRefresh')  # time at next scr refresh
        c6.setAutoDraw(True)
    
    # *slider_1* updates
    if slider_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        slider_1.frameNStart = frameN  # exact frame index
        slider_1.tStart = t  # local t and not account for scr refresh
        slider_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
        slider_1.setAutoDraw(True)
    
    # *slider_2* updates
    if slider_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        slider_2.frameNStart = frameN  # exact frame index
        slider_2.tStart = t  # local t and not account for scr refresh
        slider_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
        slider_2.setAutoDraw(True)
    
    # *slider_3* updates
    if slider_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        slider_3.frameNStart = frameN  # exact frame index
        slider_3.tStart = t  # local t and not account for scr refresh
        slider_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_3, 'tStartRefresh')  # time at next scr refresh
        slider_3.setAutoDraw(True)
    
    # *slider_4* updates
    if slider_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        slider_4.frameNStart = frameN  # exact frame index
        slider_4.tStart = t  # local t and not account for scr refresh
        slider_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_4, 'tStartRefresh')  # time at next scr refresh
        slider_4.setAutoDraw(True)
    
    # *slider_5* updates
    if slider_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        slider_5.frameNStart = frameN  # exact frame index
        slider_5.tStart = t  # local t and not account for scr refresh
        slider_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_5, 'tStartRefresh')  # time at next scr refresh
        slider_5.setAutoDraw(True)
    
    # *slider_6* updates
    if slider_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        slider_6.frameNStart = frameN  # exact frame index
        slider_6.tStart = t  # local t and not account for scr refresh
        slider_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_6, 'tStartRefresh')  # time at next scr refresh
        slider_6.setAutoDraw(True)
    # Run 'Each Frame' code from show_consent_code
    s1 = slider_1.getRating()
    s2 = slider_2.getRating()
    s3 = slider_3.getRating()
    s4 = slider_4.getRating()
    s5 = slider_5.getRating()
    s6 = slider_6.getRating()
    
    if s1 is not None:
        if s2 is not None:
            if s3 is not None:
                if s4 is not None:
                    if s5 is not None:
                        if s6 is not None:
                            show_consent = True
                
                
    
    # *mouse_consent* updates
    if mouse_consent.status == NOT_STARTED and show_consent:
        # keep track of start time/frame for later
        mouse_consent.frameNStart = frameN  # exact frame index
        mouse_consent.tStart = t  # local t and not account for scr refresh
        mouse_consent.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_consent, 'tStartRefresh')  # time at next scr refresh
        mouse_consent.status = STARTED
        mouse_consent.mouseClock.reset()
        prevButtonState = mouse_consent.getPressed()  # if button is down already this ISN'T a new click
    if mouse_consent.status == STARTED:  # only update if started and not finished!
        buttons = mouse_consent.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(consent_box)
                    clickableList = consent_box
                except:
                    clickableList = [consent_box]
                for obj in clickableList:
                    if obj.contains(mouse_consent):
                        gotValidClick = True
                        mouse_consent.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *consent_box* updates
    if consent_box.status == NOT_STARTED and show_consent:
        # keep track of start time/frame for later
        consent_box.frameNStart = frameN  # exact frame index
        consent_box.tStart = t  # local t and not account for scr refresh
        consent_box.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consent_box, 'tStartRefresh')  # time at next scr refresh
        consent_box.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "consent" ---
for thisComponent in consentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider_1.response', slider_1.getRating())
thisExp.addData('slider_2.response', slider_2.getRating())
thisExp.addData('slider_3.response', slider_3.getRating())
thisExp.addData('slider_4.response', slider_4.getRating())
thisExp.addData('slider_5.response', slider_5.getRating())
thisExp.addData('slider_6.response', slider_6.getRating())
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# Run 'End Routine' code from consent_code
res1 = slider_1.getRating()
res2 = slider_2.getRating()
res3 = slider_3.getRating()
res4 = slider_4.getRating()
res5 = slider_5.getRating()
res6 = slider_6.getRating()

if res1 == 1:
    if res2 == 1:
        if res3 == 1:
            if res4 == 1:
                if res5 == 1:
                    if res6 == 1:
                        consent = 1
                        no_consent = 0
                    else:
                        consent = 0
                        no_consent = 1
                else:
                    consent = 0
                    no_consent = 1
            else:
                consent = 0
                no_consent = 1
        else:
            consent = 0
            no_consent = 1
    else:
        consent = 0
        no_consent = 1
else:
    consent = 0
    no_consent = 1
# the Routine "consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
consent_loop = data.TrialHandler(nReps=consent, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='consent_loop')
thisExp.addLoop(consent_loop)  # add the loop to the experiment
thisConsent_loop = consent_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisConsent_loop.rgb)
if thisConsent_loop != None:
    for paramName in thisConsent_loop:
        exec('{} = thisConsent_loop[paramName]'.format(paramName))

for thisConsent_loop in consent_loop:
    currentLoop = consent_loop
    # abbreviate parameter names if possible (e.g. rgb = thisConsent_loop.rgb)
    if thisConsent_loop != None:
        for paramName in thisConsent_loop:
            exec('{} = thisConsent_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    task1_instr = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('task1_instructions.xlsx'),
        seed=None, name='task1_instr')
    thisExp.addLoop(task1_instr)  # add the loop to the experiment
    thisTask1_instr = task1_instr.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTask1_instr.rgb)
    if thisTask1_instr != None:
        for paramName in thisTask1_instr:
            exec('{} = thisTask1_instr[paramName]'.format(paramName))
    
    for thisTask1_instr in task1_instr:
        currentLoop = task1_instr
        # abbreviate parameter names if possible (e.g. rgb = thisTask1_instr.rgb)
        if thisTask1_instr != None:
            for paramName in thisTask1_instr:
                exec('{} = thisTask1_instr[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "instructions_1" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        cont_train_instr.reset()
        # setup some python lists for storing info about the cont_train_instr_mouse
        cont_train_instr_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        train_instructions.setImage(task1)
        # keep track of which components have finished
        instructions_1Components = [cont_train_instr, cont_train_instr_mouse, train_instructions]
        for thisComponent in instructions_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "instructions_1" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cont_train_instr* updates
            if cont_train_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cont_train_instr.frameNStart = frameN  # exact frame index
                cont_train_instr.tStart = t  # local t and not account for scr refresh
                cont_train_instr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cont_train_instr, 'tStartRefresh')  # time at next scr refresh
                cont_train_instr.setAutoDraw(True)
            # *cont_train_instr_mouse* updates
            if cont_train_instr_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cont_train_instr_mouse.frameNStart = frameN  # exact frame index
                cont_train_instr_mouse.tStart = t  # local t and not account for scr refresh
                cont_train_instr_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cont_train_instr_mouse, 'tStartRefresh')  # time at next scr refresh
                cont_train_instr_mouse.status = STARTED
                cont_train_instr_mouse.mouseClock.reset()
                prevButtonState = cont_train_instr_mouse.getPressed()  # if button is down already this ISN'T a new click
            if cont_train_instr_mouse.status == STARTED:  # only update if started and not finished!
                buttons = cont_train_instr_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(cont_train_instr)
                            clickableList = cont_train_instr
                        except:
                            clickableList = [cont_train_instr]
                        for obj in clickableList:
                            if obj.contains(cont_train_instr_mouse):
                                gotValidClick = True
                                cont_train_instr_mouse.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # *train_instructions* updates
            if train_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                train_instructions.frameNStart = frameN  # exact frame index
                train_instructions.tStart = t  # local t and not account for scr refresh
                train_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(train_instructions, 'tStartRefresh')  # time at next scr refresh
                train_instructions.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instructions_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "instructions_1" ---
        for thisComponent in instructions_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for task1_instr (TrialHandler)
        # the Routine "instructions_1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'task1_instr'
    
    
    # --- Prepare to start Routine "comprehension1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    comp1_resp1.reset()
    comp1_resp2.reset()
    comp1_resp3.reset()
    # setup some python lists for storing info about the comp1_mouse
    comp1_mouse.x = []
    comp1_mouse.y = []
    comp1_mouse.leftButton = []
    comp1_mouse.midButton = []
    comp1_mouse.rightButton = []
    comp1_mouse.time = []
    comp1_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    comp1_mouse.mouseClock.reset()
    # keep track of which components have finished
    comprehension1Components = [comp1_resp1, comp1_resp2, comp1_resp3, comp1_mouse, check1]
    for thisComponent in comprehension1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "comprehension1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *comp1_resp1* updates
        if comp1_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            comp1_resp1.frameNStart = frameN  # exact frame index
            comp1_resp1.tStart = t  # local t and not account for scr refresh
            comp1_resp1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comp1_resp1, 'tStartRefresh')  # time at next scr refresh
            comp1_resp1.setAutoDraw(True)
        
        # *comp1_resp2* updates
        if comp1_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            comp1_resp2.frameNStart = frameN  # exact frame index
            comp1_resp2.tStart = t  # local t and not account for scr refresh
            comp1_resp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comp1_resp2, 'tStartRefresh')  # time at next scr refresh
            comp1_resp2.setAutoDraw(True)
        
        # *comp1_resp3* updates
        if comp1_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            comp1_resp3.frameNStart = frameN  # exact frame index
            comp1_resp3.tStart = t  # local t and not account for scr refresh
            comp1_resp3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comp1_resp3, 'tStartRefresh')  # time at next scr refresh
            comp1_resp3.setAutoDraw(True)
        # *comp1_mouse* updates
        if comp1_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            comp1_mouse.frameNStart = frameN  # exact frame index
            comp1_mouse.tStart = t  # local t and not account for scr refresh
            comp1_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(comp1_mouse, 'tStartRefresh')  # time at next scr refresh
            comp1_mouse.status = STARTED
            prevButtonState = comp1_mouse.getPressed()  # if button is down already this ISN'T a new click
        if comp1_mouse.status == STARTED:  # only update if started and not finished!
            buttons = comp1_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([comp1_resp1, comp1_resp2, comp1_resp3])
                        clickableList = [comp1_resp1, comp1_resp2, comp1_resp3]
                    except:
                        clickableList = [[comp1_resp1, comp1_resp2, comp1_resp3]]
                    for obj in clickableList:
                        if obj.contains(comp1_mouse):
                            gotValidClick = True
                            comp1_mouse.clicked_name.append(obj.name)
                    x, y = comp1_mouse.getPos()
                    comp1_mouse.x.append(x)
                    comp1_mouse.y.append(y)
                    buttons = comp1_mouse.getPressed()
                    comp1_mouse.leftButton.append(buttons[0])
                    comp1_mouse.midButton.append(buttons[1])
                    comp1_mouse.rightButton.append(buttons[2])
                    comp1_mouse.time.append(comp1_mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # *check1* updates
        if check1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            check1.frameNStart = frameN  # exact frame index
            check1.tStart = t  # local t and not account for scr refresh
            check1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(check1, 'tStartRefresh')  # time at next scr refresh
            check1.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in comprehension1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "comprehension1" ---
    for thisComponent in comprehension1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from comprehension_code
    if comp1_mouse.clicked_name[0] == 'comp1_resp1':
        try_again = 0
        compr1_continue = 1
        no_compr = 0
    else:
        try_again = 1
    # store data for consent_loop (TrialHandler)
    consent_loop.addData('comp1_mouse.x', comp1_mouse.x)
    consent_loop.addData('comp1_mouse.y', comp1_mouse.y)
    consent_loop.addData('comp1_mouse.leftButton', comp1_mouse.leftButton)
    consent_loop.addData('comp1_mouse.midButton', comp1_mouse.midButton)
    consent_loop.addData('comp1_mouse.rightButton', comp1_mouse.rightButton)
    consent_loop.addData('comp1_mouse.time', comp1_mouse.time)
    consent_loop.addData('comp1_mouse.clicked_name', comp1_mouse.clicked_name)
    # the Routine "comprehension1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    comp1_loop = data.TrialHandler(nReps=try_again, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='comp1_loop')
    thisExp.addLoop(comp1_loop)  # add the loop to the experiment
    thisComp1_loop = comp1_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisComp1_loop.rgb)
    if thisComp1_loop != None:
        for paramName in thisComp1_loop:
            exec('{} = thisComp1_loop[paramName]'.format(paramName))
    
    for thisComp1_loop in comp1_loop:
        currentLoop = comp1_loop
        # abbreviate parameter names if possible (e.g. rgb = thisComp1_loop.rgb)
        if thisComp1_loop != None:
            for paramName in thisComp1_loop:
                exec('{} = thisComp1_loop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        task1_instr_again = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('task1_instructions.xlsx'),
            seed=None, name='task1_instr_again')
        thisExp.addLoop(task1_instr_again)  # add the loop to the experiment
        thisTask1_instr_again = task1_instr_again.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTask1_instr_again.rgb)
        if thisTask1_instr_again != None:
            for paramName in thisTask1_instr_again:
                exec('{} = thisTask1_instr_again[paramName]'.format(paramName))
        
        for thisTask1_instr_again in task1_instr_again:
            currentLoop = task1_instr_again
            # abbreviate parameter names if possible (e.g. rgb = thisTask1_instr_again.rgb)
            if thisTask1_instr_again != None:
                for paramName in thisTask1_instr_again:
                    exec('{} = thisTask1_instr_again[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "instructions_1" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            cont_train_instr.reset()
            # setup some python lists for storing info about the cont_train_instr_mouse
            cont_train_instr_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            train_instructions.setImage(task1)
            # keep track of which components have finished
            instructions_1Components = [cont_train_instr, cont_train_instr_mouse, train_instructions]
            for thisComponent in instructions_1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "instructions_1" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *cont_train_instr* updates
                if cont_train_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cont_train_instr.frameNStart = frameN  # exact frame index
                    cont_train_instr.tStart = t  # local t and not account for scr refresh
                    cont_train_instr.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cont_train_instr, 'tStartRefresh')  # time at next scr refresh
                    cont_train_instr.setAutoDraw(True)
                # *cont_train_instr_mouse* updates
                if cont_train_instr_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cont_train_instr_mouse.frameNStart = frameN  # exact frame index
                    cont_train_instr_mouse.tStart = t  # local t and not account for scr refresh
                    cont_train_instr_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cont_train_instr_mouse, 'tStartRefresh')  # time at next scr refresh
                    cont_train_instr_mouse.status = STARTED
                    cont_train_instr_mouse.mouseClock.reset()
                    prevButtonState = cont_train_instr_mouse.getPressed()  # if button is down already this ISN'T a new click
                if cont_train_instr_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = cont_train_instr_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter(cont_train_instr)
                                clickableList = cont_train_instr
                            except:
                                clickableList = [cont_train_instr]
                            for obj in clickableList:
                                if obj.contains(cont_train_instr_mouse):
                                    gotValidClick = True
                                    cont_train_instr_mouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                
                # *train_instructions* updates
                if train_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    train_instructions.frameNStart = frameN  # exact frame index
                    train_instructions.tStart = t  # local t and not account for scr refresh
                    train_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(train_instructions, 'tStartRefresh')  # time at next scr refresh
                    train_instructions.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in instructions_1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "instructions_1" ---
            for thisComponent in instructions_1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for task1_instr_again (TrialHandler)
            # the Routine "instructions_1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'task1_instr_again'
        
        
        # --- Prepare to start Routine "comprehension1_2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        comp1_resp1_2.reset()
        comp1_resp2_2.reset()
        comp1_resp3_2.reset()
        # setup some python lists for storing info about the comp1_mouse_2
        comp1_mouse_2.x = []
        comp1_mouse_2.y = []
        comp1_mouse_2.leftButton = []
        comp1_mouse_2.midButton = []
        comp1_mouse_2.rightButton = []
        comp1_mouse_2.time = []
        comp1_mouse_2.clicked_name = []
        gotValidClick = False  # until a click is received
        comp1_mouse_2.mouseClock.reset()
        # keep track of which components have finished
        comprehension1_2Components = [comp1_resp1_2, comp1_resp2_2, comp1_resp3_2, comp1_mouse_2, check1_2]
        for thisComponent in comprehension1_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "comprehension1_2" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *comp1_resp1_2* updates
            if comp1_resp1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                comp1_resp1_2.frameNStart = frameN  # exact frame index
                comp1_resp1_2.tStart = t  # local t and not account for scr refresh
                comp1_resp1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(comp1_resp1_2, 'tStartRefresh')  # time at next scr refresh
                comp1_resp1_2.setAutoDraw(True)
            
            # *comp1_resp2_2* updates
            if comp1_resp2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                comp1_resp2_2.frameNStart = frameN  # exact frame index
                comp1_resp2_2.tStart = t  # local t and not account for scr refresh
                comp1_resp2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(comp1_resp2_2, 'tStartRefresh')  # time at next scr refresh
                comp1_resp2_2.setAutoDraw(True)
            
            # *comp1_resp3_2* updates
            if comp1_resp3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                comp1_resp3_2.frameNStart = frameN  # exact frame index
                comp1_resp3_2.tStart = t  # local t and not account for scr refresh
                comp1_resp3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(comp1_resp3_2, 'tStartRefresh')  # time at next scr refresh
                comp1_resp3_2.setAutoDraw(True)
            # *comp1_mouse_2* updates
            if comp1_mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                comp1_mouse_2.frameNStart = frameN  # exact frame index
                comp1_mouse_2.tStart = t  # local t and not account for scr refresh
                comp1_mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(comp1_mouse_2, 'tStartRefresh')  # time at next scr refresh
                comp1_mouse_2.status = STARTED
                prevButtonState = comp1_mouse_2.getPressed()  # if button is down already this ISN'T a new click
            if comp1_mouse_2.status == STARTED:  # only update if started and not finished!
                buttons = comp1_mouse_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([comp1_resp1_2, comp1_resp2_2, comp1_resp3_2])
                            clickableList = [comp1_resp1_2, comp1_resp2_2, comp1_resp3_2]
                        except:
                            clickableList = [[comp1_resp1_2, comp1_resp2_2, comp1_resp3_2]]
                        for obj in clickableList:
                            if obj.contains(comp1_mouse_2):
                                gotValidClick = True
                                comp1_mouse_2.clicked_name.append(obj.name)
                        x, y = comp1_mouse_2.getPos()
                        comp1_mouse_2.x.append(x)
                        comp1_mouse_2.y.append(y)
                        buttons = comp1_mouse_2.getPressed()
                        comp1_mouse_2.leftButton.append(buttons[0])
                        comp1_mouse_2.midButton.append(buttons[1])
                        comp1_mouse_2.rightButton.append(buttons[2])
                        comp1_mouse_2.time.append(comp1_mouse_2.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # abort routine on response
            
            # *check1_2* updates
            if check1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                check1_2.frameNStart = frameN  # exact frame index
                check1_2.tStart = t  # local t and not account for scr refresh
                check1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(check1_2, 'tStartRefresh')  # time at next scr refresh
                check1_2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in comprehension1_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "comprehension1_2" ---
        for thisComponent in comprehension1_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from comprehension_code_2
        if comp1_mouse_2.clicked_name[0] == 'comp1_resp1_2':
            compr1_continue = 1
            no_compr = 0
        else:
            compr1_continue = 0
            no_compr = 1
        # store data for comp1_loop (TrialHandler)
        comp1_loop.addData('comp1_mouse_2.x', comp1_mouse_2.x)
        comp1_loop.addData('comp1_mouse_2.y', comp1_mouse_2.y)
        comp1_loop.addData('comp1_mouse_2.leftButton', comp1_mouse_2.leftButton)
        comp1_loop.addData('comp1_mouse_2.midButton', comp1_mouse_2.midButton)
        comp1_loop.addData('comp1_mouse_2.rightButton', comp1_mouse_2.rightButton)
        comp1_loop.addData('comp1_mouse_2.time', comp1_mouse_2.time)
        comp1_loop.addData('comp1_mouse_2.clicked_name', comp1_mouse_2.clicked_name)
        # the Routine "comprehension1_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed try_again repeats of 'comp1_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    compr1_completed = data.TrialHandler(nReps=compr1_continue, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='compr1_completed')
    thisExp.addLoop(compr1_completed)  # add the loop to the experiment
    thisCompr1_completed = compr1_completed.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCompr1_completed.rgb)
    if thisCompr1_completed != None:
        for paramName in thisCompr1_completed:
            exec('{} = thisCompr1_completed[paramName]'.format(paramName))
    
    for thisCompr1_completed in compr1_completed:
        currentLoop = compr1_completed
        # abbreviate parameter names if possible (e.g. rgb = thisCompr1_completed.rgb)
        if thisCompr1_completed != None:
            for paramName in thisCompr1_completed:
                exec('{} = thisCompr1_completed[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        training_trials = data.TrialHandler(nReps=4.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('training.xlsx'),
            seed=None, name='training_trials')
        thisExp.addLoop(training_trials)  # add the loop to the experiment
        thisTraining_trial = training_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTraining_trial.rgb)
        if thisTraining_trial != None:
            for paramName in thisTraining_trial:
                exec('{} = thisTraining_trial[paramName]'.format(paramName))
        
        for thisTraining_trial in training_trials:
            currentLoop = training_trials
            # abbreviate parameter names if possible (e.g. rgb = thisTraining_trial.rgb)
            if thisTraining_trial != None:
                for paramName in thisTraining_trial:
                    exec('{} = thisTraining_trial[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "cue_o__trial" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from cue_random
            if cue1 == 1:
                stim1 = reorder_cues[0]
            elif cue1 == 2:
                stim1 = reorder_cues[1]
            
            if cue2 == 5:
                stim2 = reorder_cues[4]
            elif cue2 == 6:
                stim2 = reorder_cues[5]
            # Run 'Begin Routine' code from position
            left_cue_pos = (-0.3, 0.2)
            right_cue_pos = (0.3, 0.2)
            left_out_pos = (-0.125, -0.2)
            right_out_pos = (0.125, -0.2)
            cue_positions = [left_cue_pos, right_cue_pos]
            out_positions = [left_out_pos, right_out_pos]
            shuffle(cue_positions)
            shuffle(out_positions)
            predictive_cue.setPos([cue_positions[0]])
            predictive_cue.setImage(stim1)
            non_predictive_cue.setPos([cue_positions[1]])
            non_predictive_cue.setImage(stim2)
            o1_image.setPos([out_positions[0]])
            o1_image.setImage('stimuli/out1.png')
            o2_image.setPos([out_positions[1]])
            o2_image.setImage('stimuli/out2.png')
            # setup some python lists for storing info about the cue_o_mouse
            cue_o_mouse.x = []
            cue_o_mouse.y = []
            cue_o_mouse.leftButton = []
            cue_o_mouse.midButton = []
            cue_o_mouse.rightButton = []
            cue_o_mouse.time = []
            cue_o_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            # Run 'Begin Routine' code from correct_click
            msg = '888'
            correct = 99
            # keep track of which components have finished
            cue_o__trialComponents = [blank_training, predictive_cue, non_predictive_cue, o1_image, o2_image, cue_o_mouse, timeout_text]
            for thisComponent in cue_o__trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "cue_o__trial" ---
            while continueRoutine and routineTimer.getTime() < 11.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *blank_training* updates
                if blank_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blank_training.frameNStart = frameN  # exact frame index
                    blank_training.tStart = t  # local t and not account for scr refresh
                    blank_training.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blank_training, 'tStartRefresh')  # time at next scr refresh
                    blank_training.setAutoDraw(True)
                if blank_training.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > blank_training.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        blank_training.tStop = t  # not accounting for scr refresh
                        blank_training.frameNStop = frameN  # exact frame index
                        blank_training.setAutoDraw(False)
                
                # *predictive_cue* updates
                if predictive_cue.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    predictive_cue.frameNStart = frameN  # exact frame index
                    predictive_cue.tStart = t  # local t and not account for scr refresh
                    predictive_cue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(predictive_cue, 'tStartRefresh')  # time at next scr refresh
                    predictive_cue.setAutoDraw(True)
                if predictive_cue.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > predictive_cue.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        predictive_cue.tStop = t  # not accounting for scr refresh
                        predictive_cue.frameNStop = frameN  # exact frame index
                        predictive_cue.setAutoDraw(False)
                
                # *non_predictive_cue* updates
                if non_predictive_cue.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    non_predictive_cue.frameNStart = frameN  # exact frame index
                    non_predictive_cue.tStart = t  # local t and not account for scr refresh
                    non_predictive_cue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(non_predictive_cue, 'tStartRefresh')  # time at next scr refresh
                    non_predictive_cue.setAutoDraw(True)
                if non_predictive_cue.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > non_predictive_cue.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        non_predictive_cue.tStop = t  # not accounting for scr refresh
                        non_predictive_cue.frameNStop = frameN  # exact frame index
                        non_predictive_cue.setAutoDraw(False)
                
                # *o1_image* updates
                if o1_image.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    o1_image.frameNStart = frameN  # exact frame index
                    o1_image.tStart = t  # local t and not account for scr refresh
                    o1_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(o1_image, 'tStartRefresh')  # time at next scr refresh
                    o1_image.setAutoDraw(True)
                if o1_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > o1_image.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        o1_image.tStop = t  # not accounting for scr refresh
                        o1_image.frameNStop = frameN  # exact frame index
                        o1_image.setAutoDraw(False)
                
                # *o2_image* updates
                if o2_image.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    o2_image.frameNStart = frameN  # exact frame index
                    o2_image.tStart = t  # local t and not account for scr refresh
                    o2_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(o2_image, 'tStartRefresh')  # time at next scr refresh
                    o2_image.setAutoDraw(True)
                if o2_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > o2_image.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        o2_image.tStop = t  # not accounting for scr refresh
                        o2_image.frameNStop = frameN  # exact frame index
                        o2_image.setAutoDraw(False)
                # *cue_o_mouse* updates
                if cue_o_mouse.status == NOT_STARTED and t >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    cue_o_mouse.frameNStart = frameN  # exact frame index
                    cue_o_mouse.tStart = t  # local t and not account for scr refresh
                    cue_o_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cue_o_mouse, 'tStartRefresh')  # time at next scr refresh
                    cue_o_mouse.status = STARTED
                    cue_o_mouse.mouseClock.reset()
                    prevButtonState = cue_o_mouse.getPressed()  # if button is down already this ISN'T a new click
                if cue_o_mouse.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > cue_o_mouse.tStartRefresh + 10-frameTolerance:
                        # keep track of stop time/frame for later
                        cue_o_mouse.tStop = t  # not accounting for scr refresh
                        cue_o_mouse.frameNStop = frameN  # exact frame index
                        cue_o_mouse.status = FINISHED
                if cue_o_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = cue_o_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([o1_image, o2_image])
                                clickableList = [o1_image, o2_image]
                            except:
                                clickableList = [[o1_image, o2_image]]
                            for obj in clickableList:
                                if obj.contains(cue_o_mouse):
                                    gotValidClick = True
                                    cue_o_mouse.clicked_name.append(obj.name)
                            if gotValidClick:
                                x, y = cue_o_mouse.getPos()
                                cue_o_mouse.x.append(x)
                                cue_o_mouse.y.append(y)
                                buttons = cue_o_mouse.getPressed()
                                cue_o_mouse.leftButton.append(buttons[0])
                                cue_o_mouse.midButton.append(buttons[1])
                                cue_o_mouse.rightButton.append(buttons[2])
                                cue_o_mouse.time.append(cue_o_mouse.mouseClock.getTime())
                            if gotValidClick:
                                continueRoutine = False  # abort routine on response
                
                # *timeout_text* updates
                if timeout_text.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
                    # keep track of start time/frame for later
                    timeout_text.frameNStart = frameN  # exact frame index
                    timeout_text.tStart = t  # local t and not account for scr refresh
                    timeout_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(timeout_text, 'tStartRefresh')  # time at next scr refresh
                    timeout_text.setAutoDraw(True)
                if timeout_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > timeout_text.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        timeout_text.tStop = t  # not accounting for scr refresh
                        timeout_text.frameNStop = frameN  # exact frame index
                        timeout_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cue_o__trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "cue_o__trial" ---
            for thisComponent in cue_o__trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from cue_random
            thisExp.addData("order", order)
            # Run 'End Routine' code from position
            thisExp.addData ('cue_order', cue_positions)
            thisExp.addData ('out_order', out_positions)
            # store data for training_trials (TrialHandler)
            training_trials.addData('cue_o_mouse.x', cue_o_mouse.x)
            training_trials.addData('cue_o_mouse.y', cue_o_mouse.y)
            training_trials.addData('cue_o_mouse.leftButton', cue_o_mouse.leftButton)
            training_trials.addData('cue_o_mouse.midButton', cue_o_mouse.midButton)
            training_trials.addData('cue_o_mouse.rightButton', cue_o_mouse.rightButton)
            training_trials.addData('cue_o_mouse.time', cue_o_mouse.time)
            training_trials.addData('cue_o_mouse.clicked_name', cue_o_mouse.clicked_name)
            # Run 'End Routine' code from timeout_code
            if cue_o_mouse.isPressedIn(o1_image) or cue_o_mouse.isPressedIn(o2_image):
                feedback_reps = 1
            else:
                feedback_reps = 0
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-11.500000)
            
            # set up handler to look after randomisation of conditions etc
            feedback_loop = data.TrialHandler(nReps=feedback_reps, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='feedback_loop')
            thisExp.addLoop(feedback_loop)  # add the loop to the experiment
            thisFeedback_loop = feedback_loop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisFeedback_loop.rgb)
            if thisFeedback_loop != None:
                for paramName in thisFeedback_loop:
                    exec('{} = thisFeedback_loop[paramName]'.format(paramName))
            
            for thisFeedback_loop in feedback_loop:
                currentLoop = feedback_loop
                # abbreviate parameter names if possible (e.g. rgb = thisFeedback_loop.rgb)
                if thisFeedback_loop != None:
                    for paramName in thisFeedback_loop:
                        exec('{} = thisFeedback_loop[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "cue_selection" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                # Run 'Begin Routine' code from clicked_outcome
                if cue_o_mouse.clicked_name[0] == 'o1_image':
                    yellow_frame_position = out_positions[0]
                else:
                    yellow_frame_position = out_positions[1]
                if cue_o_mouse.clicked_name[0] == outcome:
                    correct = 1
                else:
                    correct = 0
                
                thisExp.addData('correct_answer', correct)
                predictive_cue_selection.setPos([cue_positions[0]])
                predictive_cue_selection.setImage(stim1)
                non_predictive_cue_selection.setPos([cue_positions[1]])
                non_predictive_cue_selection.setImage(stim2)
                o1_image_selection.setPos([out_positions[0]])
                o1_image_selection.setImage('stimuli/out1.png')
                o2_image_selection.setPos([out_positions[1]])
                o2_image_selection.setImage('stimuli/out2.png')
                yellow_frame.setPos(yellow_frame_position)
                # keep track of which components have finished
                cue_selectionComponents = [predictive_cue_selection, non_predictive_cue_selection, o1_image_selection, o2_image_selection, yellow_frame]
                for thisComponent in cue_selectionComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "cue_selection" ---
                while continueRoutine and routineTimer.getTime() < 0.5:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *predictive_cue_selection* updates
                    if predictive_cue_selection.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        predictive_cue_selection.frameNStart = frameN  # exact frame index
                        predictive_cue_selection.tStart = t  # local t and not account for scr refresh
                        predictive_cue_selection.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(predictive_cue_selection, 'tStartRefresh')  # time at next scr refresh
                        predictive_cue_selection.setAutoDraw(True)
                    if predictive_cue_selection.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > predictive_cue_selection.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            predictive_cue_selection.tStop = t  # not accounting for scr refresh
                            predictive_cue_selection.frameNStop = frameN  # exact frame index
                            predictive_cue_selection.setAutoDraw(False)
                    
                    # *non_predictive_cue_selection* updates
                    if non_predictive_cue_selection.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        non_predictive_cue_selection.frameNStart = frameN  # exact frame index
                        non_predictive_cue_selection.tStart = t  # local t and not account for scr refresh
                        non_predictive_cue_selection.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(non_predictive_cue_selection, 'tStartRefresh')  # time at next scr refresh
                        non_predictive_cue_selection.setAutoDraw(True)
                    if non_predictive_cue_selection.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > non_predictive_cue_selection.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            non_predictive_cue_selection.tStop = t  # not accounting for scr refresh
                            non_predictive_cue_selection.frameNStop = frameN  # exact frame index
                            non_predictive_cue_selection.setAutoDraw(False)
                    
                    # *o1_image_selection* updates
                    if o1_image_selection.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        o1_image_selection.frameNStart = frameN  # exact frame index
                        o1_image_selection.tStart = t  # local t and not account for scr refresh
                        o1_image_selection.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(o1_image_selection, 'tStartRefresh')  # time at next scr refresh
                        o1_image_selection.setAutoDraw(True)
                    if o1_image_selection.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > o1_image_selection.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            o1_image_selection.tStop = t  # not accounting for scr refresh
                            o1_image_selection.frameNStop = frameN  # exact frame index
                            o1_image_selection.setAutoDraw(False)
                    
                    # *o2_image_selection* updates
                    if o2_image_selection.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        o2_image_selection.frameNStart = frameN  # exact frame index
                        o2_image_selection.tStart = t  # local t and not account for scr refresh
                        o2_image_selection.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(o2_image_selection, 'tStartRefresh')  # time at next scr refresh
                        o2_image_selection.setAutoDraw(True)
                    if o2_image_selection.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > o2_image_selection.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            o2_image_selection.tStop = t  # not accounting for scr refresh
                            o2_image_selection.frameNStop = frameN  # exact frame index
                            o2_image_selection.setAutoDraw(False)
                    
                    # *yellow_frame* updates
                    if yellow_frame.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        yellow_frame.frameNStart = frameN  # exact frame index
                        yellow_frame.tStart = t  # local t and not account for scr refresh
                        yellow_frame.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(yellow_frame, 'tStartRefresh')  # time at next scr refresh
                        yellow_frame.setAutoDraw(True)
                    if yellow_frame.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > yellow_frame.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            yellow_frame.tStop = t  # not accounting for scr refresh
                            yellow_frame.frameNStop = frameN  # exact frame index
                            yellow_frame.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in cue_selectionComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "cue_selection" ---
                for thisComponent in cue_selectionComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-0.500000)
                
                # --- Prepare to start Routine "feedback" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                # Run 'Begin Routine' code from feedback_code
                if correct == 1:
                    msg = 'CORRECT!' 
                    msg_color = [-1.0000, 1.0000, -1.0000]
                else:
                    msg = 'INCORRECT!'
                    msg_color = 'red'   #[1.0000, -1.0000, -1.0000]
                feedback_text.setColor(msg_color, colorSpace='rgb')
                feedback_text.setText(msg)
                predictive_cue_feedback.setPos([cue_positions[0]])
                predictive_cue_feedback.setImage(stim1)
                non_predictive_cue_feedback.setPos([cue_positions[1]])
                non_predictive_cue_feedback.setImage(stim2)
                o1_image_feedback.setPos([out_positions[0]])
                o1_image_feedback.setImage(o1_feedback)
                o2_image_feedback.setPos([out_positions[1]])
                o2_image_feedback.setImage(o2_feedback)
                # keep track of which components have finished
                feedbackComponents = [feedback_text, predictive_cue_feedback, non_predictive_cue_feedback, o1_image_feedback, o2_image_feedback]
                for thisComponent in feedbackComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "feedback" ---
                while continueRoutine and routineTimer.getTime() < 2.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *feedback_text* updates
                    if feedback_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        feedback_text.frameNStart = frameN  # exact frame index
                        feedback_text.tStart = t  # local t and not account for scr refresh
                        feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                        feedback_text.setAutoDraw(True)
                    if feedback_text.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > feedback_text.tStartRefresh + 2-frameTolerance:
                            # keep track of stop time/frame for later
                            feedback_text.tStop = t  # not accounting for scr refresh
                            feedback_text.frameNStop = frameN  # exact frame index
                            feedback_text.setAutoDraw(False)
                    
                    # *predictive_cue_feedback* updates
                    if predictive_cue_feedback.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        predictive_cue_feedback.frameNStart = frameN  # exact frame index
                        predictive_cue_feedback.tStart = t  # local t and not account for scr refresh
                        predictive_cue_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(predictive_cue_feedback, 'tStartRefresh')  # time at next scr refresh
                        predictive_cue_feedback.setAutoDraw(True)
                    if predictive_cue_feedback.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > predictive_cue_feedback.tStartRefresh + 2-frameTolerance:
                            # keep track of stop time/frame for later
                            predictive_cue_feedback.tStop = t  # not accounting for scr refresh
                            predictive_cue_feedback.frameNStop = frameN  # exact frame index
                            predictive_cue_feedback.setAutoDraw(False)
                    
                    # *non_predictive_cue_feedback* updates
                    if non_predictive_cue_feedback.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        non_predictive_cue_feedback.frameNStart = frameN  # exact frame index
                        non_predictive_cue_feedback.tStart = t  # local t and not account for scr refresh
                        non_predictive_cue_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(non_predictive_cue_feedback, 'tStartRefresh')  # time at next scr refresh
                        non_predictive_cue_feedback.setAutoDraw(True)
                    if non_predictive_cue_feedback.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > non_predictive_cue_feedback.tStartRefresh + 2-frameTolerance:
                            # keep track of stop time/frame for later
                            non_predictive_cue_feedback.tStop = t  # not accounting for scr refresh
                            non_predictive_cue_feedback.frameNStop = frameN  # exact frame index
                            non_predictive_cue_feedback.setAutoDraw(False)
                    
                    # *o1_image_feedback* updates
                    if o1_image_feedback.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        o1_image_feedback.frameNStart = frameN  # exact frame index
                        o1_image_feedback.tStart = t  # local t and not account for scr refresh
                        o1_image_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(o1_image_feedback, 'tStartRefresh')  # time at next scr refresh
                        o1_image_feedback.setAutoDraw(True)
                    if o1_image_feedback.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > o1_image_feedback.tStartRefresh + 2-frameTolerance:
                            # keep track of stop time/frame for later
                            o1_image_feedback.tStop = t  # not accounting for scr refresh
                            o1_image_feedback.frameNStop = frameN  # exact frame index
                            o1_image_feedback.setAutoDraw(False)
                    
                    # *o2_image_feedback* updates
                    if o2_image_feedback.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        o2_image_feedback.frameNStart = frameN  # exact frame index
                        o2_image_feedback.tStart = t  # local t and not account for scr refresh
                        o2_image_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(o2_image_feedback, 'tStartRefresh')  # time at next scr refresh
                        o2_image_feedback.setAutoDraw(True)
                    if o2_image_feedback.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > o2_image_feedback.tStartRefresh + 2-frameTolerance:
                            # keep track of stop time/frame for later
                            o2_image_feedback.tStop = t  # not accounting for scr refresh
                            o2_image_feedback.frameNStop = frameN  # exact frame index
                            o2_image_feedback.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in feedbackComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "feedback" ---
                for thisComponent in feedbackComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-2.000000)
                thisExp.nextEntry()
                
            # completed feedback_reps repeats of 'feedback_loop'
            
            thisExp.nextEntry()
            
        # completed 4.0 repeats of 'training_trials'
        
        
        # set up handler to look after randomisation of conditions etc
        vsubtle_loop = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='vsubtle_loop')
        thisExp.addLoop(vsubtle_loop)  # add the loop to the experiment
        thisVsubtle_loop = vsubtle_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisVsubtle_loop.rgb)
        if thisVsubtle_loop != None:
            for paramName in thisVsubtle_loop:
                exec('{} = thisVsubtle_loop[paramName]'.format(paramName))
        
        for thisVsubtle_loop in vsubtle_loop:
            currentLoop = vsubtle_loop
            # abbreviate parameter names if possible (e.g. rgb = thisVsubtle_loop.rgb)
            if thisVsubtle_loop != None:
                for paramName in thisVsubtle_loop:
                    exec('{} = thisVsubtle_loop[paramName]'.format(paramName))
            
            # set up handler to look after randomisation of conditions etc
            task2_instr_vsubtle = data.TrialHandler(nReps=1.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('task2_instructions.xlsx'),
                seed=None, name='task2_instr_vsubtle')
            thisExp.addLoop(task2_instr_vsubtle)  # add the loop to the experiment
            thisTask2_instr_vsubtle = task2_instr_vsubtle.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTask2_instr_vsubtle.rgb)
            if thisTask2_instr_vsubtle != None:
                for paramName in thisTask2_instr_vsubtle:
                    exec('{} = thisTask2_instr_vsubtle[paramName]'.format(paramName))
            
            for thisTask2_instr_vsubtle in task2_instr_vsubtle:
                currentLoop = task2_instr_vsubtle
                # abbreviate parameter names if possible (e.g. rgb = thisTask2_instr_vsubtle.rgb)
                if thisTask2_instr_vsubtle != None:
                    for paramName in thisTask2_instr_vsubtle:
                        exec('{} = thisTask2_instr_vsubtle[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "test1_vsubtle_inst" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                cont_test1_vsubtle.reset()
                # setup some python lists for storing info about the cont_mouse_test1_vsubtle
                cont_mouse_test1_vsubtle.clicked_name = []
                gotValidClick = False  # until a click is received
                instructions_test1_vsubtle.setImage(task2)
                # keep track of which components have finished
                test1_vsubtle_instComponents = [cont_test1_vsubtle, cont_mouse_test1_vsubtle, instructions_test1_vsubtle]
                for thisComponent in test1_vsubtle_instComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test1_vsubtle_inst" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *cont_test1_vsubtle* updates
                    if cont_test1_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_test1_vsubtle.frameNStart = frameN  # exact frame index
                        cont_test1_vsubtle.tStart = t  # local t and not account for scr refresh
                        cont_test1_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_test1_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        cont_test1_vsubtle.setAutoDraw(True)
                    # *cont_mouse_test1_vsubtle* updates
                    if cont_mouse_test1_vsubtle.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_mouse_test1_vsubtle.frameNStart = frameN  # exact frame index
                        cont_mouse_test1_vsubtle.tStart = t  # local t and not account for scr refresh
                        cont_mouse_test1_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_mouse_test1_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        cont_mouse_test1_vsubtle.status = STARTED
                        cont_mouse_test1_vsubtle.mouseClock.reset()
                        prevButtonState = cont_mouse_test1_vsubtle.getPressed()  # if button is down already this ISN'T a new click
                    if cont_mouse_test1_vsubtle.status == STARTED:  # only update if started and not finished!
                        buttons = cont_mouse_test1_vsubtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter(cont_test1_vsubtle)
                                    clickableList = cont_test1_vsubtle
                                except:
                                    clickableList = [cont_test1_vsubtle]
                                for obj in clickableList:
                                    if obj.contains(cont_mouse_test1_vsubtle):
                                        gotValidClick = True
                                        cont_mouse_test1_vsubtle.clicked_name.append(obj.name)
                                if gotValidClick:  
                                    continueRoutine = False  # abort routine on response
                    
                    # *instructions_test1_vsubtle* updates
                    if instructions_test1_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        instructions_test1_vsubtle.frameNStart = frameN  # exact frame index
                        instructions_test1_vsubtle.tStart = t  # local t and not account for scr refresh
                        instructions_test1_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(instructions_test1_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        instructions_test1_vsubtle.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test1_vsubtle_instComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test1_vsubtle_inst" ---
                for thisComponent in test1_vsubtle_instComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store data for task2_instr_vsubtle (TrialHandler)
                # the Routine "test1_vsubtle_inst" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'task2_instr_vsubtle'
            
            
            # --- Prepare to start Routine "comprehension2" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            comp2_resp2.reset()
            comp2_resp1.reset()
            comp2_resp3.reset()
            # setup some python lists for storing info about the comp2_mouse
            comp2_mouse.x = []
            comp2_mouse.y = []
            comp2_mouse.leftButton = []
            comp2_mouse.midButton = []
            comp2_mouse.rightButton = []
            comp2_mouse.time = []
            comp2_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            comp2_mouse.mouseClock.reset()
            # keep track of which components have finished
            comprehension2Components = [comp2_resp2, comp2_resp1, comp2_resp3, comp2_mouse, check2]
            for thisComponent in comprehension2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "comprehension2" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *comp2_resp2* updates
                if comp2_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp2_resp2.frameNStart = frameN  # exact frame index
                    comp2_resp2.tStart = t  # local t and not account for scr refresh
                    comp2_resp2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp2_resp2, 'tStartRefresh')  # time at next scr refresh
                    comp2_resp2.setAutoDraw(True)
                
                # *comp2_resp1* updates
                if comp2_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp2_resp1.frameNStart = frameN  # exact frame index
                    comp2_resp1.tStart = t  # local t and not account for scr refresh
                    comp2_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp2_resp1, 'tStartRefresh')  # time at next scr refresh
                    comp2_resp1.setAutoDraw(True)
                
                # *comp2_resp3* updates
                if comp2_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp2_resp3.frameNStart = frameN  # exact frame index
                    comp2_resp3.tStart = t  # local t and not account for scr refresh
                    comp2_resp3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp2_resp3, 'tStartRefresh')  # time at next scr refresh
                    comp2_resp3.setAutoDraw(True)
                # *comp2_mouse* updates
                if comp2_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp2_mouse.frameNStart = frameN  # exact frame index
                    comp2_mouse.tStart = t  # local t and not account for scr refresh
                    comp2_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp2_mouse, 'tStartRefresh')  # time at next scr refresh
                    comp2_mouse.status = STARTED
                    prevButtonState = comp2_mouse.getPressed()  # if button is down already this ISN'T a new click
                if comp2_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = comp2_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([comp2_resp1, comp2_resp2, comp2_resp3])
                                clickableList = [comp2_resp1, comp2_resp2, comp2_resp3]
                            except:
                                clickableList = [[comp2_resp1, comp2_resp2, comp2_resp3]]
                            for obj in clickableList:
                                if obj.contains(comp2_mouse):
                                    gotValidClick = True
                                    comp2_mouse.clicked_name.append(obj.name)
                            x, y = comp2_mouse.getPos()
                            comp2_mouse.x.append(x)
                            comp2_mouse.y.append(y)
                            buttons = comp2_mouse.getPressed()
                            comp2_mouse.leftButton.append(buttons[0])
                            comp2_mouse.midButton.append(buttons[1])
                            comp2_mouse.rightButton.append(buttons[2])
                            comp2_mouse.time.append(comp2_mouse.mouseClock.getTime())
                            if gotValidClick:
                                continueRoutine = False  # abort routine on response
                
                # *check2* updates
                if check2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    check2.frameNStart = frameN  # exact frame index
                    check2.tStart = t  # local t and not account for scr refresh
                    check2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(check2, 'tStartRefresh')  # time at next scr refresh
                    check2.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in comprehension2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "comprehension2" ---
            for thisComponent in comprehension2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for vsubtle_loop (TrialHandler)
            vsubtle_loop.addData('comp2_mouse.x', comp2_mouse.x)
            vsubtle_loop.addData('comp2_mouse.y', comp2_mouse.y)
            vsubtle_loop.addData('comp2_mouse.leftButton', comp2_mouse.leftButton)
            vsubtle_loop.addData('comp2_mouse.midButton', comp2_mouse.midButton)
            vsubtle_loop.addData('comp2_mouse.rightButton', comp2_mouse.rightButton)
            vsubtle_loop.addData('comp2_mouse.time', comp2_mouse.time)
            vsubtle_loop.addData('comp2_mouse.clicked_name', comp2_mouse.clicked_name)
            # the Routine "comprehension2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            test1_vsubtle_trials = data.TrialHandler(nReps=1.0, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('test1_trials.xlsx'),
                seed=None, name='test1_vsubtle_trials')
            thisExp.addLoop(test1_vsubtle_trials)  # add the loop to the experiment
            thisTest1_vsubtle_trial = test1_vsubtle_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTest1_vsubtle_trial.rgb)
            if thisTest1_vsubtle_trial != None:
                for paramName in thisTest1_vsubtle_trial:
                    exec('{} = thisTest1_vsubtle_trial[paramName]'.format(paramName))
            
            for thisTest1_vsubtle_trial in test1_vsubtle_trials:
                currentLoop = test1_vsubtle_trials
                # abbreviate parameter names if possible (e.g. rgb = thisTest1_vsubtle_trial.rgb)
                if thisTest1_vsubtle_trial != None:
                    for paramName in thisTest1_vsubtle_trial:
                        exec('{} = thisTest1_vsubtle_trial[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "test1_vsubtle_choice" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                # Run 'Begin Routine' code from target_determination_test1_vsubtle
                if target == 1:
                    stim1 = reorder_cues[0]
                elif target == 2:
                    stim1 = reorder_cues[1]
                elif target == 5:
                    stim1 = reorder_cues[4]
                elif target == 6:
                    stim1 = reorder_cues[5]
                # Run 'Begin Routine' code from distractor_presentation
                if target == 1:
                    distractor = reorder_vsubtle[0]
                elif target == 2:
                    distractor = reorder_vsubtle[1]
                elif target == 5:
                    distractor = reorder_vsubtle[4]
                elif target == 6:
                    distractor = reorder_vsubtle[5]
                target_test1_vsubtle.setPos(target_position)
                target_test1_vsubtle.setImage(stim1)
                distractor_test1_vsubtle.setPos(distractor_position)
                distractor_test1_vsubtle.setImage(distractor)
                # setup some python lists for storing info about the mouse_test1_vsubtle
                mouse_test1_vsubtle.x = []
                mouse_test1_vsubtle.y = []
                mouse_test1_vsubtle.leftButton = []
                mouse_test1_vsubtle.midButton = []
                mouse_test1_vsubtle.rightButton = []
                mouse_test1_vsubtle.time = []
                mouse_test1_vsubtle.clicked_name = []
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                test1_vsubtle_choiceComponents = [blank_test1_vsubtle, target_test1_vsubtle, distractor_test1_vsubtle, mouse_test1_vsubtle]
                for thisComponent in test1_vsubtle_choiceComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test1_vsubtle_choice" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *blank_test1_vsubtle* updates
                    if blank_test1_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        blank_test1_vsubtle.frameNStart = frameN  # exact frame index
                        blank_test1_vsubtle.tStart = t  # local t and not account for scr refresh
                        blank_test1_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(blank_test1_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        blank_test1_vsubtle.setAutoDraw(True)
                    if blank_test1_vsubtle.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > blank_test1_vsubtle.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            blank_test1_vsubtle.tStop = t  # not accounting for scr refresh
                            blank_test1_vsubtle.frameNStop = frameN  # exact frame index
                            blank_test1_vsubtle.setAutoDraw(False)
                    
                    # *target_test1_vsubtle* updates
                    if target_test1_vsubtle.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        target_test1_vsubtle.frameNStart = frameN  # exact frame index
                        target_test1_vsubtle.tStart = t  # local t and not account for scr refresh
                        target_test1_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(target_test1_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        target_test1_vsubtle.setAutoDraw(True)
                    
                    # *distractor_test1_vsubtle* updates
                    if distractor_test1_vsubtle.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        distractor_test1_vsubtle.frameNStart = frameN  # exact frame index
                        distractor_test1_vsubtle.tStart = t  # local t and not account for scr refresh
                        distractor_test1_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(distractor_test1_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        distractor_test1_vsubtle.setAutoDraw(True)
                    # *mouse_test1_vsubtle* updates
                    if mouse_test1_vsubtle.status == NOT_STARTED and t >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_test1_vsubtle.frameNStart = frameN  # exact frame index
                        mouse_test1_vsubtle.tStart = t  # local t and not account for scr refresh
                        mouse_test1_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_test1_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        mouse_test1_vsubtle.status = STARTED
                        mouse_test1_vsubtle.mouseClock.reset()
                        prevButtonState = mouse_test1_vsubtle.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_test1_vsubtle.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_test1_vsubtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter([target_test1_vsubtle, distractor_test1_vsubtle])
                                    clickableList = [target_test1_vsubtle, distractor_test1_vsubtle]
                                except:
                                    clickableList = [[target_test1_vsubtle, distractor_test1_vsubtle]]
                                for obj in clickableList:
                                    if obj.contains(mouse_test1_vsubtle):
                                        gotValidClick = True
                                        mouse_test1_vsubtle.clicked_name.append(obj.name)
                                if gotValidClick:
                                    x, y = mouse_test1_vsubtle.getPos()
                                    mouse_test1_vsubtle.x.append(x)
                                    mouse_test1_vsubtle.y.append(y)
                                    buttons = mouse_test1_vsubtle.getPressed()
                                    mouse_test1_vsubtle.leftButton.append(buttons[0])
                                    mouse_test1_vsubtle.midButton.append(buttons[1])
                                    mouse_test1_vsubtle.rightButton.append(buttons[2])
                                    mouse_test1_vsubtle.time.append(mouse_test1_vsubtle.mouseClock.getTime())
                                if gotValidClick:
                                    continueRoutine = False  # abort routine on response
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test1_vsubtle_choiceComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test1_vsubtle_choice" ---
                for thisComponent in test1_vsubtle_choiceComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store data for test1_vsubtle_trials (TrialHandler)
                test1_vsubtle_trials.addData('mouse_test1_vsubtle.x', mouse_test1_vsubtle.x)
                test1_vsubtle_trials.addData('mouse_test1_vsubtle.y', mouse_test1_vsubtle.y)
                test1_vsubtle_trials.addData('mouse_test1_vsubtle.leftButton', mouse_test1_vsubtle.leftButton)
                test1_vsubtle_trials.addData('mouse_test1_vsubtle.midButton', mouse_test1_vsubtle.midButton)
                test1_vsubtle_trials.addData('mouse_test1_vsubtle.rightButton', mouse_test1_vsubtle.rightButton)
                test1_vsubtle_trials.addData('mouse_test1_vsubtle.time', mouse_test1_vsubtle.time)
                test1_vsubtle_trials.addData('mouse_test1_vsubtle.clicked_name', mouse_test1_vsubtle.clicked_name)
                # the Routine "test1_vsubtle_choice" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "test1_vsubtle_rate" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                slider_test1_vsubtle.reset()
                slider_target_test1_vsubtle.setPos(target_position)
                slider_target_test1_vsubtle.setImage(stim1)
                slider_distractor_test1_vsubtle.setPos(distractor_position)
                slider_distractor_test1_vsubtle.setImage(distractor)
                continue_rate_test1_vsubtle.reset()
                # setup some python lists for storing info about the mouse_continue_test1_vsubtle
                mouse_continue_test1_vsubtle.clicked_name = []
                gotValidClick = False  # until a click is received
                # Run 'Begin Routine' code from show_continue_rate
                show_continue = False
                # keep track of which components have finished
                test1_vsubtle_rateComponents = [slider_text_test1_vsubtle, slider_test1_vsubtle, slider_target_test1_vsubtle, slider_distractor_test1_vsubtle, continue_rate_test1_vsubtle, mouse_continue_test1_vsubtle]
                for thisComponent in test1_vsubtle_rateComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test1_vsubtle_rate" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *slider_text_test1_vsubtle* updates
                    if slider_text_test1_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_text_test1_vsubtle.frameNStart = frameN  # exact frame index
                        slider_text_test1_vsubtle.tStart = t  # local t and not account for scr refresh
                        slider_text_test1_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_text_test1_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_text_test1_vsubtle.setAutoDraw(True)
                    
                    # *slider_test1_vsubtle* updates
                    if slider_test1_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_test1_vsubtle.frameNStart = frameN  # exact frame index
                        slider_test1_vsubtle.tStart = t  # local t and not account for scr refresh
                        slider_test1_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_test1_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_test1_vsubtle.setAutoDraw(True)
                    
                    # *slider_target_test1_vsubtle* updates
                    if slider_target_test1_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_target_test1_vsubtle.frameNStart = frameN  # exact frame index
                        slider_target_test1_vsubtle.tStart = t  # local t and not account for scr refresh
                        slider_target_test1_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_target_test1_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_target_test1_vsubtle.setAutoDraw(True)
                    
                    # *slider_distractor_test1_vsubtle* updates
                    if slider_distractor_test1_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_distractor_test1_vsubtle.frameNStart = frameN  # exact frame index
                        slider_distractor_test1_vsubtle.tStart = t  # local t and not account for scr refresh
                        slider_distractor_test1_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_distractor_test1_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_distractor_test1_vsubtle.setAutoDraw(True)
                    
                    # *continue_rate_test1_vsubtle* updates
                    if continue_rate_test1_vsubtle.status == NOT_STARTED and show_continue:
                        # keep track of start time/frame for later
                        continue_rate_test1_vsubtle.frameNStart = frameN  # exact frame index
                        continue_rate_test1_vsubtle.tStart = t  # local t and not account for scr refresh
                        continue_rate_test1_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(continue_rate_test1_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        continue_rate_test1_vsubtle.setAutoDraw(True)
                    # *mouse_continue_test1_vsubtle* updates
                    if mouse_continue_test1_vsubtle.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_continue_test1_vsubtle.frameNStart = frameN  # exact frame index
                        mouse_continue_test1_vsubtle.tStart = t  # local t and not account for scr refresh
                        mouse_continue_test1_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_continue_test1_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        mouse_continue_test1_vsubtle.status = STARTED
                        mouse_continue_test1_vsubtle.mouseClock.reset()
                        prevButtonState = mouse_continue_test1_vsubtle.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_continue_test1_vsubtle.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_continue_test1_vsubtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter(continue_rate_test1_vsubtle)
                                    clickableList = continue_rate_test1_vsubtle
                                except:
                                    clickableList = [continue_rate_test1_vsubtle]
                                for obj in clickableList:
                                    if obj.contains(mouse_continue_test1_vsubtle):
                                        gotValidClick = True
                                        mouse_continue_test1_vsubtle.clicked_name.append(obj.name)
                                if gotValidClick:  
                                    continueRoutine = False  # abort routine on response
                    # Run 'Each Frame' code from show_continue_rate
                    slid = slider_test1_vsubtle.getRating()
                    
                    if slid is not None:
                        show_continue = True
                                
                                
                    
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test1_vsubtle_rateComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test1_vsubtle_rate" ---
                for thisComponent in test1_vsubtle_rateComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                test1_vsubtle_trials.addData('slider_test1_vsubtle.response', slider_test1_vsubtle.getRating())
                test1_vsubtle_trials.addData('slider_test1_vsubtle.rt', slider_test1_vsubtle.getRT())
                # store data for test1_vsubtle_trials (TrialHandler)
                # the Routine "test1_vsubtle_rate" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'test1_vsubtle_trials'
            
            
            # set up handler to look after randomisation of conditions etc
            task3_instr_vsubtle = data.TrialHandler(nReps=1.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('task3_instructions.xlsx'),
                seed=None, name='task3_instr_vsubtle')
            thisExp.addLoop(task3_instr_vsubtle)  # add the loop to the experiment
            thisTask3_instr_vsubtle = task3_instr_vsubtle.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTask3_instr_vsubtle.rgb)
            if thisTask3_instr_vsubtle != None:
                for paramName in thisTask3_instr_vsubtle:
                    exec('{} = thisTask3_instr_vsubtle[paramName]'.format(paramName))
            
            for thisTask3_instr_vsubtle in task3_instr_vsubtle:
                currentLoop = task3_instr_vsubtle
                # abbreviate parameter names if possible (e.g. rgb = thisTask3_instr_vsubtle.rgb)
                if thisTask3_instr_vsubtle != None:
                    for paramName in thisTask3_instr_vsubtle:
                        exec('{} = thisTask3_instr_vsubtle[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "test2_vsubtle_inst" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                cont_test2_vsubtle.reset()
                # setup some python lists for storing info about the cont_mouse_test2_vsubtle
                cont_mouse_test2_vsubtle.clicked_name = []
                gotValidClick = False  # until a click is received
                instructions_test2_vsubtle.setImage(task3)
                # keep track of which components have finished
                test2_vsubtle_instComponents = [cont_test2_vsubtle, cont_mouse_test2_vsubtle, instructions_test2_vsubtle]
                for thisComponent in test2_vsubtle_instComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test2_vsubtle_inst" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *cont_test2_vsubtle* updates
                    if cont_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_test2_vsubtle.frameNStart = frameN  # exact frame index
                        cont_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                        cont_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        cont_test2_vsubtle.setAutoDraw(True)
                    # *cont_mouse_test2_vsubtle* updates
                    if cont_mouse_test2_vsubtle.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_mouse_test2_vsubtle.frameNStart = frameN  # exact frame index
                        cont_mouse_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                        cont_mouse_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_mouse_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        cont_mouse_test2_vsubtle.status = STARTED
                        cont_mouse_test2_vsubtle.mouseClock.reset()
                        prevButtonState = cont_mouse_test2_vsubtle.getPressed()  # if button is down already this ISN'T a new click
                    if cont_mouse_test2_vsubtle.status == STARTED:  # only update if started and not finished!
                        buttons = cont_mouse_test2_vsubtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter(cont_test2_vsubtle)
                                    clickableList = cont_test2_vsubtle
                                except:
                                    clickableList = [cont_test2_vsubtle]
                                for obj in clickableList:
                                    if obj.contains(cont_mouse_test2_vsubtle):
                                        gotValidClick = True
                                        cont_mouse_test2_vsubtle.clicked_name.append(obj.name)
                                if gotValidClick:  
                                    continueRoutine = False  # abort routine on response
                    
                    # *instructions_test2_vsubtle* updates
                    if instructions_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        instructions_test2_vsubtle.frameNStart = frameN  # exact frame index
                        instructions_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                        instructions_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(instructions_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        instructions_test2_vsubtle.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test2_vsubtle_instComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test2_vsubtle_inst" ---
                for thisComponent in test2_vsubtle_instComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store data for task3_instr_vsubtle (TrialHandler)
                # the Routine "test2_vsubtle_inst" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'task3_instr_vsubtle'
            
            
            # --- Prepare to start Routine "comprehension3" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            comp3_resp2.reset()
            comp3_resp1.reset()
            comp3_resp3.reset()
            # setup some python lists for storing info about the comp3_mouse
            comp3_mouse.x = []
            comp3_mouse.y = []
            comp3_mouse.leftButton = []
            comp3_mouse.midButton = []
            comp3_mouse.rightButton = []
            comp3_mouse.time = []
            comp3_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            comp3_mouse.mouseClock.reset()
            # keep track of which components have finished
            comprehension3Components = [comp3_resp2, comp3_resp1, comp3_resp3, comp3_mouse, check3]
            for thisComponent in comprehension3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "comprehension3" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *comp3_resp2* updates
                if comp3_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp3_resp2.frameNStart = frameN  # exact frame index
                    comp3_resp2.tStart = t  # local t and not account for scr refresh
                    comp3_resp2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp3_resp2, 'tStartRefresh')  # time at next scr refresh
                    comp3_resp2.setAutoDraw(True)
                
                # *comp3_resp1* updates
                if comp3_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp3_resp1.frameNStart = frameN  # exact frame index
                    comp3_resp1.tStart = t  # local t and not account for scr refresh
                    comp3_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp3_resp1, 'tStartRefresh')  # time at next scr refresh
                    comp3_resp1.setAutoDraw(True)
                
                # *comp3_resp3* updates
                if comp3_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp3_resp3.frameNStart = frameN  # exact frame index
                    comp3_resp3.tStart = t  # local t and not account for scr refresh
                    comp3_resp3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp3_resp3, 'tStartRefresh')  # time at next scr refresh
                    comp3_resp3.setAutoDraw(True)
                # *comp3_mouse* updates
                if comp3_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp3_mouse.frameNStart = frameN  # exact frame index
                    comp3_mouse.tStart = t  # local t and not account for scr refresh
                    comp3_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp3_mouse, 'tStartRefresh')  # time at next scr refresh
                    comp3_mouse.status = STARTED
                    prevButtonState = comp3_mouse.getPressed()  # if button is down already this ISN'T a new click
                if comp3_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = comp3_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([comp3_resp1, comp3_resp2, comp3_resp3])
                                clickableList = [comp3_resp1, comp3_resp2, comp3_resp3]
                            except:
                                clickableList = [[comp3_resp1, comp3_resp2, comp3_resp3]]
                            for obj in clickableList:
                                if obj.contains(comp3_mouse):
                                    gotValidClick = True
                                    comp3_mouse.clicked_name.append(obj.name)
                            x, y = comp3_mouse.getPos()
                            comp3_mouse.x.append(x)
                            comp3_mouse.y.append(y)
                            buttons = comp3_mouse.getPressed()
                            comp3_mouse.leftButton.append(buttons[0])
                            comp3_mouse.midButton.append(buttons[1])
                            comp3_mouse.rightButton.append(buttons[2])
                            comp3_mouse.time.append(comp3_mouse.mouseClock.getTime())
                            if gotValidClick:
                                continueRoutine = False  # abort routine on response
                
                # *check3* updates
                if check3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    check3.frameNStart = frameN  # exact frame index
                    check3.tStart = t  # local t and not account for scr refresh
                    check3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(check3, 'tStartRefresh')  # time at next scr refresh
                    check3.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in comprehension3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "comprehension3" ---
            for thisComponent in comprehension3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for vsubtle_loop (TrialHandler)
            vsubtle_loop.addData('comp3_mouse.x', comp3_mouse.x)
            vsubtle_loop.addData('comp3_mouse.y', comp3_mouse.y)
            vsubtle_loop.addData('comp3_mouse.leftButton', comp3_mouse.leftButton)
            vsubtle_loop.addData('comp3_mouse.midButton', comp3_mouse.midButton)
            vsubtle_loop.addData('comp3_mouse.rightButton', comp3_mouse.rightButton)
            vsubtle_loop.addData('comp3_mouse.time', comp3_mouse.time)
            vsubtle_loop.addData('comp3_mouse.clicked_name', comp3_mouse.clicked_name)
            # the Routine "comprehension3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            test2_vsubtle_trials = data.TrialHandler(nReps=1.0, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('test2_trials.xlsx'),
                seed=None, name='test2_vsubtle_trials')
            thisExp.addLoop(test2_vsubtle_trials)  # add the loop to the experiment
            thisTest2_vsubtle_trial = test2_vsubtle_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTest2_vsubtle_trial.rgb)
            if thisTest2_vsubtle_trial != None:
                for paramName in thisTest2_vsubtle_trial:
                    exec('{} = thisTest2_vsubtle_trial[paramName]'.format(paramName))
            
            for thisTest2_vsubtle_trial in test2_vsubtle_trials:
                currentLoop = test2_vsubtle_trials
                # abbreviate parameter names if possible (e.g. rgb = thisTest2_vsubtle_trial.rgb)
                if thisTest2_vsubtle_trial != None:
                    for paramName in thisTest2_vsubtle_trial:
                        exec('{} = thisTest2_vsubtle_trial[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "test2_vsubtle_choice" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                # Run 'Begin Routine' code from target_determination_2
                if target == 1:
                    stim1 = reorder_cues[0]
                elif target == 2:
                    stim1 = reorder_cues[1]
                elif target == 5:
                    stim1 = reorder_cues[4]
                elif target == 6:
                    stim1 = reorder_cues[5]
                # Run 'Begin Routine' code from distractor_presentation_test2_vsubtle
                if distractor_test2 == 1:
                    distractor = reorder_vsubtle[0]
                elif distractor_test2 == 2:
                    distractor = reorder_vsubtle[1]
                elif distractor_test2 == 5:
                    distractor = reorder_vsubtle[4]
                elif distractor_test2 == 6:
                    distractor = reorder_vsubtle[5]
                target_test2_vsubtle.setPos(target_position)
                target_test2_vsubtle.setImage(stim1)
                distractor_test2_vsubtle.setPos(distractor_position)
                distractor_test2_vsubtle.setImage(distractor)
                # setup some python lists for storing info about the mouse_test2_vsubtle
                mouse_test2_vsubtle.x = []
                mouse_test2_vsubtle.y = []
                mouse_test2_vsubtle.leftButton = []
                mouse_test2_vsubtle.midButton = []
                mouse_test2_vsubtle.rightButton = []
                mouse_test2_vsubtle.time = []
                mouse_test2_vsubtle.clicked_name = []
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                test2_vsubtle_choiceComponents = [blank_test2_vsubtle, target_test2_vsubtle, distractor_test2_vsubtle, mouse_test2_vsubtle]
                for thisComponent in test2_vsubtle_choiceComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test2_vsubtle_choice" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *blank_test2_vsubtle* updates
                    if blank_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        blank_test2_vsubtle.frameNStart = frameN  # exact frame index
                        blank_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                        blank_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(blank_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        blank_test2_vsubtle.setAutoDraw(True)
                    if blank_test2_vsubtle.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > blank_test2_vsubtle.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            blank_test2_vsubtle.tStop = t  # not accounting for scr refresh
                            blank_test2_vsubtle.frameNStop = frameN  # exact frame index
                            blank_test2_vsubtle.setAutoDraw(False)
                    
                    # *target_test2_vsubtle* updates
                    if target_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        target_test2_vsubtle.frameNStart = frameN  # exact frame index
                        target_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                        target_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(target_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        target_test2_vsubtle.setAutoDraw(True)
                    
                    # *distractor_test2_vsubtle* updates
                    if distractor_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        distractor_test2_vsubtle.frameNStart = frameN  # exact frame index
                        distractor_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                        distractor_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(distractor_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        distractor_test2_vsubtle.setAutoDraw(True)
                    # *mouse_test2_vsubtle* updates
                    if mouse_test2_vsubtle.status == NOT_STARTED and t >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_test2_vsubtle.frameNStart = frameN  # exact frame index
                        mouse_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                        mouse_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        mouse_test2_vsubtle.status = STARTED
                        mouse_test2_vsubtle.mouseClock.reset()
                        prevButtonState = mouse_test2_vsubtle.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_test2_vsubtle.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_test2_vsubtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter([target_test2_vsubtle, distractor_test2_vsubtle])
                                    clickableList = [target_test2_vsubtle, distractor_test2_vsubtle]
                                except:
                                    clickableList = [[target_test2_vsubtle, distractor_test2_vsubtle]]
                                for obj in clickableList:
                                    if obj.contains(mouse_test2_vsubtle):
                                        gotValidClick = True
                                        mouse_test2_vsubtle.clicked_name.append(obj.name)
                                if gotValidClick:
                                    x, y = mouse_test2_vsubtle.getPos()
                                    mouse_test2_vsubtle.x.append(x)
                                    mouse_test2_vsubtle.y.append(y)
                                    buttons = mouse_test2_vsubtle.getPressed()
                                    mouse_test2_vsubtle.leftButton.append(buttons[0])
                                    mouse_test2_vsubtle.midButton.append(buttons[1])
                                    mouse_test2_vsubtle.rightButton.append(buttons[2])
                                    mouse_test2_vsubtle.time.append(mouse_test2_vsubtle.mouseClock.getTime())
                                if gotValidClick:
                                    continueRoutine = False  # abort routine on response
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test2_vsubtle_choiceComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test2_vsubtle_choice" ---
                for thisComponent in test2_vsubtle_choiceComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store data for test2_vsubtle_trials (TrialHandler)
                test2_vsubtle_trials.addData('mouse_test2_vsubtle.x', mouse_test2_vsubtle.x)
                test2_vsubtle_trials.addData('mouse_test2_vsubtle.y', mouse_test2_vsubtle.y)
                test2_vsubtle_trials.addData('mouse_test2_vsubtle.leftButton', mouse_test2_vsubtle.leftButton)
                test2_vsubtle_trials.addData('mouse_test2_vsubtle.midButton', mouse_test2_vsubtle.midButton)
                test2_vsubtle_trials.addData('mouse_test2_vsubtle.rightButton', mouse_test2_vsubtle.rightButton)
                test2_vsubtle_trials.addData('mouse_test2_vsubtle.time', mouse_test2_vsubtle.time)
                test2_vsubtle_trials.addData('mouse_test2_vsubtle.clicked_name', mouse_test2_vsubtle.clicked_name)
                # the Routine "test2_vsubtle_choice" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "test2_vsubtle_rate" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                slider_test2_vsubtle.reset()
                slider_target_test2_vsubtle.setPos(target_position)
                slider_target_test2_vsubtle.setImage(stim1)
                slider_distractor_test2_vsubtle.setPos(distractor_position)
                slider_distractor_test2_vsubtle.setImage(distractor)
                # Run 'Begin Routine' code from show_continue_rate_test2_vsubtle
                show_continue_test2_vsubtle = False
                continue_rate_test2_vsubtle.reset()
                # setup some python lists for storing info about the mouse_continue_test2_vsubtle
                mouse_continue_test2_vsubtle.clicked_name = []
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                test2_vsubtle_rateComponents = [slider_text_test2_vsubtle, slider_test2_vsubtle, slider_target_test2_vsubtle, slider_distractor_test2_vsubtle, continue_rate_test2_vsubtle, mouse_continue_test2_vsubtle]
                for thisComponent in test2_vsubtle_rateComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test2_vsubtle_rate" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *slider_text_test2_vsubtle* updates
                    if slider_text_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_text_test2_vsubtle.frameNStart = frameN  # exact frame index
                        slider_text_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                        slider_text_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_text_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_text_test2_vsubtle.setAutoDraw(True)
                    
                    # *slider_test2_vsubtle* updates
                    if slider_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_test2_vsubtle.frameNStart = frameN  # exact frame index
                        slider_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                        slider_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_test2_vsubtle.setAutoDraw(True)
                    
                    # *slider_target_test2_vsubtle* updates
                    if slider_target_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_target_test2_vsubtle.frameNStart = frameN  # exact frame index
                        slider_target_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                        slider_target_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_target_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_target_test2_vsubtle.setAutoDraw(True)
                    
                    # *slider_distractor_test2_vsubtle* updates
                    if slider_distractor_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_distractor_test2_vsubtle.frameNStart = frameN  # exact frame index
                        slider_distractor_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                        slider_distractor_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_distractor_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_distractor_test2_vsubtle.setAutoDraw(True)
                    # Run 'Each Frame' code from show_continue_rate_test2_vsubtle
                    slid2 = slider_test2_vsubtle.getRating()
                    
                    if slid2 is not None:
                        show_continue_test2_vsubtle = True
                                
                                
                    
                    
                    # *continue_rate_test2_vsubtle* updates
                    if continue_rate_test2_vsubtle.status == NOT_STARTED and show_continue_test2_vsubtle:
                        # keep track of start time/frame for later
                        continue_rate_test2_vsubtle.frameNStart = frameN  # exact frame index
                        continue_rate_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                        continue_rate_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(continue_rate_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        continue_rate_test2_vsubtle.setAutoDraw(True)
                    # *mouse_continue_test2_vsubtle* updates
                    if mouse_continue_test2_vsubtle.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_continue_test2_vsubtle.frameNStart = frameN  # exact frame index
                        mouse_continue_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                        mouse_continue_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_continue_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                        mouse_continue_test2_vsubtle.status = STARTED
                        mouse_continue_test2_vsubtle.mouseClock.reset()
                        prevButtonState = mouse_continue_test2_vsubtle.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_continue_test2_vsubtle.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_continue_test2_vsubtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter(continue_rate_test2_vsubtle)
                                    clickableList = continue_rate_test2_vsubtle
                                except:
                                    clickableList = [continue_rate_test2_vsubtle]
                                for obj in clickableList:
                                    if obj.contains(mouse_continue_test2_vsubtle):
                                        gotValidClick = True
                                        mouse_continue_test2_vsubtle.clicked_name.append(obj.name)
                                if gotValidClick:  
                                    continueRoutine = False  # abort routine on response
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test2_vsubtle_rateComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test2_vsubtle_rate" ---
                for thisComponent in test2_vsubtle_rateComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                test2_vsubtle_trials.addData('slider_test2_vsubtle.response', slider_test2_vsubtle.getRating())
                test2_vsubtle_trials.addData('slider_test2_vsubtle.rt', slider_test2_vsubtle.getRT())
                # store data for test2_vsubtle_trials (TrialHandler)
                # the Routine "test2_vsubtle_rate" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'test2_vsubtle_trials'
            
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'vsubtle_loop'
        
        
        # set up handler to look after randomisation of conditions etc
        subtle_loop = data.TrialHandler(nReps=0.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='subtle_loop')
        thisExp.addLoop(subtle_loop)  # add the loop to the experiment
        thisSubtle_loop = subtle_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSubtle_loop.rgb)
        if thisSubtle_loop != None:
            for paramName in thisSubtle_loop:
                exec('{} = thisSubtle_loop[paramName]'.format(paramName))
        
        for thisSubtle_loop in subtle_loop:
            currentLoop = subtle_loop
            # abbreviate parameter names if possible (e.g. rgb = thisSubtle_loop.rgb)
            if thisSubtle_loop != None:
                for paramName in thisSubtle_loop:
                    exec('{} = thisSubtle_loop[paramName]'.format(paramName))
            
            # set up handler to look after randomisation of conditions etc
            task2_instr_subtle = data.TrialHandler(nReps=1.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('task2_instructions.xlsx'),
                seed=None, name='task2_instr_subtle')
            thisExp.addLoop(task2_instr_subtle)  # add the loop to the experiment
            thisTask2_instr_subtle = task2_instr_subtle.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTask2_instr_subtle.rgb)
            if thisTask2_instr_subtle != None:
                for paramName in thisTask2_instr_subtle:
                    exec('{} = thisTask2_instr_subtle[paramName]'.format(paramName))
            
            for thisTask2_instr_subtle in task2_instr_subtle:
                currentLoop = task2_instr_subtle
                # abbreviate parameter names if possible (e.g. rgb = thisTask2_instr_subtle.rgb)
                if thisTask2_instr_subtle != None:
                    for paramName in thisTask2_instr_subtle:
                        exec('{} = thisTask2_instr_subtle[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "test1_subtle_inst" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                cont_test1_subtle.reset()
                # setup some python lists for storing info about the cont_mouse_test1_subtle
                cont_mouse_test1_subtle.clicked_name = []
                gotValidClick = False  # until a click is received
                instructions_test1_subtle.setImage(task2)
                # keep track of which components have finished
                test1_subtle_instComponents = [cont_test1_subtle, cont_mouse_test1_subtle, instructions_test1_subtle]
                for thisComponent in test1_subtle_instComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test1_subtle_inst" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *cont_test1_subtle* updates
                    if cont_test1_subtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_test1_subtle.frameNStart = frameN  # exact frame index
                        cont_test1_subtle.tStart = t  # local t and not account for scr refresh
                        cont_test1_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_test1_subtle, 'tStartRefresh')  # time at next scr refresh
                        cont_test1_subtle.setAutoDraw(True)
                    # *cont_mouse_test1_subtle* updates
                    if cont_mouse_test1_subtle.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_mouse_test1_subtle.frameNStart = frameN  # exact frame index
                        cont_mouse_test1_subtle.tStart = t  # local t and not account for scr refresh
                        cont_mouse_test1_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_mouse_test1_subtle, 'tStartRefresh')  # time at next scr refresh
                        cont_mouse_test1_subtle.status = STARTED
                        cont_mouse_test1_subtle.mouseClock.reset()
                        prevButtonState = cont_mouse_test1_subtle.getPressed()  # if button is down already this ISN'T a new click
                    if cont_mouse_test1_subtle.status == STARTED:  # only update if started and not finished!
                        buttons = cont_mouse_test1_subtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter(cont_test1_subtle)
                                    clickableList = cont_test1_subtle
                                except:
                                    clickableList = [cont_test1_subtle]
                                for obj in clickableList:
                                    if obj.contains(cont_mouse_test1_subtle):
                                        gotValidClick = True
                                        cont_mouse_test1_subtle.clicked_name.append(obj.name)
                                if gotValidClick:  
                                    continueRoutine = False  # abort routine on response
                    
                    # *instructions_test1_subtle* updates
                    if instructions_test1_subtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        instructions_test1_subtle.frameNStart = frameN  # exact frame index
                        instructions_test1_subtle.tStart = t  # local t and not account for scr refresh
                        instructions_test1_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(instructions_test1_subtle, 'tStartRefresh')  # time at next scr refresh
                        instructions_test1_subtle.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test1_subtle_instComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test1_subtle_inst" ---
                for thisComponent in test1_subtle_instComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store data for task2_instr_subtle (TrialHandler)
                # the Routine "test1_subtle_inst" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'task2_instr_subtle'
            
            
            # --- Prepare to start Routine "comprehension2" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            comp2_resp2.reset()
            comp2_resp1.reset()
            comp2_resp3.reset()
            # setup some python lists for storing info about the comp2_mouse
            comp2_mouse.x = []
            comp2_mouse.y = []
            comp2_mouse.leftButton = []
            comp2_mouse.midButton = []
            comp2_mouse.rightButton = []
            comp2_mouse.time = []
            comp2_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            comp2_mouse.mouseClock.reset()
            # keep track of which components have finished
            comprehension2Components = [comp2_resp2, comp2_resp1, comp2_resp3, comp2_mouse, check2]
            for thisComponent in comprehension2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "comprehension2" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *comp2_resp2* updates
                if comp2_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp2_resp2.frameNStart = frameN  # exact frame index
                    comp2_resp2.tStart = t  # local t and not account for scr refresh
                    comp2_resp2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp2_resp2, 'tStartRefresh')  # time at next scr refresh
                    comp2_resp2.setAutoDraw(True)
                
                # *comp2_resp1* updates
                if comp2_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp2_resp1.frameNStart = frameN  # exact frame index
                    comp2_resp1.tStart = t  # local t and not account for scr refresh
                    comp2_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp2_resp1, 'tStartRefresh')  # time at next scr refresh
                    comp2_resp1.setAutoDraw(True)
                
                # *comp2_resp3* updates
                if comp2_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp2_resp3.frameNStart = frameN  # exact frame index
                    comp2_resp3.tStart = t  # local t and not account for scr refresh
                    comp2_resp3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp2_resp3, 'tStartRefresh')  # time at next scr refresh
                    comp2_resp3.setAutoDraw(True)
                # *comp2_mouse* updates
                if comp2_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp2_mouse.frameNStart = frameN  # exact frame index
                    comp2_mouse.tStart = t  # local t and not account for scr refresh
                    comp2_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp2_mouse, 'tStartRefresh')  # time at next scr refresh
                    comp2_mouse.status = STARTED
                    prevButtonState = comp2_mouse.getPressed()  # if button is down already this ISN'T a new click
                if comp2_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = comp2_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([comp2_resp1, comp2_resp2, comp2_resp3])
                                clickableList = [comp2_resp1, comp2_resp2, comp2_resp3]
                            except:
                                clickableList = [[comp2_resp1, comp2_resp2, comp2_resp3]]
                            for obj in clickableList:
                                if obj.contains(comp2_mouse):
                                    gotValidClick = True
                                    comp2_mouse.clicked_name.append(obj.name)
                            x, y = comp2_mouse.getPos()
                            comp2_mouse.x.append(x)
                            comp2_mouse.y.append(y)
                            buttons = comp2_mouse.getPressed()
                            comp2_mouse.leftButton.append(buttons[0])
                            comp2_mouse.midButton.append(buttons[1])
                            comp2_mouse.rightButton.append(buttons[2])
                            comp2_mouse.time.append(comp2_mouse.mouseClock.getTime())
                            if gotValidClick:
                                continueRoutine = False  # abort routine on response
                
                # *check2* updates
                if check2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    check2.frameNStart = frameN  # exact frame index
                    check2.tStart = t  # local t and not account for scr refresh
                    check2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(check2, 'tStartRefresh')  # time at next scr refresh
                    check2.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in comprehension2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "comprehension2" ---
            for thisComponent in comprehension2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for subtle_loop (TrialHandler)
            subtle_loop.addData('comp2_mouse.x', comp2_mouse.x)
            subtle_loop.addData('comp2_mouse.y', comp2_mouse.y)
            subtle_loop.addData('comp2_mouse.leftButton', comp2_mouse.leftButton)
            subtle_loop.addData('comp2_mouse.midButton', comp2_mouse.midButton)
            subtle_loop.addData('comp2_mouse.rightButton', comp2_mouse.rightButton)
            subtle_loop.addData('comp2_mouse.time', comp2_mouse.time)
            subtle_loop.addData('comp2_mouse.clicked_name', comp2_mouse.clicked_name)
            # the Routine "comprehension2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            test1_subtle_trials = data.TrialHandler(nReps=1.0, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('test1_trials.xlsx'),
                seed=None, name='test1_subtle_trials')
            thisExp.addLoop(test1_subtle_trials)  # add the loop to the experiment
            thisTest1_subtle_trial = test1_subtle_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTest1_subtle_trial.rgb)
            if thisTest1_subtle_trial != None:
                for paramName in thisTest1_subtle_trial:
                    exec('{} = thisTest1_subtle_trial[paramName]'.format(paramName))
            
            for thisTest1_subtle_trial in test1_subtle_trials:
                currentLoop = test1_subtle_trials
                # abbreviate parameter names if possible (e.g. rgb = thisTest1_subtle_trial.rgb)
                if thisTest1_subtle_trial != None:
                    for paramName in thisTest1_subtle_trial:
                        exec('{} = thisTest1_subtle_trial[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "test1_subtle_choice" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                # Run 'Begin Routine' code from target_determination_test1_subtle
                if target == 1:
                    stim1 = reorder_cues[0]
                elif target == 2:
                    stim1 = reorder_cues[1]
                elif target == 5:
                    stim1 = reorder_cues[4]
                elif target == 6:
                    stim1 = reorder_cues[5]
                # Run 'Begin Routine' code from distractor_presentation_test1_subtle
                if target == 1:
                    distractor = reorder_subtle[0]
                elif target == 2:
                    distractor = reorder_subtle[1]
                elif target == 5:
                    distractor = reorder_subtle[4]
                elif target == 6:
                    distractor = reorder_subtle[5]
                target_test1_subtle.setPos(target_position)
                target_test1_subtle.setImage(stim1)
                distractor_test1_subtle.setPos(distractor_position)
                distractor_test1_subtle.setImage(distractor)
                # setup some python lists for storing info about the mouse_test1_subtle
                mouse_test1_subtle.x = []
                mouse_test1_subtle.y = []
                mouse_test1_subtle.leftButton = []
                mouse_test1_subtle.midButton = []
                mouse_test1_subtle.rightButton = []
                mouse_test1_subtle.time = []
                mouse_test1_subtle.clicked_name = []
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                test1_subtle_choiceComponents = [blank_test1_subtle, target_test1_subtle, distractor_test1_subtle, mouse_test1_subtle]
                for thisComponent in test1_subtle_choiceComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test1_subtle_choice" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *blank_test1_subtle* updates
                    if blank_test1_subtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        blank_test1_subtle.frameNStart = frameN  # exact frame index
                        blank_test1_subtle.tStart = t  # local t and not account for scr refresh
                        blank_test1_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(blank_test1_subtle, 'tStartRefresh')  # time at next scr refresh
                        blank_test1_subtle.setAutoDraw(True)
                    if blank_test1_subtle.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > blank_test1_subtle.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            blank_test1_subtle.tStop = t  # not accounting for scr refresh
                            blank_test1_subtle.frameNStop = frameN  # exact frame index
                            blank_test1_subtle.setAutoDraw(False)
                    
                    # *target_test1_subtle* updates
                    if target_test1_subtle.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        target_test1_subtle.frameNStart = frameN  # exact frame index
                        target_test1_subtle.tStart = t  # local t and not account for scr refresh
                        target_test1_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(target_test1_subtle, 'tStartRefresh')  # time at next scr refresh
                        target_test1_subtle.setAutoDraw(True)
                    
                    # *distractor_test1_subtle* updates
                    if distractor_test1_subtle.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        distractor_test1_subtle.frameNStart = frameN  # exact frame index
                        distractor_test1_subtle.tStart = t  # local t and not account for scr refresh
                        distractor_test1_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(distractor_test1_subtle, 'tStartRefresh')  # time at next scr refresh
                        distractor_test1_subtle.setAutoDraw(True)
                    # *mouse_test1_subtle* updates
                    if mouse_test1_subtle.status == NOT_STARTED and t >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_test1_subtle.frameNStart = frameN  # exact frame index
                        mouse_test1_subtle.tStart = t  # local t and not account for scr refresh
                        mouse_test1_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_test1_subtle, 'tStartRefresh')  # time at next scr refresh
                        mouse_test1_subtle.status = STARTED
                        mouse_test1_subtle.mouseClock.reset()
                        prevButtonState = mouse_test1_subtle.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_test1_subtle.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_test1_subtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter([target_test1_subtle, distractor_test1_subtle])
                                    clickableList = [target_test1_subtle, distractor_test1_subtle]
                                except:
                                    clickableList = [[target_test1_subtle, distractor_test1_subtle]]
                                for obj in clickableList:
                                    if obj.contains(mouse_test1_subtle):
                                        gotValidClick = True
                                        mouse_test1_subtle.clicked_name.append(obj.name)
                                if gotValidClick:
                                    x, y = mouse_test1_subtle.getPos()
                                    mouse_test1_subtle.x.append(x)
                                    mouse_test1_subtle.y.append(y)
                                    buttons = mouse_test1_subtle.getPressed()
                                    mouse_test1_subtle.leftButton.append(buttons[0])
                                    mouse_test1_subtle.midButton.append(buttons[1])
                                    mouse_test1_subtle.rightButton.append(buttons[2])
                                    mouse_test1_subtle.time.append(mouse_test1_subtle.mouseClock.getTime())
                                if gotValidClick:
                                    continueRoutine = False  # abort routine on response
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test1_subtle_choiceComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test1_subtle_choice" ---
                for thisComponent in test1_subtle_choiceComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store data for test1_subtle_trials (TrialHandler)
                test1_subtle_trials.addData('mouse_test1_subtle.x', mouse_test1_subtle.x)
                test1_subtle_trials.addData('mouse_test1_subtle.y', mouse_test1_subtle.y)
                test1_subtle_trials.addData('mouse_test1_subtle.leftButton', mouse_test1_subtle.leftButton)
                test1_subtle_trials.addData('mouse_test1_subtle.midButton', mouse_test1_subtle.midButton)
                test1_subtle_trials.addData('mouse_test1_subtle.rightButton', mouse_test1_subtle.rightButton)
                test1_subtle_trials.addData('mouse_test1_subtle.time', mouse_test1_subtle.time)
                test1_subtle_trials.addData('mouse_test1_subtle.clicked_name', mouse_test1_subtle.clicked_name)
                # the Routine "test1_subtle_choice" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "test1_subtle_rate" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                slider_test1_subtle.reset()
                slider_target_test1_subtle.setPos(target_position)
                slider_target_test1_subtle.setImage(stim1)
                slider_distractor_test1_subtle.setPos(distractor_position)
                slider_distractor_test1_subtle.setImage(distractor)
                # Run 'Begin Routine' code from show_continue_rate_test1_subtle
                show_continue_test1_subtle = False
                continue_rate_test1_subtle.reset()
                # setup some python lists for storing info about the mouse_continue_test1_subtle
                mouse_continue_test1_subtle.clicked_name = []
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                test1_subtle_rateComponents = [slider_text_test1_subtle, slider_test1_subtle, slider_target_test1_subtle, slider_distractor_test1_subtle, continue_rate_test1_subtle, mouse_continue_test1_subtle]
                for thisComponent in test1_subtle_rateComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test1_subtle_rate" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *slider_text_test1_subtle* updates
                    if slider_text_test1_subtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_text_test1_subtle.frameNStart = frameN  # exact frame index
                        slider_text_test1_subtle.tStart = t  # local t and not account for scr refresh
                        slider_text_test1_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_text_test1_subtle, 'tStartRefresh')  # time at next scr refresh
                        slider_text_test1_subtle.setAutoDraw(True)
                    
                    # *slider_test1_subtle* updates
                    if slider_test1_subtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_test1_subtle.frameNStart = frameN  # exact frame index
                        slider_test1_subtle.tStart = t  # local t and not account for scr refresh
                        slider_test1_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_test1_subtle, 'tStartRefresh')  # time at next scr refresh
                        slider_test1_subtle.setAutoDraw(True)
                    
                    # *slider_target_test1_subtle* updates
                    if slider_target_test1_subtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_target_test1_subtle.frameNStart = frameN  # exact frame index
                        slider_target_test1_subtle.tStart = t  # local t and not account for scr refresh
                        slider_target_test1_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_target_test1_subtle, 'tStartRefresh')  # time at next scr refresh
                        slider_target_test1_subtle.setAutoDraw(True)
                    
                    # *slider_distractor_test1_subtle* updates
                    if slider_distractor_test1_subtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_distractor_test1_subtle.frameNStart = frameN  # exact frame index
                        slider_distractor_test1_subtle.tStart = t  # local t and not account for scr refresh
                        slider_distractor_test1_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_distractor_test1_subtle, 'tStartRefresh')  # time at next scr refresh
                        slider_distractor_test1_subtle.setAutoDraw(True)
                    # Run 'Each Frame' code from show_continue_rate_test1_subtle
                    slid = slider_test1_subtle.getRating()
                    
                    if slid is not None:
                        show_continue_test1_subtle = True
                                
                                
                    
                    
                    # *continue_rate_test1_subtle* updates
                    if continue_rate_test1_subtle.status == NOT_STARTED and show_continue_test1_subtle:
                        # keep track of start time/frame for later
                        continue_rate_test1_subtle.frameNStart = frameN  # exact frame index
                        continue_rate_test1_subtle.tStart = t  # local t and not account for scr refresh
                        continue_rate_test1_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(continue_rate_test1_subtle, 'tStartRefresh')  # time at next scr refresh
                        continue_rate_test1_subtle.setAutoDraw(True)
                    # *mouse_continue_test1_subtle* updates
                    if mouse_continue_test1_subtle.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_continue_test1_subtle.frameNStart = frameN  # exact frame index
                        mouse_continue_test1_subtle.tStart = t  # local t and not account for scr refresh
                        mouse_continue_test1_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_continue_test1_subtle, 'tStartRefresh')  # time at next scr refresh
                        mouse_continue_test1_subtle.status = STARTED
                        mouse_continue_test1_subtle.mouseClock.reset()
                        prevButtonState = mouse_continue_test1_subtle.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_continue_test1_subtle.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_continue_test1_subtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter(continue_rate_test1_subtle)
                                    clickableList = continue_rate_test1_subtle
                                except:
                                    clickableList = [continue_rate_test1_subtle]
                                for obj in clickableList:
                                    if obj.contains(mouse_continue_test1_subtle):
                                        gotValidClick = True
                                        mouse_continue_test1_subtle.clicked_name.append(obj.name)
                                if gotValidClick:  
                                    continueRoutine = False  # abort routine on response
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test1_subtle_rateComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test1_subtle_rate" ---
                for thisComponent in test1_subtle_rateComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                test1_subtle_trials.addData('slider_test1_subtle.response', slider_test1_subtle.getRating())
                test1_subtle_trials.addData('slider_test1_subtle.rt', slider_test1_subtle.getRT())
                # store data for test1_subtle_trials (TrialHandler)
                # the Routine "test1_subtle_rate" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'test1_subtle_trials'
            
            
            # set up handler to look after randomisation of conditions etc
            task3_instr_subtle = data.TrialHandler(nReps=1.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('task3_instructions.xlsx'),
                seed=None, name='task3_instr_subtle')
            thisExp.addLoop(task3_instr_subtle)  # add the loop to the experiment
            thisTask3_instr_subtle = task3_instr_subtle.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTask3_instr_subtle.rgb)
            if thisTask3_instr_subtle != None:
                for paramName in thisTask3_instr_subtle:
                    exec('{} = thisTask3_instr_subtle[paramName]'.format(paramName))
            
            for thisTask3_instr_subtle in task3_instr_subtle:
                currentLoop = task3_instr_subtle
                # abbreviate parameter names if possible (e.g. rgb = thisTask3_instr_subtle.rgb)
                if thisTask3_instr_subtle != None:
                    for paramName in thisTask3_instr_subtle:
                        exec('{} = thisTask3_instr_subtle[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "test2_subtle_inst" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                cont_test2_subtle.reset()
                # setup some python lists for storing info about the cont_mouse_test2_subtle
                cont_mouse_test2_subtle.clicked_name = []
                gotValidClick = False  # until a click is received
                instructions_test2_subtle.setImage(task3)
                # keep track of which components have finished
                test2_subtle_instComponents = [cont_test2_subtle, cont_mouse_test2_subtle, instructions_test2_subtle]
                for thisComponent in test2_subtle_instComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test2_subtle_inst" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *cont_test2_subtle* updates
                    if cont_test2_subtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_test2_subtle.frameNStart = frameN  # exact frame index
                        cont_test2_subtle.tStart = t  # local t and not account for scr refresh
                        cont_test2_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_test2_subtle, 'tStartRefresh')  # time at next scr refresh
                        cont_test2_subtle.setAutoDraw(True)
                    # *cont_mouse_test2_subtle* updates
                    if cont_mouse_test2_subtle.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_mouse_test2_subtle.frameNStart = frameN  # exact frame index
                        cont_mouse_test2_subtle.tStart = t  # local t and not account for scr refresh
                        cont_mouse_test2_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_mouse_test2_subtle, 'tStartRefresh')  # time at next scr refresh
                        cont_mouse_test2_subtle.status = STARTED
                        cont_mouse_test2_subtle.mouseClock.reset()
                        prevButtonState = cont_mouse_test2_subtle.getPressed()  # if button is down already this ISN'T a new click
                    if cont_mouse_test2_subtle.status == STARTED:  # only update if started and not finished!
                        buttons = cont_mouse_test2_subtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter(cont_test2_subtle)
                                    clickableList = cont_test2_subtle
                                except:
                                    clickableList = [cont_test2_subtle]
                                for obj in clickableList:
                                    if obj.contains(cont_mouse_test2_subtle):
                                        gotValidClick = True
                                        cont_mouse_test2_subtle.clicked_name.append(obj.name)
                                if gotValidClick:  
                                    continueRoutine = False  # abort routine on response
                    
                    # *instructions_test2_subtle* updates
                    if instructions_test2_subtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        instructions_test2_subtle.frameNStart = frameN  # exact frame index
                        instructions_test2_subtle.tStart = t  # local t and not account for scr refresh
                        instructions_test2_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(instructions_test2_subtle, 'tStartRefresh')  # time at next scr refresh
                        instructions_test2_subtle.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test2_subtle_instComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test2_subtle_inst" ---
                for thisComponent in test2_subtle_instComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store data for task3_instr_subtle (TrialHandler)
                # the Routine "test2_subtle_inst" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'task3_instr_subtle'
            
            
            # --- Prepare to start Routine "comprehension3" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            comp3_resp2.reset()
            comp3_resp1.reset()
            comp3_resp3.reset()
            # setup some python lists for storing info about the comp3_mouse
            comp3_mouse.x = []
            comp3_mouse.y = []
            comp3_mouse.leftButton = []
            comp3_mouse.midButton = []
            comp3_mouse.rightButton = []
            comp3_mouse.time = []
            comp3_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            comp3_mouse.mouseClock.reset()
            # keep track of which components have finished
            comprehension3Components = [comp3_resp2, comp3_resp1, comp3_resp3, comp3_mouse, check3]
            for thisComponent in comprehension3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "comprehension3" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *comp3_resp2* updates
                if comp3_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp3_resp2.frameNStart = frameN  # exact frame index
                    comp3_resp2.tStart = t  # local t and not account for scr refresh
                    comp3_resp2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp3_resp2, 'tStartRefresh')  # time at next scr refresh
                    comp3_resp2.setAutoDraw(True)
                
                # *comp3_resp1* updates
                if comp3_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp3_resp1.frameNStart = frameN  # exact frame index
                    comp3_resp1.tStart = t  # local t and not account for scr refresh
                    comp3_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp3_resp1, 'tStartRefresh')  # time at next scr refresh
                    comp3_resp1.setAutoDraw(True)
                
                # *comp3_resp3* updates
                if comp3_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp3_resp3.frameNStart = frameN  # exact frame index
                    comp3_resp3.tStart = t  # local t and not account for scr refresh
                    comp3_resp3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp3_resp3, 'tStartRefresh')  # time at next scr refresh
                    comp3_resp3.setAutoDraw(True)
                # *comp3_mouse* updates
                if comp3_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp3_mouse.frameNStart = frameN  # exact frame index
                    comp3_mouse.tStart = t  # local t and not account for scr refresh
                    comp3_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp3_mouse, 'tStartRefresh')  # time at next scr refresh
                    comp3_mouse.status = STARTED
                    prevButtonState = comp3_mouse.getPressed()  # if button is down already this ISN'T a new click
                if comp3_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = comp3_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([comp3_resp1, comp3_resp2, comp3_resp3])
                                clickableList = [comp3_resp1, comp3_resp2, comp3_resp3]
                            except:
                                clickableList = [[comp3_resp1, comp3_resp2, comp3_resp3]]
                            for obj in clickableList:
                                if obj.contains(comp3_mouse):
                                    gotValidClick = True
                                    comp3_mouse.clicked_name.append(obj.name)
                            x, y = comp3_mouse.getPos()
                            comp3_mouse.x.append(x)
                            comp3_mouse.y.append(y)
                            buttons = comp3_mouse.getPressed()
                            comp3_mouse.leftButton.append(buttons[0])
                            comp3_mouse.midButton.append(buttons[1])
                            comp3_mouse.rightButton.append(buttons[2])
                            comp3_mouse.time.append(comp3_mouse.mouseClock.getTime())
                            if gotValidClick:
                                continueRoutine = False  # abort routine on response
                
                # *check3* updates
                if check3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    check3.frameNStart = frameN  # exact frame index
                    check3.tStart = t  # local t and not account for scr refresh
                    check3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(check3, 'tStartRefresh')  # time at next scr refresh
                    check3.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in comprehension3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "comprehension3" ---
            for thisComponent in comprehension3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for subtle_loop (TrialHandler)
            subtle_loop.addData('comp3_mouse.x', comp3_mouse.x)
            subtle_loop.addData('comp3_mouse.y', comp3_mouse.y)
            subtle_loop.addData('comp3_mouse.leftButton', comp3_mouse.leftButton)
            subtle_loop.addData('comp3_mouse.midButton', comp3_mouse.midButton)
            subtle_loop.addData('comp3_mouse.rightButton', comp3_mouse.rightButton)
            subtle_loop.addData('comp3_mouse.time', comp3_mouse.time)
            subtle_loop.addData('comp3_mouse.clicked_name', comp3_mouse.clicked_name)
            # the Routine "comprehension3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            test2_subtle_trials = data.TrialHandler(nReps=1.0, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('test2_trials.xlsx'),
                seed=None, name='test2_subtle_trials')
            thisExp.addLoop(test2_subtle_trials)  # add the loop to the experiment
            thisTest2_subtle_trial = test2_subtle_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTest2_subtle_trial.rgb)
            if thisTest2_subtle_trial != None:
                for paramName in thisTest2_subtle_trial:
                    exec('{} = thisTest2_subtle_trial[paramName]'.format(paramName))
            
            for thisTest2_subtle_trial in test2_subtle_trials:
                currentLoop = test2_subtle_trials
                # abbreviate parameter names if possible (e.g. rgb = thisTest2_subtle_trial.rgb)
                if thisTest2_subtle_trial != None:
                    for paramName in thisTest2_subtle_trial:
                        exec('{} = thisTest2_subtle_trial[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "test2_subtle_choice" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                # Run 'Begin Routine' code from target_determination_test2_subtle
                if target == 1:
                    stim1 = reorder_cues[0]
                elif target == 2:
                    stim1 = reorder_cues[1]
                elif target == 5:
                    stim1 = reorder_cues[4]
                elif target == 6:
                    stim1 = reorder_cues[5]
                # Run 'Begin Routine' code from distractor_presentation_test2_subtle
                if distractor_test2 == 1:
                    distractor = reorder_subtle[0]
                elif distractor_test2 == 2:
                    distractor = reorder_subtle[1]
                elif distractor_test2 == 5:
                    distractor = reorder_subtle[4]
                elif distractor_test2 == 6:
                    distractor = reorder_subtle[5]
                target_test2_subtle.setPos(target_position)
                target_test2_subtle.setImage(stim1)
                distractor_test2_subtle.setPos(distractor_position)
                distractor_test2_subtle.setImage(distractor)
                # setup some python lists for storing info about the mouse_test2_subtle
                mouse_test2_subtle.x = []
                mouse_test2_subtle.y = []
                mouse_test2_subtle.leftButton = []
                mouse_test2_subtle.midButton = []
                mouse_test2_subtle.rightButton = []
                mouse_test2_subtle.time = []
                mouse_test2_subtle.clicked_name = []
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                test2_subtle_choiceComponents = [blank_test2_subtle, target_test2_subtle, distractor_test2_subtle, mouse_test2_subtle]
                for thisComponent in test2_subtle_choiceComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test2_subtle_choice" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *blank_test2_subtle* updates
                    if blank_test2_subtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        blank_test2_subtle.frameNStart = frameN  # exact frame index
                        blank_test2_subtle.tStart = t  # local t and not account for scr refresh
                        blank_test2_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(blank_test2_subtle, 'tStartRefresh')  # time at next scr refresh
                        blank_test2_subtle.setAutoDraw(True)
                    if blank_test2_subtle.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > blank_test2_subtle.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            blank_test2_subtle.tStop = t  # not accounting for scr refresh
                            blank_test2_subtle.frameNStop = frameN  # exact frame index
                            blank_test2_subtle.setAutoDraw(False)
                    
                    # *target_test2_subtle* updates
                    if target_test2_subtle.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        target_test2_subtle.frameNStart = frameN  # exact frame index
                        target_test2_subtle.tStart = t  # local t and not account for scr refresh
                        target_test2_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(target_test2_subtle, 'tStartRefresh')  # time at next scr refresh
                        target_test2_subtle.setAutoDraw(True)
                    
                    # *distractor_test2_subtle* updates
                    if distractor_test2_subtle.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        distractor_test2_subtle.frameNStart = frameN  # exact frame index
                        distractor_test2_subtle.tStart = t  # local t and not account for scr refresh
                        distractor_test2_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(distractor_test2_subtle, 'tStartRefresh')  # time at next scr refresh
                        distractor_test2_subtle.setAutoDraw(True)
                    # *mouse_test2_subtle* updates
                    if mouse_test2_subtle.status == NOT_STARTED and t >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_test2_subtle.frameNStart = frameN  # exact frame index
                        mouse_test2_subtle.tStart = t  # local t and not account for scr refresh
                        mouse_test2_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_test2_subtle, 'tStartRefresh')  # time at next scr refresh
                        mouse_test2_subtle.status = STARTED
                        mouse_test2_subtle.mouseClock.reset()
                        prevButtonState = mouse_test2_subtle.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_test2_subtle.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_test2_subtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter([target_test2_subtle, distractor_test2_subtle])
                                    clickableList = [target_test2_subtle, distractor_test2_subtle]
                                except:
                                    clickableList = [[target_test2_subtle, distractor_test2_subtle]]
                                for obj in clickableList:
                                    if obj.contains(mouse_test2_subtle):
                                        gotValidClick = True
                                        mouse_test2_subtle.clicked_name.append(obj.name)
                                if gotValidClick:
                                    x, y = mouse_test2_subtle.getPos()
                                    mouse_test2_subtle.x.append(x)
                                    mouse_test2_subtle.y.append(y)
                                    buttons = mouse_test2_subtle.getPressed()
                                    mouse_test2_subtle.leftButton.append(buttons[0])
                                    mouse_test2_subtle.midButton.append(buttons[1])
                                    mouse_test2_subtle.rightButton.append(buttons[2])
                                    mouse_test2_subtle.time.append(mouse_test2_subtle.mouseClock.getTime())
                                if gotValidClick:
                                    continueRoutine = False  # abort routine on response
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test2_subtle_choiceComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test2_subtle_choice" ---
                for thisComponent in test2_subtle_choiceComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store data for test2_subtle_trials (TrialHandler)
                test2_subtle_trials.addData('mouse_test2_subtle.x', mouse_test2_subtle.x)
                test2_subtle_trials.addData('mouse_test2_subtle.y', mouse_test2_subtle.y)
                test2_subtle_trials.addData('mouse_test2_subtle.leftButton', mouse_test2_subtle.leftButton)
                test2_subtle_trials.addData('mouse_test2_subtle.midButton', mouse_test2_subtle.midButton)
                test2_subtle_trials.addData('mouse_test2_subtle.rightButton', mouse_test2_subtle.rightButton)
                test2_subtle_trials.addData('mouse_test2_subtle.time', mouse_test2_subtle.time)
                test2_subtle_trials.addData('mouse_test2_subtle.clicked_name', mouse_test2_subtle.clicked_name)
                # the Routine "test2_subtle_choice" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "test2_subtle_rate" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                slider_test2_subtle.reset()
                slider_target_test2_subtle.setPos(target_position)
                slider_target_test2_subtle.setImage(stim1)
                slider_distractor_test2_subtle.setPos(distractor_position)
                slider_distractor_test2_subtle.setImage(distractor)
                # Run 'Begin Routine' code from show_continue_rate_test2_subtle
                show_continue_test2_subtle = False
                continue_rate_test2_subtle.reset()
                # setup some python lists for storing info about the mouse_continue_test2_subtle
                mouse_continue_test2_subtle.clicked_name = []
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                test2_subtle_rateComponents = [slider_text_test2_subtle, slider_test2_subtle, slider_target_test2_subtle, slider_distractor_test2_subtle, continue_rate_test2_subtle, mouse_continue_test2_subtle]
                for thisComponent in test2_subtle_rateComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test2_subtle_rate" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *slider_text_test2_subtle* updates
                    if slider_text_test2_subtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_text_test2_subtle.frameNStart = frameN  # exact frame index
                        slider_text_test2_subtle.tStart = t  # local t and not account for scr refresh
                        slider_text_test2_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_text_test2_subtle, 'tStartRefresh')  # time at next scr refresh
                        slider_text_test2_subtle.setAutoDraw(True)
                    
                    # *slider_test2_subtle* updates
                    if slider_test2_subtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_test2_subtle.frameNStart = frameN  # exact frame index
                        slider_test2_subtle.tStart = t  # local t and not account for scr refresh
                        slider_test2_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_test2_subtle, 'tStartRefresh')  # time at next scr refresh
                        slider_test2_subtle.setAutoDraw(True)
                    
                    # *slider_target_test2_subtle* updates
                    if slider_target_test2_subtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_target_test2_subtle.frameNStart = frameN  # exact frame index
                        slider_target_test2_subtle.tStart = t  # local t and not account for scr refresh
                        slider_target_test2_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_target_test2_subtle, 'tStartRefresh')  # time at next scr refresh
                        slider_target_test2_subtle.setAutoDraw(True)
                    
                    # *slider_distractor_test2_subtle* updates
                    if slider_distractor_test2_subtle.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_distractor_test2_subtle.frameNStart = frameN  # exact frame index
                        slider_distractor_test2_subtle.tStart = t  # local t and not account for scr refresh
                        slider_distractor_test2_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_distractor_test2_subtle, 'tStartRefresh')  # time at next scr refresh
                        slider_distractor_test2_subtle.setAutoDraw(True)
                    # Run 'Each Frame' code from show_continue_rate_test2_subtle
                    slid = slider_test2_subtle.getRating()
                    
                    if slid is not None:
                        show_continue_test2_subtle = True
                                
                                
                    
                    
                    # *continue_rate_test2_subtle* updates
                    if continue_rate_test2_subtle.status == NOT_STARTED and show_continue_test2_subtle:
                        # keep track of start time/frame for later
                        continue_rate_test2_subtle.frameNStart = frameN  # exact frame index
                        continue_rate_test2_subtle.tStart = t  # local t and not account for scr refresh
                        continue_rate_test2_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(continue_rate_test2_subtle, 'tStartRefresh')  # time at next scr refresh
                        continue_rate_test2_subtle.setAutoDraw(True)
                    # *mouse_continue_test2_subtle* updates
                    if mouse_continue_test2_subtle.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_continue_test2_subtle.frameNStart = frameN  # exact frame index
                        mouse_continue_test2_subtle.tStart = t  # local t and not account for scr refresh
                        mouse_continue_test2_subtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_continue_test2_subtle, 'tStartRefresh')  # time at next scr refresh
                        mouse_continue_test2_subtle.status = STARTED
                        mouse_continue_test2_subtle.mouseClock.reset()
                        prevButtonState = mouse_continue_test2_subtle.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_continue_test2_subtle.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_continue_test2_subtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter(continue_rate_test2_subtle)
                                    clickableList = continue_rate_test2_subtle
                                except:
                                    clickableList = [continue_rate_test2_subtle]
                                for obj in clickableList:
                                    if obj.contains(mouse_continue_test2_subtle):
                                        gotValidClick = True
                                        mouse_continue_test2_subtle.clicked_name.append(obj.name)
                                if gotValidClick:  
                                    continueRoutine = False  # abort routine on response
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test2_subtle_rateComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test2_subtle_rate" ---
                for thisComponent in test2_subtle_rateComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                test2_subtle_trials.addData('slider_test2_subtle.response', slider_test2_subtle.getRating())
                test2_subtle_trials.addData('slider_test2_subtle.rt', slider_test2_subtle.getRT())
                # store data for test2_subtle_trials (TrialHandler)
                # the Routine "test2_subtle_rate" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'test2_subtle_trials'
            
            thisExp.nextEntry()
            
        # completed 0.0 repeats of 'subtle_loop'
        
        
        # set up handler to look after randomisation of conditions etc
        nosubtle_loop = data.TrialHandler(nReps=0.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='nosubtle_loop')
        thisExp.addLoop(nosubtle_loop)  # add the loop to the experiment
        thisNosubtle_loop = nosubtle_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisNosubtle_loop.rgb)
        if thisNosubtle_loop != None:
            for paramName in thisNosubtle_loop:
                exec('{} = thisNosubtle_loop[paramName]'.format(paramName))
        
        for thisNosubtle_loop in nosubtle_loop:
            currentLoop = nosubtle_loop
            # abbreviate parameter names if possible (e.g. rgb = thisNosubtle_loop.rgb)
            if thisNosubtle_loop != None:
                for paramName in thisNosubtle_loop:
                    exec('{} = thisNosubtle_loop[paramName]'.format(paramName))
            
            # set up handler to look after randomisation of conditions etc
            task2_instr_nosubtle = data.TrialHandler(nReps=1.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('task2_instructions.xlsx'),
                seed=None, name='task2_instr_nosubtle')
            thisExp.addLoop(task2_instr_nosubtle)  # add the loop to the experiment
            thisTask2_instr_nosubtle = task2_instr_nosubtle.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTask2_instr_nosubtle.rgb)
            if thisTask2_instr_nosubtle != None:
                for paramName in thisTask2_instr_nosubtle:
                    exec('{} = thisTask2_instr_nosubtle[paramName]'.format(paramName))
            
            for thisTask2_instr_nosubtle in task2_instr_nosubtle:
                currentLoop = task2_instr_nosubtle
                # abbreviate parameter names if possible (e.g. rgb = thisTask2_instr_nosubtle.rgb)
                if thisTask2_instr_nosubtle != None:
                    for paramName in thisTask2_instr_nosubtle:
                        exec('{} = thisTask2_instr_nosubtle[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "test1_nosubtle_inst" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                cont_test1_nosubtle.reset()
                # setup some python lists for storing info about the cont_mouse_test1_nosubtle
                cont_mouse_test1_nosubtle.clicked_name = []
                gotValidClick = False  # until a click is received
                instructions_test1_nosubtle.setImage(task2)
                # keep track of which components have finished
                test1_nosubtle_instComponents = [cont_test1_nosubtle, cont_mouse_test1_nosubtle, instructions_test1_nosubtle]
                for thisComponent in test1_nosubtle_instComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test1_nosubtle_inst" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *cont_test1_nosubtle* updates
                    if cont_test1_nosubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_test1_nosubtle.frameNStart = frameN  # exact frame index
                        cont_test1_nosubtle.tStart = t  # local t and not account for scr refresh
                        cont_test1_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_test1_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        cont_test1_nosubtle.setAutoDraw(True)
                    # *cont_mouse_test1_nosubtle* updates
                    if cont_mouse_test1_nosubtle.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_mouse_test1_nosubtle.frameNStart = frameN  # exact frame index
                        cont_mouse_test1_nosubtle.tStart = t  # local t and not account for scr refresh
                        cont_mouse_test1_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_mouse_test1_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        cont_mouse_test1_nosubtle.status = STARTED
                        cont_mouse_test1_nosubtle.mouseClock.reset()
                        prevButtonState = cont_mouse_test1_nosubtle.getPressed()  # if button is down already this ISN'T a new click
                    if cont_mouse_test1_nosubtle.status == STARTED:  # only update if started and not finished!
                        buttons = cont_mouse_test1_nosubtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter(cont_test1_nosubtle)
                                    clickableList = cont_test1_nosubtle
                                except:
                                    clickableList = [cont_test1_nosubtle]
                                for obj in clickableList:
                                    if obj.contains(cont_mouse_test1_nosubtle):
                                        gotValidClick = True
                                        cont_mouse_test1_nosubtle.clicked_name.append(obj.name)
                                if gotValidClick:  
                                    continueRoutine = False  # abort routine on response
                    
                    # *instructions_test1_nosubtle* updates
                    if instructions_test1_nosubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        instructions_test1_nosubtle.frameNStart = frameN  # exact frame index
                        instructions_test1_nosubtle.tStart = t  # local t and not account for scr refresh
                        instructions_test1_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(instructions_test1_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        instructions_test1_nosubtle.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test1_nosubtle_instComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test1_nosubtle_inst" ---
                for thisComponent in test1_nosubtle_instComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store data for task2_instr_nosubtle (TrialHandler)
                # the Routine "test1_nosubtle_inst" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'task2_instr_nosubtle'
            
            
            # --- Prepare to start Routine "comprehension2" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            comp2_resp2.reset()
            comp2_resp1.reset()
            comp2_resp3.reset()
            # setup some python lists for storing info about the comp2_mouse
            comp2_mouse.x = []
            comp2_mouse.y = []
            comp2_mouse.leftButton = []
            comp2_mouse.midButton = []
            comp2_mouse.rightButton = []
            comp2_mouse.time = []
            comp2_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            comp2_mouse.mouseClock.reset()
            # keep track of which components have finished
            comprehension2Components = [comp2_resp2, comp2_resp1, comp2_resp3, comp2_mouse, check2]
            for thisComponent in comprehension2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "comprehension2" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *comp2_resp2* updates
                if comp2_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp2_resp2.frameNStart = frameN  # exact frame index
                    comp2_resp2.tStart = t  # local t and not account for scr refresh
                    comp2_resp2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp2_resp2, 'tStartRefresh')  # time at next scr refresh
                    comp2_resp2.setAutoDraw(True)
                
                # *comp2_resp1* updates
                if comp2_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp2_resp1.frameNStart = frameN  # exact frame index
                    comp2_resp1.tStart = t  # local t and not account for scr refresh
                    comp2_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp2_resp1, 'tStartRefresh')  # time at next scr refresh
                    comp2_resp1.setAutoDraw(True)
                
                # *comp2_resp3* updates
                if comp2_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp2_resp3.frameNStart = frameN  # exact frame index
                    comp2_resp3.tStart = t  # local t and not account for scr refresh
                    comp2_resp3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp2_resp3, 'tStartRefresh')  # time at next scr refresh
                    comp2_resp3.setAutoDraw(True)
                # *comp2_mouse* updates
                if comp2_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp2_mouse.frameNStart = frameN  # exact frame index
                    comp2_mouse.tStart = t  # local t and not account for scr refresh
                    comp2_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp2_mouse, 'tStartRefresh')  # time at next scr refresh
                    comp2_mouse.status = STARTED
                    prevButtonState = comp2_mouse.getPressed()  # if button is down already this ISN'T a new click
                if comp2_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = comp2_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([comp2_resp1, comp2_resp2, comp2_resp3])
                                clickableList = [comp2_resp1, comp2_resp2, comp2_resp3]
                            except:
                                clickableList = [[comp2_resp1, comp2_resp2, comp2_resp3]]
                            for obj in clickableList:
                                if obj.contains(comp2_mouse):
                                    gotValidClick = True
                                    comp2_mouse.clicked_name.append(obj.name)
                            x, y = comp2_mouse.getPos()
                            comp2_mouse.x.append(x)
                            comp2_mouse.y.append(y)
                            buttons = comp2_mouse.getPressed()
                            comp2_mouse.leftButton.append(buttons[0])
                            comp2_mouse.midButton.append(buttons[1])
                            comp2_mouse.rightButton.append(buttons[2])
                            comp2_mouse.time.append(comp2_mouse.mouseClock.getTime())
                            if gotValidClick:
                                continueRoutine = False  # abort routine on response
                
                # *check2* updates
                if check2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    check2.frameNStart = frameN  # exact frame index
                    check2.tStart = t  # local t and not account for scr refresh
                    check2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(check2, 'tStartRefresh')  # time at next scr refresh
                    check2.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in comprehension2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "comprehension2" ---
            for thisComponent in comprehension2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for nosubtle_loop (TrialHandler)
            nosubtle_loop.addData('comp2_mouse.x', comp2_mouse.x)
            nosubtle_loop.addData('comp2_mouse.y', comp2_mouse.y)
            nosubtle_loop.addData('comp2_mouse.leftButton', comp2_mouse.leftButton)
            nosubtle_loop.addData('comp2_mouse.midButton', comp2_mouse.midButton)
            nosubtle_loop.addData('comp2_mouse.rightButton', comp2_mouse.rightButton)
            nosubtle_loop.addData('comp2_mouse.time', comp2_mouse.time)
            nosubtle_loop.addData('comp2_mouse.clicked_name', comp2_mouse.clicked_name)
            # the Routine "comprehension2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            test1_nosubtle_trials = data.TrialHandler(nReps=1.0, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('test1_trials.xlsx'),
                seed=None, name='test1_nosubtle_trials')
            thisExp.addLoop(test1_nosubtle_trials)  # add the loop to the experiment
            thisTest1_nosubtle_trial = test1_nosubtle_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTest1_nosubtle_trial.rgb)
            if thisTest1_nosubtle_trial != None:
                for paramName in thisTest1_nosubtle_trial:
                    exec('{} = thisTest1_nosubtle_trial[paramName]'.format(paramName))
            
            for thisTest1_nosubtle_trial in test1_nosubtle_trials:
                currentLoop = test1_nosubtle_trials
                # abbreviate parameter names if possible (e.g. rgb = thisTest1_nosubtle_trial.rgb)
                if thisTest1_nosubtle_trial != None:
                    for paramName in thisTest1_nosubtle_trial:
                        exec('{} = thisTest1_nosubtle_trial[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "test1_nosubtle_choice" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                # Run 'Begin Routine' code from target_determination_test1_nosubtle
                if target == 1:
                    stim1 = reorder_cues[0]
                elif target == 2:
                    stim1 = reorder_cues[1]
                elif target == 5:
                    stim1 = reorder_cues[4]
                elif target == 6:
                    stim1 = reorder_cues[5]
                # Run 'Begin Routine' code from distractor_presentation_test1_nosubtle
                if target == 1:
                    distractor = reorder_nosubtle[0]
                elif target == 2:
                    distractor = reorder_nosubtle[1]
                elif target == 5:
                    distractor = reorder_nosubtle[4]
                elif target == 6:
                    distractor = reorder_nosubtle[5]
                target_test1_nosubtle.setPos(target_position)
                target_test1_nosubtle.setImage(stim1)
                distractor_test1_nosubtle.setPos(distractor_position)
                distractor_test1_nosubtle.setImage(distractor)
                # setup some python lists for storing info about the mouse_test1_nosubtle
                mouse_test1_nosubtle.x = []
                mouse_test1_nosubtle.y = []
                mouse_test1_nosubtle.leftButton = []
                mouse_test1_nosubtle.midButton = []
                mouse_test1_nosubtle.rightButton = []
                mouse_test1_nosubtle.time = []
                mouse_test1_nosubtle.clicked_name = []
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                test1_nosubtle_choiceComponents = [blank_test1_nosubtle, target_test1_nosubtle, distractor_test1_nosubtle, mouse_test1_nosubtle]
                for thisComponent in test1_nosubtle_choiceComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test1_nosubtle_choice" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *blank_test1_nosubtle* updates
                    if blank_test1_nosubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        blank_test1_nosubtle.frameNStart = frameN  # exact frame index
                        blank_test1_nosubtle.tStart = t  # local t and not account for scr refresh
                        blank_test1_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(blank_test1_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        blank_test1_nosubtle.setAutoDraw(True)
                    if blank_test1_nosubtle.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > blank_test1_nosubtle.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            blank_test1_nosubtle.tStop = t  # not accounting for scr refresh
                            blank_test1_nosubtle.frameNStop = frameN  # exact frame index
                            blank_test1_nosubtle.setAutoDraw(False)
                    
                    # *target_test1_nosubtle* updates
                    if target_test1_nosubtle.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        target_test1_nosubtle.frameNStart = frameN  # exact frame index
                        target_test1_nosubtle.tStart = t  # local t and not account for scr refresh
                        target_test1_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(target_test1_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        target_test1_nosubtle.setAutoDraw(True)
                    
                    # *distractor_test1_nosubtle* updates
                    if distractor_test1_nosubtle.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        distractor_test1_nosubtle.frameNStart = frameN  # exact frame index
                        distractor_test1_nosubtle.tStart = t  # local t and not account for scr refresh
                        distractor_test1_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(distractor_test1_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        distractor_test1_nosubtle.setAutoDraw(True)
                    # *mouse_test1_nosubtle* updates
                    if mouse_test1_nosubtle.status == NOT_STARTED and t >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_test1_nosubtle.frameNStart = frameN  # exact frame index
                        mouse_test1_nosubtle.tStart = t  # local t and not account for scr refresh
                        mouse_test1_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_test1_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        mouse_test1_nosubtle.status = STARTED
                        mouse_test1_nosubtle.mouseClock.reset()
                        prevButtonState = mouse_test1_nosubtle.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_test1_nosubtle.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_test1_nosubtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter([target_test1_nosubtle, distractor_test1_nosubtle])
                                    clickableList = [target_test1_nosubtle, distractor_test1_nosubtle]
                                except:
                                    clickableList = [[target_test1_nosubtle, distractor_test1_nosubtle]]
                                for obj in clickableList:
                                    if obj.contains(mouse_test1_nosubtle):
                                        gotValidClick = True
                                        mouse_test1_nosubtle.clicked_name.append(obj.name)
                                if gotValidClick:
                                    x, y = mouse_test1_nosubtle.getPos()
                                    mouse_test1_nosubtle.x.append(x)
                                    mouse_test1_nosubtle.y.append(y)
                                    buttons = mouse_test1_nosubtle.getPressed()
                                    mouse_test1_nosubtle.leftButton.append(buttons[0])
                                    mouse_test1_nosubtle.midButton.append(buttons[1])
                                    mouse_test1_nosubtle.rightButton.append(buttons[2])
                                    mouse_test1_nosubtle.time.append(mouse_test1_nosubtle.mouseClock.getTime())
                                if gotValidClick:
                                    continueRoutine = False  # abort routine on response
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test1_nosubtle_choiceComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test1_nosubtle_choice" ---
                for thisComponent in test1_nosubtle_choiceComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store data for test1_nosubtle_trials (TrialHandler)
                test1_nosubtle_trials.addData('mouse_test1_nosubtle.x', mouse_test1_nosubtle.x)
                test1_nosubtle_trials.addData('mouse_test1_nosubtle.y', mouse_test1_nosubtle.y)
                test1_nosubtle_trials.addData('mouse_test1_nosubtle.leftButton', mouse_test1_nosubtle.leftButton)
                test1_nosubtle_trials.addData('mouse_test1_nosubtle.midButton', mouse_test1_nosubtle.midButton)
                test1_nosubtle_trials.addData('mouse_test1_nosubtle.rightButton', mouse_test1_nosubtle.rightButton)
                test1_nosubtle_trials.addData('mouse_test1_nosubtle.time', mouse_test1_nosubtle.time)
                test1_nosubtle_trials.addData('mouse_test1_nosubtle.clicked_name', mouse_test1_nosubtle.clicked_name)
                # the Routine "test1_nosubtle_choice" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "test1_nosubtle_rate" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                slider_test1_nosubtle.reset()
                slider_target_test1_nosubtle.setPos(target_position)
                slider_target_test1_nosubtle.setImage(stim1)
                slider_distractor_test1_nosubtle.setPos(distractor_position)
                slider_distractor_test1_nosubtle.setImage(distractor)
                # Run 'Begin Routine' code from show_continue_rate_test1_nosubtle
                show_continue_test1_nosubtle = False
                continue_rate_test1_nosubtle.reset()
                # setup some python lists for storing info about the mouse_continue_test1_nosubtle
                mouse_continue_test1_nosubtle.clicked_name = []
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                test1_nosubtle_rateComponents = [slider_text_test1_nosubtle, slider_test1_nosubtle, slider_target_test1_nosubtle, slider_distractor_test1_nosubtle, continue_rate_test1_nosubtle, mouse_continue_test1_nosubtle]
                for thisComponent in test1_nosubtle_rateComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test1_nosubtle_rate" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *slider_text_test1_nosubtle* updates
                    if slider_text_test1_nosubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_text_test1_nosubtle.frameNStart = frameN  # exact frame index
                        slider_text_test1_nosubtle.tStart = t  # local t and not account for scr refresh
                        slider_text_test1_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_text_test1_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_text_test1_nosubtle.setAutoDraw(True)
                    
                    # *slider_test1_nosubtle* updates
                    if slider_test1_nosubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_test1_nosubtle.frameNStart = frameN  # exact frame index
                        slider_test1_nosubtle.tStart = t  # local t and not account for scr refresh
                        slider_test1_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_test1_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_test1_nosubtle.setAutoDraw(True)
                    
                    # *slider_target_test1_nosubtle* updates
                    if slider_target_test1_nosubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_target_test1_nosubtle.frameNStart = frameN  # exact frame index
                        slider_target_test1_nosubtle.tStart = t  # local t and not account for scr refresh
                        slider_target_test1_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_target_test1_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_target_test1_nosubtle.setAutoDraw(True)
                    
                    # *slider_distractor_test1_nosubtle* updates
                    if slider_distractor_test1_nosubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_distractor_test1_nosubtle.frameNStart = frameN  # exact frame index
                        slider_distractor_test1_nosubtle.tStart = t  # local t and not account for scr refresh
                        slider_distractor_test1_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_distractor_test1_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_distractor_test1_nosubtle.setAutoDraw(True)
                    # Run 'Each Frame' code from show_continue_rate_test1_nosubtle
                    slid = slider_test1_nosubtle.getRating()
                    
                    if slid is not None:
                        show_continue_test1_nosubtle = True
                                
                                
                    
                    
                    # *continue_rate_test1_nosubtle* updates
                    if continue_rate_test1_nosubtle.status == NOT_STARTED and show_continue_test1_nosubtle:
                        # keep track of start time/frame for later
                        continue_rate_test1_nosubtle.frameNStart = frameN  # exact frame index
                        continue_rate_test1_nosubtle.tStart = t  # local t and not account for scr refresh
                        continue_rate_test1_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(continue_rate_test1_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        continue_rate_test1_nosubtle.setAutoDraw(True)
                    # *mouse_continue_test1_nosubtle* updates
                    if mouse_continue_test1_nosubtle.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_continue_test1_nosubtle.frameNStart = frameN  # exact frame index
                        mouse_continue_test1_nosubtle.tStart = t  # local t and not account for scr refresh
                        mouse_continue_test1_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_continue_test1_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        mouse_continue_test1_nosubtle.status = STARTED
                        mouse_continue_test1_nosubtle.mouseClock.reset()
                        prevButtonState = mouse_continue_test1_nosubtle.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_continue_test1_nosubtle.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_continue_test1_nosubtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter(continue_rate_test1_nosubtle)
                                    clickableList = continue_rate_test1_nosubtle
                                except:
                                    clickableList = [continue_rate_test1_nosubtle]
                                for obj in clickableList:
                                    if obj.contains(mouse_continue_test1_nosubtle):
                                        gotValidClick = True
                                        mouse_continue_test1_nosubtle.clicked_name.append(obj.name)
                                if gotValidClick:  
                                    continueRoutine = False  # abort routine on response
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test1_nosubtle_rateComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test1_nosubtle_rate" ---
                for thisComponent in test1_nosubtle_rateComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                test1_nosubtle_trials.addData('slider_test1_nosubtle.response', slider_test1_nosubtle.getRating())
                test1_nosubtle_trials.addData('slider_test1_nosubtle.rt', slider_test1_nosubtle.getRT())
                # store data for test1_nosubtle_trials (TrialHandler)
                # the Routine "test1_nosubtle_rate" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'test1_nosubtle_trials'
            
            
            # set up handler to look after randomisation of conditions etc
            task3_instr_nosubtle = data.TrialHandler(nReps=1.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('task3_instructions.xlsx'),
                seed=None, name='task3_instr_nosubtle')
            thisExp.addLoop(task3_instr_nosubtle)  # add the loop to the experiment
            thisTask3_instr_nosubtle = task3_instr_nosubtle.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTask3_instr_nosubtle.rgb)
            if thisTask3_instr_nosubtle != None:
                for paramName in thisTask3_instr_nosubtle:
                    exec('{} = thisTask3_instr_nosubtle[paramName]'.format(paramName))
            
            for thisTask3_instr_nosubtle in task3_instr_nosubtle:
                currentLoop = task3_instr_nosubtle
                # abbreviate parameter names if possible (e.g. rgb = thisTask3_instr_nosubtle.rgb)
                if thisTask3_instr_nosubtle != None:
                    for paramName in thisTask3_instr_nosubtle:
                        exec('{} = thisTask3_instr_nosubtle[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "test2_nosubtle_inst" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                cont_test2_nosubtle.reset()
                # setup some python lists for storing info about the cont_mouse_test2_nosubtle
                cont_mouse_test2_nosubtle.clicked_name = []
                gotValidClick = False  # until a click is received
                instructions_test2_nosubtle.setImage(task3)
                # keep track of which components have finished
                test2_nosubtle_instComponents = [cont_test2_nosubtle, cont_mouse_test2_nosubtle, instructions_test2_nosubtle]
                for thisComponent in test2_nosubtle_instComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test2_nosubtle_inst" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *cont_test2_nosubtle* updates
                    if cont_test2_nosubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_test2_nosubtle.frameNStart = frameN  # exact frame index
                        cont_test2_nosubtle.tStart = t  # local t and not account for scr refresh
                        cont_test2_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_test2_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        cont_test2_nosubtle.setAutoDraw(True)
                    # *cont_mouse_test2_nosubtle* updates
                    if cont_mouse_test2_nosubtle.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_mouse_test2_nosubtle.frameNStart = frameN  # exact frame index
                        cont_mouse_test2_nosubtle.tStart = t  # local t and not account for scr refresh
                        cont_mouse_test2_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_mouse_test2_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        cont_mouse_test2_nosubtle.status = STARTED
                        cont_mouse_test2_nosubtle.mouseClock.reset()
                        prevButtonState = cont_mouse_test2_nosubtle.getPressed()  # if button is down already this ISN'T a new click
                    if cont_mouse_test2_nosubtle.status == STARTED:  # only update if started and not finished!
                        buttons = cont_mouse_test2_nosubtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter(cont_test2_nosubtle)
                                    clickableList = cont_test2_nosubtle
                                except:
                                    clickableList = [cont_test2_nosubtle]
                                for obj in clickableList:
                                    if obj.contains(cont_mouse_test2_nosubtle):
                                        gotValidClick = True
                                        cont_mouse_test2_nosubtle.clicked_name.append(obj.name)
                                if gotValidClick:  
                                    continueRoutine = False  # abort routine on response
                    
                    # *instructions_test2_nosubtle* updates
                    if instructions_test2_nosubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        instructions_test2_nosubtle.frameNStart = frameN  # exact frame index
                        instructions_test2_nosubtle.tStart = t  # local t and not account for scr refresh
                        instructions_test2_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(instructions_test2_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        instructions_test2_nosubtle.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test2_nosubtle_instComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test2_nosubtle_inst" ---
                for thisComponent in test2_nosubtle_instComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store data for task3_instr_nosubtle (TrialHandler)
                # the Routine "test2_nosubtle_inst" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'task3_instr_nosubtle'
            
            
            # --- Prepare to start Routine "comprehension3" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            comp3_resp2.reset()
            comp3_resp1.reset()
            comp3_resp3.reset()
            # setup some python lists for storing info about the comp3_mouse
            comp3_mouse.x = []
            comp3_mouse.y = []
            comp3_mouse.leftButton = []
            comp3_mouse.midButton = []
            comp3_mouse.rightButton = []
            comp3_mouse.time = []
            comp3_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            comp3_mouse.mouseClock.reset()
            # keep track of which components have finished
            comprehension3Components = [comp3_resp2, comp3_resp1, comp3_resp3, comp3_mouse, check3]
            for thisComponent in comprehension3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "comprehension3" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *comp3_resp2* updates
                if comp3_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp3_resp2.frameNStart = frameN  # exact frame index
                    comp3_resp2.tStart = t  # local t and not account for scr refresh
                    comp3_resp2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp3_resp2, 'tStartRefresh')  # time at next scr refresh
                    comp3_resp2.setAutoDraw(True)
                
                # *comp3_resp1* updates
                if comp3_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp3_resp1.frameNStart = frameN  # exact frame index
                    comp3_resp1.tStart = t  # local t and not account for scr refresh
                    comp3_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp3_resp1, 'tStartRefresh')  # time at next scr refresh
                    comp3_resp1.setAutoDraw(True)
                
                # *comp3_resp3* updates
                if comp3_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp3_resp3.frameNStart = frameN  # exact frame index
                    comp3_resp3.tStart = t  # local t and not account for scr refresh
                    comp3_resp3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp3_resp3, 'tStartRefresh')  # time at next scr refresh
                    comp3_resp3.setAutoDraw(True)
                # *comp3_mouse* updates
                if comp3_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp3_mouse.frameNStart = frameN  # exact frame index
                    comp3_mouse.tStart = t  # local t and not account for scr refresh
                    comp3_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp3_mouse, 'tStartRefresh')  # time at next scr refresh
                    comp3_mouse.status = STARTED
                    prevButtonState = comp3_mouse.getPressed()  # if button is down already this ISN'T a new click
                if comp3_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = comp3_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([comp3_resp1, comp3_resp2, comp3_resp3])
                                clickableList = [comp3_resp1, comp3_resp2, comp3_resp3]
                            except:
                                clickableList = [[comp3_resp1, comp3_resp2, comp3_resp3]]
                            for obj in clickableList:
                                if obj.contains(comp3_mouse):
                                    gotValidClick = True
                                    comp3_mouse.clicked_name.append(obj.name)
                            x, y = comp3_mouse.getPos()
                            comp3_mouse.x.append(x)
                            comp3_mouse.y.append(y)
                            buttons = comp3_mouse.getPressed()
                            comp3_mouse.leftButton.append(buttons[0])
                            comp3_mouse.midButton.append(buttons[1])
                            comp3_mouse.rightButton.append(buttons[2])
                            comp3_mouse.time.append(comp3_mouse.mouseClock.getTime())
                            if gotValidClick:
                                continueRoutine = False  # abort routine on response
                
                # *check3* updates
                if check3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    check3.frameNStart = frameN  # exact frame index
                    check3.tStart = t  # local t and not account for scr refresh
                    check3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(check3, 'tStartRefresh')  # time at next scr refresh
                    check3.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in comprehension3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "comprehension3" ---
            for thisComponent in comprehension3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for nosubtle_loop (TrialHandler)
            nosubtle_loop.addData('comp3_mouse.x', comp3_mouse.x)
            nosubtle_loop.addData('comp3_mouse.y', comp3_mouse.y)
            nosubtle_loop.addData('comp3_mouse.leftButton', comp3_mouse.leftButton)
            nosubtle_loop.addData('comp3_mouse.midButton', comp3_mouse.midButton)
            nosubtle_loop.addData('comp3_mouse.rightButton', comp3_mouse.rightButton)
            nosubtle_loop.addData('comp3_mouse.time', comp3_mouse.time)
            nosubtle_loop.addData('comp3_mouse.clicked_name', comp3_mouse.clicked_name)
            # the Routine "comprehension3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            test2_nosubtle_trials = data.TrialHandler(nReps=1.0, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('test2_trials.xlsx'),
                seed=None, name='test2_nosubtle_trials')
            thisExp.addLoop(test2_nosubtle_trials)  # add the loop to the experiment
            thisTest2_nosubtle_trial = test2_nosubtle_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTest2_nosubtle_trial.rgb)
            if thisTest2_nosubtle_trial != None:
                for paramName in thisTest2_nosubtle_trial:
                    exec('{} = thisTest2_nosubtle_trial[paramName]'.format(paramName))
            
            for thisTest2_nosubtle_trial in test2_nosubtle_trials:
                currentLoop = test2_nosubtle_trials
                # abbreviate parameter names if possible (e.g. rgb = thisTest2_nosubtle_trial.rgb)
                if thisTest2_nosubtle_trial != None:
                    for paramName in thisTest2_nosubtle_trial:
                        exec('{} = thisTest2_nosubtle_trial[paramName]'.format(paramName))
                
                # --- Prepare to start Routine "test2_nosubtle_choice" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                # Run 'Begin Routine' code from target_determination_test2_nosubtle
                if target == 1:
                    stim1 = reorder_cues[0]
                elif target == 2:
                    stim1 = reorder_cues[1]
                elif target == 5:
                    stim1 = reorder_cues[4]
                elif target == 6:
                    stim1 = reorder_cues[5]
                # Run 'Begin Routine' code from distractor_presentation_test2_nosubtle
                if distractor_test2 == 1:
                    distractor = reorder_nosubtle[0]
                elif distractor_test2 == 2:
                    distractor = reorder_nosubtle[1]
                elif distractor_test2 == 5:
                    distractor = reorder_nosubtle[4]
                elif distractor_test2 == 6:
                    distractor = reorder_nosubtle[5]
                target_test2_nosubtle.setPos(target_position)
                target_test2_nosubtle.setImage(stim1)
                distractor_test2_nosubtle.setPos(distractor_position)
                distractor_test2_nosubtle.setImage(distractor)
                # setup some python lists for storing info about the mouse_test2_nosubtle
                mouse_test2_nosubtle.x = []
                mouse_test2_nosubtle.y = []
                mouse_test2_nosubtle.leftButton = []
                mouse_test2_nosubtle.midButton = []
                mouse_test2_nosubtle.rightButton = []
                mouse_test2_nosubtle.time = []
                mouse_test2_nosubtle.clicked_name = []
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                test2_nosubtle_choiceComponents = [blank_test2_nosubtle, target_test2_nosubtle, distractor_test2_nosubtle, mouse_test2_nosubtle]
                for thisComponent in test2_nosubtle_choiceComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test2_nosubtle_choice" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *blank_test2_nosubtle* updates
                    if blank_test2_nosubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        blank_test2_nosubtle.frameNStart = frameN  # exact frame index
                        blank_test2_nosubtle.tStart = t  # local t and not account for scr refresh
                        blank_test2_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(blank_test2_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        blank_test2_nosubtle.setAutoDraw(True)
                    if blank_test2_nosubtle.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > blank_test2_nosubtle.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            blank_test2_nosubtle.tStop = t  # not accounting for scr refresh
                            blank_test2_nosubtle.frameNStop = frameN  # exact frame index
                            blank_test2_nosubtle.setAutoDraw(False)
                    
                    # *target_test2_nosubtle* updates
                    if target_test2_nosubtle.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        target_test2_nosubtle.frameNStart = frameN  # exact frame index
                        target_test2_nosubtle.tStart = t  # local t and not account for scr refresh
                        target_test2_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(target_test2_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        target_test2_nosubtle.setAutoDraw(True)
                    
                    # *distractor_test2_nosubtle* updates
                    if distractor_test2_nosubtle.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        distractor_test2_nosubtle.frameNStart = frameN  # exact frame index
                        distractor_test2_nosubtle.tStart = t  # local t and not account for scr refresh
                        distractor_test2_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(distractor_test2_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        distractor_test2_nosubtle.setAutoDraw(True)
                    # *mouse_test2_nosubtle* updates
                    if mouse_test2_nosubtle.status == NOT_STARTED and t >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_test2_nosubtle.frameNStart = frameN  # exact frame index
                        mouse_test2_nosubtle.tStart = t  # local t and not account for scr refresh
                        mouse_test2_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_test2_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        mouse_test2_nosubtle.status = STARTED
                        mouse_test2_nosubtle.mouseClock.reset()
                        prevButtonState = mouse_test2_nosubtle.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_test2_nosubtle.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_test2_nosubtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter([target_test2_nosubtle, distractor_test2_nosubtle])
                                    clickableList = [target_test2_nosubtle, distractor_test2_nosubtle]
                                except:
                                    clickableList = [[target_test2_nosubtle, distractor_test2_nosubtle]]
                                for obj in clickableList:
                                    if obj.contains(mouse_test2_nosubtle):
                                        gotValidClick = True
                                        mouse_test2_nosubtle.clicked_name.append(obj.name)
                                if gotValidClick:
                                    x, y = mouse_test2_nosubtle.getPos()
                                    mouse_test2_nosubtle.x.append(x)
                                    mouse_test2_nosubtle.y.append(y)
                                    buttons = mouse_test2_nosubtle.getPressed()
                                    mouse_test2_nosubtle.leftButton.append(buttons[0])
                                    mouse_test2_nosubtle.midButton.append(buttons[1])
                                    mouse_test2_nosubtle.rightButton.append(buttons[2])
                                    mouse_test2_nosubtle.time.append(mouse_test2_nosubtle.mouseClock.getTime())
                                if gotValidClick:
                                    continueRoutine = False  # abort routine on response
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test2_nosubtle_choiceComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test2_nosubtle_choice" ---
                for thisComponent in test2_nosubtle_choiceComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store data for test2_nosubtle_trials (TrialHandler)
                test2_nosubtle_trials.addData('mouse_test2_nosubtle.x', mouse_test2_nosubtle.x)
                test2_nosubtle_trials.addData('mouse_test2_nosubtle.y', mouse_test2_nosubtle.y)
                test2_nosubtle_trials.addData('mouse_test2_nosubtle.leftButton', mouse_test2_nosubtle.leftButton)
                test2_nosubtle_trials.addData('mouse_test2_nosubtle.midButton', mouse_test2_nosubtle.midButton)
                test2_nosubtle_trials.addData('mouse_test2_nosubtle.rightButton', mouse_test2_nosubtle.rightButton)
                test2_nosubtle_trials.addData('mouse_test2_nosubtle.time', mouse_test2_nosubtle.time)
                test2_nosubtle_trials.addData('mouse_test2_nosubtle.clicked_name', mouse_test2_nosubtle.clicked_name)
                # the Routine "test2_nosubtle_choice" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "test2_nosubtle_rate" ---
                continueRoutine = True
                routineForceEnded = False
                # update component parameters for each repeat
                slider_test2_nosubtle.reset()
                slider_target_test2_nosubtle.setPos(target_position)
                slider_target_test2_nosubtle.setImage(stim1)
                slider_distractor_test2_nosubtle.setPos(distractor_position)
                slider_distractor_test2_nosubtle.setImage(distractor)
                # Run 'Begin Routine' code from show_continue_rate_test2_nosubtle
                show_continue_test2_nosubtle = False
                continue_rate_test2_nosubtle.reset()
                # setup some python lists for storing info about the mouse_continue_test2_nosubtle
                mouse_continue_test2_nosubtle.clicked_name = []
                gotValidClick = False  # until a click is received
                # keep track of which components have finished
                test2_nosubtle_rateComponents = [slider_text_test2_nosubtle, slider_test2_nosubtle, slider_target_test2_nosubtle, slider_distractor_test2_nosubtle, continue_rate_test2_nosubtle, mouse_continue_test2_nosubtle]
                for thisComponent in test2_nosubtle_rateComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "test2_nosubtle_rate" ---
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *slider_text_test2_nosubtle* updates
                    if slider_text_test2_nosubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_text_test2_nosubtle.frameNStart = frameN  # exact frame index
                        slider_text_test2_nosubtle.tStart = t  # local t and not account for scr refresh
                        slider_text_test2_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_text_test2_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_text_test2_nosubtle.setAutoDraw(True)
                    
                    # *slider_test2_nosubtle* updates
                    if slider_test2_nosubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_test2_nosubtle.frameNStart = frameN  # exact frame index
                        slider_test2_nosubtle.tStart = t  # local t and not account for scr refresh
                        slider_test2_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_test2_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_test2_nosubtle.setAutoDraw(True)
                    
                    # *slider_target_test2_nosubtle* updates
                    if slider_target_test2_nosubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_target_test2_nosubtle.frameNStart = frameN  # exact frame index
                        slider_target_test2_nosubtle.tStart = t  # local t and not account for scr refresh
                        slider_target_test2_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_target_test2_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_target_test2_nosubtle.setAutoDraw(True)
                    
                    # *slider_distractor_test2_nosubtle* updates
                    if slider_distractor_test2_nosubtle.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        slider_distractor_test2_nosubtle.frameNStart = frameN  # exact frame index
                        slider_distractor_test2_nosubtle.tStart = t  # local t and not account for scr refresh
                        slider_distractor_test2_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(slider_distractor_test2_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        slider_distractor_test2_nosubtle.setAutoDraw(True)
                    # Run 'Each Frame' code from show_continue_rate_test2_nosubtle
                    slid = slider_test2_nosubtle.getRating()
                    
                    if slid is not None:
                        show_continue_test2_nosubtle = True
                                
                                
                    
                    
                    # *continue_rate_test2_nosubtle* updates
                    if continue_rate_test2_nosubtle.status == NOT_STARTED and show_continue_test2_nosubtle:
                        # keep track of start time/frame for later
                        continue_rate_test2_nosubtle.frameNStart = frameN  # exact frame index
                        continue_rate_test2_nosubtle.tStart = t  # local t and not account for scr refresh
                        continue_rate_test2_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(continue_rate_test2_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        continue_rate_test2_nosubtle.setAutoDraw(True)
                    # *mouse_continue_test2_nosubtle* updates
                    if mouse_continue_test2_nosubtle.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        mouse_continue_test2_nosubtle.frameNStart = frameN  # exact frame index
                        mouse_continue_test2_nosubtle.tStart = t  # local t and not account for scr refresh
                        mouse_continue_test2_nosubtle.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mouse_continue_test2_nosubtle, 'tStartRefresh')  # time at next scr refresh
                        mouse_continue_test2_nosubtle.status = STARTED
                        mouse_continue_test2_nosubtle.mouseClock.reset()
                        prevButtonState = mouse_continue_test2_nosubtle.getPressed()  # if button is down already this ISN'T a new click
                    if mouse_continue_test2_nosubtle.status == STARTED:  # only update if started and not finished!
                        buttons = mouse_continue_test2_nosubtle.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                try:
                                    iter(continue_rate_test2_nosubtle)
                                    clickableList = continue_rate_test2_nosubtle
                                except:
                                    clickableList = [continue_rate_test2_nosubtle]
                                for obj in clickableList:
                                    if obj.contains(mouse_continue_test2_nosubtle):
                                        gotValidClick = True
                                        mouse_continue_test2_nosubtle.clicked_name.append(obj.name)
                                if gotValidClick:  
                                    continueRoutine = False  # abort routine on response
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in test2_nosubtle_rateComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "test2_nosubtle_rate" ---
                for thisComponent in test2_nosubtle_rateComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                test2_nosubtle_trials.addData('slider_test2_nosubtle.response', slider_test2_nosubtle.getRating())
                test2_nosubtle_trials.addData('slider_test2_nosubtle.rt', slider_test2_nosubtle.getRT())
                # store data for test2_nosubtle_trials (TrialHandler)
                # the Routine "test2_nosubtle_rate" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'test2_nosubtle_trials'
            
            thisExp.nextEntry()
            
        # completed 0.0 repeats of 'nosubtle_loop'
        
        
        # set up handler to look after randomisation of conditions etc
        debrief_loop = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('debrief.xlsx'),
            seed=None, name='debrief_loop')
        thisExp.addLoop(debrief_loop)  # add the loop to the experiment
        thisDebrief_loop = debrief_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisDebrief_loop.rgb)
        if thisDebrief_loop != None:
            for paramName in thisDebrief_loop:
                exec('{} = thisDebrief_loop[paramName]'.format(paramName))
        
        for thisDebrief_loop in debrief_loop:
            currentLoop = debrief_loop
            # abbreviate parameter names if possible (e.g. rgb = thisDebrief_loop.rgb)
            if thisDebrief_loop != None:
                for paramName in thisDebrief_loop:
                    exec('{} = thisDebrief_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "debrief" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            cont_debrief.reset()
            # setup some python lists for storing info about the cont_debrief_mouse
            cont_debrief_mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            debrief_image.setImage(debrief_img)
            # keep track of which components have finished
            debriefComponents = [cont_debrief, cont_debrief_mouse, debrief_image]
            for thisComponent in debriefComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "debrief" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *cont_debrief* updates
                if cont_debrief.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cont_debrief.frameNStart = frameN  # exact frame index
                    cont_debrief.tStart = t  # local t and not account for scr refresh
                    cont_debrief.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cont_debrief, 'tStartRefresh')  # time at next scr refresh
                    cont_debrief.setAutoDraw(True)
                # *cont_debrief_mouse* updates
                if cont_debrief_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cont_debrief_mouse.frameNStart = frameN  # exact frame index
                    cont_debrief_mouse.tStart = t  # local t and not account for scr refresh
                    cont_debrief_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cont_debrief_mouse, 'tStartRefresh')  # time at next scr refresh
                    cont_debrief_mouse.status = STARTED
                    cont_debrief_mouse.mouseClock.reset()
                    prevButtonState = cont_debrief_mouse.getPressed()  # if button is down already this ISN'T a new click
                if cont_debrief_mouse.status == STARTED:  # only update if started and not finished!
                    buttons = cont_debrief_mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter(cont_debrief)
                                clickableList = cont_debrief
                            except:
                                clickableList = [cont_debrief]
                            for obj in clickableList:
                                if obj.contains(cont_debrief_mouse):
                                    gotValidClick = True
                                    cont_debrief_mouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                
                # *debrief_image* updates
                if debrief_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debrief_image.frameNStart = frameN  # exact frame index
                    debrief_image.tStart = t  # local t and not account for scr refresh
                    debrief_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debrief_image, 'tStartRefresh')  # time at next scr refresh
                    debrief_image.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in debriefComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "debrief" ---
            for thisComponent in debriefComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for debrief_loop (TrialHandler)
            # the Routine "debrief" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'debrief_loop'
        
        thisExp.nextEntry()
        
    # completed compr1_continue repeats of 'compr1_completed'
    
    
    # set up handler to look after randomisation of conditions etc
    no_compr_loop = data.TrialHandler(nReps=no_compr, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='no_compr_loop')
    thisExp.addLoop(no_compr_loop)  # add the loop to the experiment
    thisNo_compr_loop = no_compr_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNo_compr_loop.rgb)
    if thisNo_compr_loop != None:
        for paramName in thisNo_compr_loop:
            exec('{} = thisNo_compr_loop[paramName]'.format(paramName))
    
    for thisNo_compr_loop in no_compr_loop:
        currentLoop = no_compr_loop
        # abbreviate parameter names if possible (e.g. rgb = thisNo_compr_loop.rgb)
        if thisNo_compr_loop != None:
            for paramName in thisNo_compr_loop:
                exec('{} = thisNo_compr_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "no_comprehension" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        no_compr_textbox.reset()
        exit_box_no_compr.reset()
        # setup some python lists for storing info about the mouse_exit_no_compr
        mouse_exit_no_compr.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        no_comprehensionComponents = [no_compr_textbox, exit_box_no_compr, mouse_exit_no_compr]
        for thisComponent in no_comprehensionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "no_comprehension" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *no_compr_textbox* updates
            if no_compr_textbox.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                no_compr_textbox.frameNStart = frameN  # exact frame index
                no_compr_textbox.tStart = t  # local t and not account for scr refresh
                no_compr_textbox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no_compr_textbox, 'tStartRefresh')  # time at next scr refresh
                no_compr_textbox.setAutoDraw(True)
            
            # *exit_box_no_compr* updates
            if exit_box_no_compr.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                exit_box_no_compr.frameNStart = frameN  # exact frame index
                exit_box_no_compr.tStart = t  # local t and not account for scr refresh
                exit_box_no_compr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(exit_box_no_compr, 'tStartRefresh')  # time at next scr refresh
                exit_box_no_compr.setAutoDraw(True)
            # *mouse_exit_no_compr* updates
            if mouse_exit_no_compr.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                mouse_exit_no_compr.frameNStart = frameN  # exact frame index
                mouse_exit_no_compr.tStart = t  # local t and not account for scr refresh
                mouse_exit_no_compr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_exit_no_compr, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_exit_no_compr.started', t)
                mouse_exit_no_compr.status = STARTED
                mouse_exit_no_compr.mouseClock.reset()
                prevButtonState = mouse_exit_no_compr.getPressed()  # if button is down already this ISN'T a new click
            if mouse_exit_no_compr.status == STARTED:  # only update if started and not finished!
                buttons = mouse_exit_no_compr.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(exit_box_no_compr)
                            clickableList = exit_box_no_compr
                        except:
                            clickableList = [exit_box_no_compr]
                        for obj in clickableList:
                            if obj.contains(mouse_exit_no_compr):
                                gotValidClick = True
                                mouse_exit_no_compr.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in no_comprehensionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "no_comprehension" ---
        for thisComponent in no_comprehensionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for no_compr_loop (TrialHandler)
        # the Routine "no_comprehension" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed no_compr repeats of 'no_compr_loop'
    
    thisExp.nextEntry()
    
# completed consent repeats of 'consent_loop'


# set up handler to look after randomisation of conditions etc
no_consent_loop = data.TrialHandler(nReps=no_consent, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='no_consent_loop')
thisExp.addLoop(no_consent_loop)  # add the loop to the experiment
thisNo_consent_loop = no_consent_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNo_consent_loop.rgb)
if thisNo_consent_loop != None:
    for paramName in thisNo_consent_loop:
        exec('{} = thisNo_consent_loop[paramName]'.format(paramName))

for thisNo_consent_loop in no_consent_loop:
    currentLoop = no_consent_loop
    # abbreviate parameter names if possible (e.g. rgb = thisNo_consent_loop.rgb)
    if thisNo_consent_loop != None:
        for paramName in thisNo_consent_loop:
            exec('{} = thisNo_consent_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "no_consent_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    no_consent_textbox.reset()
    exit_box.reset()
    # setup some python lists for storing info about the mouse_exit
    mouse_exit.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    no_consent_trialComponents = [no_consent_textbox, exit_box, mouse_exit]
    for thisComponent in no_consent_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "no_consent_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *no_consent_textbox* updates
        if no_consent_textbox.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            no_consent_textbox.frameNStart = frameN  # exact frame index
            no_consent_textbox.tStart = t  # local t and not account for scr refresh
            no_consent_textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no_consent_textbox, 'tStartRefresh')  # time at next scr refresh
            no_consent_textbox.setAutoDraw(True)
        
        # *exit_box* updates
        if exit_box.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            exit_box.frameNStart = frameN  # exact frame index
            exit_box.tStart = t  # local t and not account for scr refresh
            exit_box.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exit_box, 'tStartRefresh')  # time at next scr refresh
            exit_box.setAutoDraw(True)
        # *mouse_exit* updates
        if mouse_exit.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse_exit.frameNStart = frameN  # exact frame index
            mouse_exit.tStart = t  # local t and not account for scr refresh
            mouse_exit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_exit, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_exit.started', t)
            mouse_exit.status = STARTED
            mouse_exit.mouseClock.reset()
            prevButtonState = mouse_exit.getPressed()  # if button is down already this ISN'T a new click
        if mouse_exit.status == STARTED:  # only update if started and not finished!
            buttons = mouse_exit.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(exit_box)
                        clickableList = exit_box
                    except:
                        clickableList = [exit_box]
                    for obj in clickableList:
                        if obj.contains(mouse_exit):
                            gotValidClick = True
                            mouse_exit.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in no_consent_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "no_consent_trial" ---
    for thisComponent in no_consent_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for no_consent_loop (TrialHandler)
    # the Routine "no_consent_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed no_consent repeats of 'no_consent_loop'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='comma')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
