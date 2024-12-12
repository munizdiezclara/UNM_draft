#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.1),
    on July 11, 2024, at 12:08
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.1'
expName = 'UNM08'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'age': '',
    'gender': ["male","female", "non-binary", "other"],
    'condition': f"{randint(1, 4)}",
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_loggingLevel = logging.getLevel('exp')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\munizdie\\OneDrive - Lancaster University\\Experiments\\Recognition Memory\\UNM08\\UNM08_experiment\\UNM08_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1920, 1080], fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "counterbalance" ---
    # Run 'Begin Experiment' code from counterbalance_2
    if int(expInfo['condition']) == 1:
        stage2File = "stage2_certain.xlsx"
        stage2Reps = 4
    elif int(expInfo['condition']) == 2:
        stage2File = "stage2_uncertain.xlsx"
        stage2Reps = 4
    elif int(expInfo['condition']) == 3:
        stage2File = "stage2_uncertain.xlsx"
        stage2Reps = 0
    
    # --- Initialize components for Routine "information" ---
    continue_info = visual.TextBox2(
         win, text='CONTINUE', placeholder='Type here...', font='Trebuchet MS',
         pos=(0, -0.45),     letterHeight=0.03,
         size=(0.2, 0.065), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='darkgrey', borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='continue_info',
         depth=0, autoLog=False,
    )
    mouse_info = event.Mouse(win=win)
    x, y = [None, None]
    mouse_info.mouseClock = core.Clock()
    image_info = visual.ImageStim(
        win=win,
        name='image_info', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.45, 0.75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "consent" ---
    c1 = visual.TextBox2(
         win, text='I agree to participate in the study on learning the predictive value of cues as described. I understand that my responses will be treated confidentially and that I have the option to withdraw from the study.', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.2, 0.35),     letterHeight=0.028,
         size=(0.7, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='c1',
         depth=0, autoLog=False,
    )
    c2 = visual.TextBox2(
         win, text='I understand my participation is completely voluntary.', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.2, 0.20),     letterHeight=0.028,
         size=(0.7, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='c2',
         depth=-1, autoLog=False,
    )
    c3 = visual.TextBox2(
         win, text='I understand I have the right to withdraw from the study at any time during or at the end of the study without giving a reason and with no adverse consequences.', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.2, 0.05),     letterHeight=0.028,
         size=(0.7, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='c3',
         depth=-2, autoLog=False,
    )
    c4 = visual.TextBox2(
         win, text='I have been given full information about what the study entails.', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.2, -0.125),     letterHeight=0.028,
         size=(0.7, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='c4',
         depth=-3, autoLog=False,
    )
    c5 = visual.TextBox2(
         win, text='I have been given contact information for the research team.', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.2, -0.25),     letterHeight=0.028,
         size=(0.7, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='c5',
         depth=-4, autoLog=False,
    )
    c6 = visual.TextBox2(
         win, text='I understand my responses will be fully anonymized.', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.2, -0.35),     letterHeight=0.028,
         size=(0.7, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='c6',
         depth=-5, autoLog=False,
    )
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(0.065, 0.02), pos=(0.37, 0.35), units=win.units,
        labels=['Yes', 'No'],ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-6, readOnly=False)
    slider_2 = visual.Slider(win=win, name='slider_2',
        startValue=None, size=(0.065, 0.02), pos=(0.37, 0.2), units=win.units,
        labels=['Yes', 'No'],ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-7, readOnly=False)
    slider_3 = visual.Slider(win=win, name='slider_3',
        startValue=None, size=(0.065, 0.02), pos=(0.37, 0.05), units=win.units,
        labels=['Yes', 'No'],ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-8, readOnly=False)
    slider_4 = visual.Slider(win=win, name='slider_4',
        startValue=None, size=(0.065, 0.02), pos=(0.37, -0.125), units=win.units,
        labels=['Yes', 'No'],ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-9, readOnly=False)
    slider_5 = visual.Slider(win=win, name='slider_5',
        startValue=None, size=(0.065, 0.02), pos=(0.37, -0.25), units=win.units,
        labels=['Yes', 'No'],ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-10, readOnly=False)
    slider_6 = visual.Slider(win=win, name='slider_6',
        startValue=None, size=(0.065, 0.02), pos=(0.37, -0.35), units=win.units,
        labels=['Yes', 'No'],ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.025,
        flip=False, ori=0.0, depth=-11, readOnly=False)
    mouse_consent = event.Mouse(win=win)
    x, y = [None, None]
    mouse_consent.mouseClock = core.Clock()
    consent_box = visual.TextBox2(
         win, text='CONTINUE', placeholder='Type here...', font='Trebuchet MS',
         pos=(0, -0.45),     letterHeight=0.03,
         size=(0.2, 0.065), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='darkgrey', borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='consent_box',
         depth=-14, autoLog=False,
    )
    
    # --- Initialize components for Routine "instructions_1" ---
    cont_train_instr = visual.TextBox2(
         win, text='CONTINUE', placeholder='Type here...', font='Trebuchet MS',
         pos=(0, -0.45),     letterHeight=0.03,
         size=(0.2, 0.065), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='darkgrey', borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='cont_train_instr',
         depth=0, autoLog=False,
    )
    cont_train_instr_mouse = event.Mouse(win=win)
    x, y = [None, None]
    cont_train_instr_mouse.mouseClock = core.Clock()
    train_instructions = visual.ImageStim(
        win=win,
        name='train_instructions', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "comprehension1" ---
    comp1_resp1 = visual.TextBox2(
         win, text='Learn which mutant would result of each chemicals combination', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.71, -0.2),     letterHeight=0.035,
         size=(1.5, 0.05), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='comp1_resp1',
         depth=-1, autoLog=False,
    )
    comp1_resp2 = visual.TextBox2(
         win, text='Predict which mutant would take over the world', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.71, -0.26),     letterHeight=0.035,
         size=(1.5, 0.05), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='comp1_resp2',
         depth=-2, autoLog=False,
    )
    comp1_resp3 = visual.TextBox2(
         win, text='Decide if the chemicals are organic or inorganic', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.71, -0.32),     letterHeight=0.035,
         size=(1.5, 0.05), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='comp1_resp3',
         depth=-3, autoLog=False,
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
         win, text='CONTINUE', placeholder='Type here...', font='Trebuchet MS',
         pos=(0, -0.45),     letterHeight=0.03,
         size=(0.2, 0.065), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='darkgrey', borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='cont_train_instr',
         depth=0, autoLog=False,
    )
    cont_train_instr_mouse = event.Mouse(win=win)
    x, y = [None, None]
    cont_train_instr_mouse.mouseClock = core.Clock()
    train_instructions = visual.ImageStim(
        win=win,
        name='train_instructions', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "comprehension1_2" ---
    comp1_resp1_2 = visual.TextBox2(
         win, text='Learn which mutant would result of each chemicals combination', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.71, -0.2),     letterHeight=0.035,
         size=(1.5, 0.05), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='comp1_resp1_2',
         depth=-1, autoLog=False,
    )
    comp1_resp2_2 = visual.TextBox2(
         win, text='Predict which mutant would take over the world', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.71, -0.26),     letterHeight=0.035,
         size=(1.5, 0.05), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='comp1_resp2_2',
         depth=-2, autoLog=False,
    )
    comp1_resp3_2 = visual.TextBox2(
         win, text='Decide if the chemicals are organic or inorganic', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.71, -0.32),     letterHeight=0.035,
         size=(1.5, 0.05), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='comp1_resp3_2',
         depth=-3, autoLog=False,
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
    order = [1, 2, 3, 4, 5, 6, 7, 8]
    shuffle (order)
    
    reorder_cues = [cues[i-1] for i in order]
    reorder_vsubtle = [distractors_vsubtle[i-1] for i in order]
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
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    non_predictive_cue = visual.ImageStim(
        win=win,
        name='non_predictive_cue', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    o1_image = visual.ImageStim(
        win=win,
        name='o1_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.16, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    o2_image = visual.ImageStim(
        win=win,
        name='o2_image', 
        image='default.png', mask=None, anchor='center',
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
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    non_predictive_cue_selection = visual.ImageStim(
        win=win,
        name='non_predictive_cue_selection', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    o1_image_selection = visual.ImageStim(
        win=win,
        name='o1_image_selection', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.16, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    o2_image_selection = visual.ImageStim(
        win=win,
        name='o2_image_selection', 
        image='default.png', mask=None, anchor='center',
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
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    non_predictive_cue_feedback = visual.ImageStim(
        win=win,
        name='non_predictive_cue_feedback', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    o1_image_feedback = visual.ImageStim(
        win=win,
        name='o1_image_feedback', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.16, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    o2_image_feedback = visual.ImageStim(
        win=win,
        name='o2_image_feedback', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.16, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "cue_o__trial" ---
    # Run 'Begin Experiment' code from cue_random
    cues = ["stimuli/cue_a1.png", "stimuli/cue_a2.png", "stimuli/cue_a3.png", "stimuli/cue_a4.png", "stimuli/cue_a5.png", "stimuli/cue_a6.png", "stimuli/cue_a7.png", "stimuli/cue_a8.png"]
    distractors_vsubtle = ["stimuli/cue_b1.png", "stimuli/cue_b2.png", "stimuli/cue_b3.png", "stimuli/cue_b4.png", "stimuli/cue_b5.png", "stimuli/cue_b6.png", "stimuli/cue_b7.png", "stimuli/cue_b8.png"]
    order = [1, 2, 3, 4, 5, 6, 7, 8]
    shuffle (order)
    
    reorder_cues = [cues[i-1] for i in order]
    reorder_vsubtle = [distractors_vsubtle[i-1] for i in order]
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
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    non_predictive_cue = visual.ImageStim(
        win=win,
        name='non_predictive_cue', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    o1_image = visual.ImageStim(
        win=win,
        name='o1_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.16, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    o2_image = visual.ImageStim(
        win=win,
        name='o2_image', 
        image='default.png', mask=None, anchor='center',
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
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    non_predictive_cue_selection = visual.ImageStim(
        win=win,
        name='non_predictive_cue_selection', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    o1_image_selection = visual.ImageStim(
        win=win,
        name='o1_image_selection', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.16, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    o2_image_selection = visual.ImageStim(
        win=win,
        name='o2_image_selection', 
        image='default.png', mask=None, anchor='center',
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
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    non_predictive_cue_feedback = visual.ImageStim(
        win=win,
        name='non_predictive_cue_feedback', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    o1_image_feedback = visual.ImageStim(
        win=win,
        name='o1_image_feedback', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.16, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    o2_image_feedback = visual.ImageStim(
        win=win,
        name='o2_image_feedback', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.16, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "test2_vsubtle_inst" ---
    cont_test2_vsubtle = visual.TextBox2(
         win, text='CONTINUE', placeholder='Type here...', font='Trebuchet MS',
         pos=(0, -0.45),     letterHeight=0.03,
         size=(0.2, 0.065), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='darkgrey', borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='cont_test2_vsubtle',
         depth=0, autoLog=False,
    )
    cont_mouse_test2_vsubtle = event.Mouse(win=win)
    x, y = [None, None]
    cont_mouse_test2_vsubtle.mouseClock = core.Clock()
    instructions_test2_vsubtle = visual.ImageStim(
        win=win,
        name='instructions_test2_vsubtle', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "comprehension3" ---
    comp3_resp2 = visual.TextBox2(
         win, text='Click on the mutant that would result of each chemicals combination', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.71, -0.2),     letterHeight=0.035,
         size=(1.5, 0.05), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='comp3_resp2',
         depth=0, autoLog=False,
    )
    comp3_resp1 = visual.TextBox2(
         win, text='Select the chemical you have seen in Task 1', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.71, -0.26),     letterHeight=0.035,
         size=(1.5, 0.05), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='comp3_resp1',
         depth=-1, autoLog=False,
    )
    comp3_resp3 = visual.TextBox2(
         win, text='Rate how beautiful the chemicals presented are', placeholder='Type here...', font='Trebuchet MS',
         pos=(-0.71, -0.32),     letterHeight=0.035,
         size=(1.5, 0.05), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center-left', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='comp3_resp3',
         depth=-2, autoLog=False,
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
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    distractor_test2_vsubtle = visual.ImageStim(
        win=win,
        name='distractor_test2_vsubtle', 
        image='default.png', mask=None, anchor='center',
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
        startValue=5.5, size=(0.5, 0.025), pos=(0, -0.2), units=win.units,
        labels=["I am guessing", "I am certain"], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.5,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='white', markerColor='Red', lineColor='white', colorSpace='rgb',
        font='Trebuchet MS', labelHeight=0.028,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    slider_target_test2_vsubtle = visual.ImageStim(
        win=win,
        name='slider_target_test2_vsubtle', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    slider_distractor_test2_vsubtle = visual.ImageStim(
        win=win,
        name='slider_distractor_test2_vsubtle', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    continue_rate_test2_vsubtle = visual.TextBox2(
         win, text='CONTINUE', placeholder='Type here...', font='Trebuchet MS',
         pos=(0, -0.45),     letterHeight=0.03,
         size=(0.2, 0.065), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='darkgrey', borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='continue_rate_test2_vsubtle',
         depth=-5, autoLog=False,
    )
    mouse_continue_test2_vsubtle = event.Mouse(win=win)
    x, y = [None, None]
    mouse_continue_test2_vsubtle.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "debrief" ---
    cont_debrief = visual.TextBox2(
         win, text='CONTINUE', placeholder='Type here...', font='Trebuchet MS',
         pos=(0, -0.45),     letterHeight=0.03,
         size=(0.2, 0.065), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='darkgrey', borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='cont_debrief',
         depth=0, autoLog=False,
    )
    cont_debrief_mouse = event.Mouse(win=win)
    x, y = [None, None]
    cont_debrief_mouse.mouseClock = core.Clock()
    debrief_image = visual.ImageStim(
        win=win,
        name='debrief_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "no_comprehension" ---
    no_compr_textbox = visual.TextBox2(
         win, text="You did not pass the comprehension check.\nPlease, click the button below to leave the experiment and return the experiment clicking 'Stop Without Completing' on Prolific.", placeholder='Type here...', font='Trebuchet MS',
         pos=(0, 0),     letterHeight=0.03,
         size=(0.65, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='no_compr_textbox',
         depth=0, autoLog=False,
    )
    exit_box_no_compr = visual.TextBox2(
         win, text='EXIT', placeholder='Type here...', font='Trebuchet MS',
         pos=(0, -0.4),     letterHeight=0.03,
         size=(0.2, 0.065), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='darkgrey', borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='exit_box_no_compr',
         depth=-1, autoLog=False,
    )
    mouse_exit_no_compr = event.Mouse(win=win)
    x, y = [None, None]
    mouse_exit_no_compr.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "no_consent_trial" ---
    no_consent_textbox = visual.TextBox2(
         win, text='Thank you for considering our study. You did not consent to participate.', placeholder='Type here...', font='Trebuchet MS',
         pos=(0, 0),     letterHeight=0.03,
         size=(0.65, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='no_consent_textbox',
         depth=0, autoLog=False,
    )
    exit_box = visual.TextBox2(
         win, text='EXIT', placeholder='Type here...', font='Trebuchet MS',
         pos=(0, -0.4),     letterHeight=0.03,
         size=(0.2, 0.065), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='darkgrey', borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='exit_box',
         depth=-1, autoLog=False,
    )
    mouse_exit = event.Mouse(win=win)
    x, y = [None, None]
    mouse_exit.mouseClock = core.Clock()
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "counterbalance" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('counterbalance.started', globalClock.getTime(format='float'))
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
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
    thisExp.addData('counterbalance.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
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
            globals()[paramName] = thisInformation_loop[paramName]
    
    for thisInformation_loop in information_loop:
        currentLoop = information_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisInformation_loop.rgb)
        if thisInformation_loop != None:
            for paramName in thisInformation_loop:
                globals()[paramName] = thisInformation_loop[paramName]
        
        # --- Prepare to start Routine "information" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('information.started', globalClock.getTime(format='float'))
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
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *continue_info* updates
            
            # if continue_info is starting this frame...
            if continue_info.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                continue_info.frameNStart = frameN  # exact frame index
                continue_info.tStart = t  # local t and not account for scr refresh
                continue_info.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continue_info, 'tStartRefresh')  # time at next scr refresh
                # update status
                continue_info.status = STARTED
                continue_info.setAutoDraw(True)
            
            # if continue_info is active this frame...
            if continue_info.status == STARTED:
                # update params
                pass
            # *mouse_info* updates
            
            # if mouse_info is starting this frame...
            if mouse_info.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_info.frameNStart = frameN  # exact frame index
                mouse_info.tStart = t  # local t and not account for scr refresh
                mouse_info.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_info, 'tStartRefresh')  # time at next scr refresh
                # update status
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
                        clickableList = environmenttools.getFromNames(continue_info, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_info):
                                gotValidClick = True
                                mouse_info.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # end routine on response
            
            # *image_info* updates
            
            # if image_info is starting this frame...
            if image_info.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_info.frameNStart = frameN  # exact frame index
                image_info.tStart = t  # local t and not account for scr refresh
                image_info.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_info, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_info.status = STARTED
                image_info.setAutoDraw(True)
            
            # if image_info is active this frame...
            if image_info.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
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
        thisExp.addData('information.stopped', globalClock.getTime(format='float'))
        # store data for information_loop (TrialHandler)
        # the Routine "information" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'information_loop'
    
    
    # --- Prepare to start Routine "consent" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('consent.started', globalClock.getTime(format='float'))
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *c1* updates
        
        # if c1 is starting this frame...
        if c1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            c1.frameNStart = frameN  # exact frame index
            c1.tStart = t  # local t and not account for scr refresh
            c1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(c1, 'tStartRefresh')  # time at next scr refresh
            # update status
            c1.status = STARTED
            c1.setAutoDraw(True)
        
        # if c1 is active this frame...
        if c1.status == STARTED:
            # update params
            pass
        
        # *c2* updates
        
        # if c2 is starting this frame...
        if c2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            c2.frameNStart = frameN  # exact frame index
            c2.tStart = t  # local t and not account for scr refresh
            c2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(c2, 'tStartRefresh')  # time at next scr refresh
            # update status
            c2.status = STARTED
            c2.setAutoDraw(True)
        
        # if c2 is active this frame...
        if c2.status == STARTED:
            # update params
            pass
        
        # *c3* updates
        
        # if c3 is starting this frame...
        if c3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            c3.frameNStart = frameN  # exact frame index
            c3.tStart = t  # local t and not account for scr refresh
            c3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(c3, 'tStartRefresh')  # time at next scr refresh
            # update status
            c3.status = STARTED
            c3.setAutoDraw(True)
        
        # if c3 is active this frame...
        if c3.status == STARTED:
            # update params
            pass
        
        # *c4* updates
        
        # if c4 is starting this frame...
        if c4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            c4.frameNStart = frameN  # exact frame index
            c4.tStart = t  # local t and not account for scr refresh
            c4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(c4, 'tStartRefresh')  # time at next scr refresh
            # update status
            c4.status = STARTED
            c4.setAutoDraw(True)
        
        # if c4 is active this frame...
        if c4.status == STARTED:
            # update params
            pass
        
        # *c5* updates
        
        # if c5 is starting this frame...
        if c5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            c5.frameNStart = frameN  # exact frame index
            c5.tStart = t  # local t and not account for scr refresh
            c5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(c5, 'tStartRefresh')  # time at next scr refresh
            # update status
            c5.status = STARTED
            c5.setAutoDraw(True)
        
        # if c5 is active this frame...
        if c5.status == STARTED:
            # update params
            pass
        
        # *c6* updates
        
        # if c6 is starting this frame...
        if c6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            c6.frameNStart = frameN  # exact frame index
            c6.tStart = t  # local t and not account for scr refresh
            c6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(c6, 'tStartRefresh')  # time at next scr refresh
            # update status
            c6.status = STARTED
            c6.setAutoDraw(True)
        
        # if c6 is active this frame...
        if c6.status == STARTED:
            # update params
            pass
        
        # *slider_1* updates
        
        # if slider_1 is starting this frame...
        if slider_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            slider_1.frameNStart = frameN  # exact frame index
            slider_1.tStart = t  # local t and not account for scr refresh
            slider_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
            # update status
            slider_1.status = STARTED
            slider_1.setAutoDraw(True)
        
        # if slider_1 is active this frame...
        if slider_1.status == STARTED:
            # update params
            pass
        
        # *slider_2* updates
        
        # if slider_2 is starting this frame...
        if slider_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            slider_2.frameNStart = frameN  # exact frame index
            slider_2.tStart = t  # local t and not account for scr refresh
            slider_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            slider_2.status = STARTED
            slider_2.setAutoDraw(True)
        
        # if slider_2 is active this frame...
        if slider_2.status == STARTED:
            # update params
            pass
        
        # *slider_3* updates
        
        # if slider_3 is starting this frame...
        if slider_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            slider_3.frameNStart = frameN  # exact frame index
            slider_3.tStart = t  # local t and not account for scr refresh
            slider_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            slider_3.status = STARTED
            slider_3.setAutoDraw(True)
        
        # if slider_3 is active this frame...
        if slider_3.status == STARTED:
            # update params
            pass
        
        # *slider_4* updates
        
        # if slider_4 is starting this frame...
        if slider_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            slider_4.frameNStart = frameN  # exact frame index
            slider_4.tStart = t  # local t and not account for scr refresh
            slider_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            slider_4.status = STARTED
            slider_4.setAutoDraw(True)
        
        # if slider_4 is active this frame...
        if slider_4.status == STARTED:
            # update params
            pass
        
        # *slider_5* updates
        
        # if slider_5 is starting this frame...
        if slider_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            slider_5.frameNStart = frameN  # exact frame index
            slider_5.tStart = t  # local t and not account for scr refresh
            slider_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_5, 'tStartRefresh')  # time at next scr refresh
            # update status
            slider_5.status = STARTED
            slider_5.setAutoDraw(True)
        
        # if slider_5 is active this frame...
        if slider_5.status == STARTED:
            # update params
            pass
        
        # *slider_6* updates
        
        # if slider_6 is starting this frame...
        if slider_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            slider_6.frameNStart = frameN  # exact frame index
            slider_6.tStart = t  # local t and not account for scr refresh
            slider_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            slider_6.status = STARTED
            slider_6.setAutoDraw(True)
        
        # if slider_6 is active this frame...
        if slider_6.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from show_consent_code
        s1 = slider_1.getRating()
        s2 = slider_2.getRating()
        s3 = slider_3.getRating()
        s4 = slider_4.getRating()
        s5 = slider_5.getRating()
        s6 = slider_6.getRating()
        
        if s1:
            if s2:
                if s3:
                    if s4:
                        if s5:
                            if s6:
                                show_consent = True
        # *mouse_consent* updates
        
        # if mouse_consent is starting this frame...
        if mouse_consent.status == NOT_STARTED and show_consent:
            # keep track of start time/frame for later
            mouse_consent.frameNStart = frameN  # exact frame index
            mouse_consent.tStart = t  # local t and not account for scr refresh
            mouse_consent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_consent, 'tStartRefresh')  # time at next scr refresh
            # update status
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
                    clickableList = environmenttools.getFromNames(consent_box, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_consent):
                            gotValidClick = True
                            mouse_consent.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # *consent_box* updates
        
        # if consent_box is starting this frame...
        if consent_box.status == NOT_STARTED and show_consent:
            # keep track of start time/frame for later
            consent_box.frameNStart = frameN  # exact frame index
            consent_box.tStart = t  # local t and not account for scr refresh
            consent_box.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consent_box, 'tStartRefresh')  # time at next scr refresh
            # update status
            consent_box.status = STARTED
            consent_box.setAutoDraw(True)
        
        # if consent_box is active this frame...
        if consent_box.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
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
    thisExp.addData('consent.stopped', globalClock.getTime(format='float'))
    thisExp.addData('slider_1.response', slider_1.getRating())
    thisExp.addData('slider_2.response', slider_2.getRating())
    thisExp.addData('slider_3.response', slider_3.getRating())
    thisExp.addData('slider_4.response', slider_4.getRating())
    thisExp.addData('slider_5.response', slider_5.getRating())
    thisExp.addData('slider_6.response', slider_6.getRating())
    # store data for thisExp (ExperimentHandler)
    # Run 'End Routine' code from consent_code
    res1 = slider_1.getRating()
    res2 = slider_2.getRating()
    res3 = slider_3.getRating()
    res4 = slider_4.getRating()
    res5 = slider_5.getRating()
    res6 = slider_6.getRating()
    
    if res1 == 'Yes':
        if res2 == 'Yes':
            if res3 == 'Yes':
                if res4 == 'Yes':
                    if res5 == 'Yes':
                        if res6 == 'Yes':
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
    thisExp.nextEntry()
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
            globals()[paramName] = thisConsent_loop[paramName]
    
    for thisConsent_loop in consent_loop:
        currentLoop = consent_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisConsent_loop.rgb)
        if thisConsent_loop != None:
            for paramName in thisConsent_loop:
                globals()[paramName] = thisConsent_loop[paramName]
        
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
                globals()[paramName] = thisTask1_instr[paramName]
        
        for thisTask1_instr in task1_instr:
            currentLoop = task1_instr
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTask1_instr.rgb)
            if thisTask1_instr != None:
                for paramName in thisTask1_instr:
                    globals()[paramName] = thisTask1_instr[paramName]
            
            # --- Prepare to start Routine "instructions_1" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('instructions_1.started', globalClock.getTime(format='float'))
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
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *cont_train_instr* updates
                
                # if cont_train_instr is starting this frame...
                if cont_train_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cont_train_instr.frameNStart = frameN  # exact frame index
                    cont_train_instr.tStart = t  # local t and not account for scr refresh
                    cont_train_instr.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cont_train_instr, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    cont_train_instr.status = STARTED
                    cont_train_instr.setAutoDraw(True)
                
                # if cont_train_instr is active this frame...
                if cont_train_instr.status == STARTED:
                    # update params
                    pass
                # *cont_train_instr_mouse* updates
                
                # if cont_train_instr_mouse is starting this frame...
                if cont_train_instr_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cont_train_instr_mouse.frameNStart = frameN  # exact frame index
                    cont_train_instr_mouse.tStart = t  # local t and not account for scr refresh
                    cont_train_instr_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cont_train_instr_mouse, 'tStartRefresh')  # time at next scr refresh
                    # update status
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
                            clickableList = environmenttools.getFromNames(cont_train_instr, namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(cont_train_instr_mouse):
                                    gotValidClick = True
                                    cont_train_instr_mouse.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # end routine on response
                
                # *train_instructions* updates
                
                # if train_instructions is starting this frame...
                if train_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    train_instructions.frameNStart = frameN  # exact frame index
                    train_instructions.tStart = t  # local t and not account for scr refresh
                    train_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(train_instructions, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    train_instructions.status = STARTED
                    train_instructions.setAutoDraw(True)
                
                # if train_instructions is active this frame...
                if train_instructions.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
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
            thisExp.addData('instructions_1.stopped', globalClock.getTime(format='float'))
            # store data for task1_instr (TrialHandler)
            # the Routine "instructions_1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'task1_instr'
        
        
        # --- Prepare to start Routine "comprehension1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('comprehension1.started', globalClock.getTime(format='float'))
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
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *comp1_resp1* updates
            
            # if comp1_resp1 is starting this frame...
            if comp1_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                comp1_resp1.frameNStart = frameN  # exact frame index
                comp1_resp1.tStart = t  # local t and not account for scr refresh
                comp1_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(comp1_resp1, 'tStartRefresh')  # time at next scr refresh
                # update status
                comp1_resp1.status = STARTED
                comp1_resp1.setAutoDraw(True)
            
            # if comp1_resp1 is active this frame...
            if comp1_resp1.status == STARTED:
                # update params
                pass
            
            # *comp1_resp2* updates
            
            # if comp1_resp2 is starting this frame...
            if comp1_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                comp1_resp2.frameNStart = frameN  # exact frame index
                comp1_resp2.tStart = t  # local t and not account for scr refresh
                comp1_resp2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(comp1_resp2, 'tStartRefresh')  # time at next scr refresh
                # update status
                comp1_resp2.status = STARTED
                comp1_resp2.setAutoDraw(True)
            
            # if comp1_resp2 is active this frame...
            if comp1_resp2.status == STARTED:
                # update params
                pass
            
            # *comp1_resp3* updates
            
            # if comp1_resp3 is starting this frame...
            if comp1_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                comp1_resp3.frameNStart = frameN  # exact frame index
                comp1_resp3.tStart = t  # local t and not account for scr refresh
                comp1_resp3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(comp1_resp3, 'tStartRefresh')  # time at next scr refresh
                # update status
                comp1_resp3.status = STARTED
                comp1_resp3.setAutoDraw(True)
            
            # if comp1_resp3 is active this frame...
            if comp1_resp3.status == STARTED:
                # update params
                pass
            # *comp1_mouse* updates
            
            # if comp1_mouse is starting this frame...
            if comp1_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                comp1_mouse.frameNStart = frameN  # exact frame index
                comp1_mouse.tStart = t  # local t and not account for scr refresh
                comp1_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(comp1_mouse, 'tStartRefresh')  # time at next scr refresh
                # update status
                comp1_mouse.status = STARTED
                prevButtonState = comp1_mouse.getPressed()  # if button is down already this ISN'T a new click
            if comp1_mouse.status == STARTED:  # only update if started and not finished!
                buttons = comp1_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([comp1_resp1, comp1_resp2, comp1_resp3], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
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
                            continueRoutine = False  # end routine on response
            
            # *check1* updates
            
            # if check1 is starting this frame...
            if check1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                check1.frameNStart = frameN  # exact frame index
                check1.tStart = t  # local t and not account for scr refresh
                check1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(check1, 'tStartRefresh')  # time at next scr refresh
                # update status
                check1.status = STARTED
                check1.setAutoDraw(True)
            
            # if check1 is active this frame...
            if check1.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
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
        thisExp.addData('comprehension1.stopped', globalClock.getTime(format='float'))
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
                globals()[paramName] = thisComp1_loop[paramName]
        
        for thisComp1_loop in comp1_loop:
            currentLoop = comp1_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisComp1_loop.rgb)
            if thisComp1_loop != None:
                for paramName in thisComp1_loop:
                    globals()[paramName] = thisComp1_loop[paramName]
            
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
                    globals()[paramName] = thisTask1_instr_again[paramName]
            
            for thisTask1_instr_again in task1_instr_again:
                currentLoop = task1_instr_again
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTask1_instr_again.rgb)
                if thisTask1_instr_again != None:
                    for paramName in thisTask1_instr_again:
                        globals()[paramName] = thisTask1_instr_again[paramName]
                
                # --- Prepare to start Routine "instructions_1" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('instructions_1.started', globalClock.getTime(format='float'))
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
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *cont_train_instr* updates
                    
                    # if cont_train_instr is starting this frame...
                    if cont_train_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_train_instr.frameNStart = frameN  # exact frame index
                        cont_train_instr.tStart = t  # local t and not account for scr refresh
                        cont_train_instr.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_train_instr, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        cont_train_instr.status = STARTED
                        cont_train_instr.setAutoDraw(True)
                    
                    # if cont_train_instr is active this frame...
                    if cont_train_instr.status == STARTED:
                        # update params
                        pass
                    # *cont_train_instr_mouse* updates
                    
                    # if cont_train_instr_mouse is starting this frame...
                    if cont_train_instr_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_train_instr_mouse.frameNStart = frameN  # exact frame index
                        cont_train_instr_mouse.tStart = t  # local t and not account for scr refresh
                        cont_train_instr_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_train_instr_mouse, 'tStartRefresh')  # time at next scr refresh
                        # update status
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
                                clickableList = environmenttools.getFromNames(cont_train_instr, namespace=locals())
                                for obj in clickableList:
                                    # is this object clicked on?
                                    if obj.contains(cont_train_instr_mouse):
                                        gotValidClick = True
                                        cont_train_instr_mouse.clicked_name.append(obj.name)
                                if gotValidClick:  
                                    continueRoutine = False  # end routine on response
                    
                    # *train_instructions* updates
                    
                    # if train_instructions is starting this frame...
                    if train_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        train_instructions.frameNStart = frameN  # exact frame index
                        train_instructions.tStart = t  # local t and not account for scr refresh
                        train_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(train_instructions, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        train_instructions.status = STARTED
                        train_instructions.setAutoDraw(True)
                    
                    # if train_instructions is active this frame...
                    if train_instructions.status == STARTED:
                        # update params
                        pass
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    
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
                thisExp.addData('instructions_1.stopped', globalClock.getTime(format='float'))
                # store data for task1_instr_again (TrialHandler)
                # the Routine "instructions_1" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 1.0 repeats of 'task1_instr_again'
            
            
            # --- Prepare to start Routine "comprehension1_2" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('comprehension1_2.started', globalClock.getTime(format='float'))
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
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *comp1_resp1_2* updates
                
                # if comp1_resp1_2 is starting this frame...
                if comp1_resp1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp1_resp1_2.frameNStart = frameN  # exact frame index
                    comp1_resp1_2.tStart = t  # local t and not account for scr refresh
                    comp1_resp1_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp1_resp1_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    comp1_resp1_2.status = STARTED
                    comp1_resp1_2.setAutoDraw(True)
                
                # if comp1_resp1_2 is active this frame...
                if comp1_resp1_2.status == STARTED:
                    # update params
                    pass
                
                # *comp1_resp2_2* updates
                
                # if comp1_resp2_2 is starting this frame...
                if comp1_resp2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp1_resp2_2.frameNStart = frameN  # exact frame index
                    comp1_resp2_2.tStart = t  # local t and not account for scr refresh
                    comp1_resp2_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp1_resp2_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    comp1_resp2_2.status = STARTED
                    comp1_resp2_2.setAutoDraw(True)
                
                # if comp1_resp2_2 is active this frame...
                if comp1_resp2_2.status == STARTED:
                    # update params
                    pass
                
                # *comp1_resp3_2* updates
                
                # if comp1_resp3_2 is starting this frame...
                if comp1_resp3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp1_resp3_2.frameNStart = frameN  # exact frame index
                    comp1_resp3_2.tStart = t  # local t and not account for scr refresh
                    comp1_resp3_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp1_resp3_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    comp1_resp3_2.status = STARTED
                    comp1_resp3_2.setAutoDraw(True)
                
                # if comp1_resp3_2 is active this frame...
                if comp1_resp3_2.status == STARTED:
                    # update params
                    pass
                # *comp1_mouse_2* updates
                
                # if comp1_mouse_2 is starting this frame...
                if comp1_mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    comp1_mouse_2.frameNStart = frameN  # exact frame index
                    comp1_mouse_2.tStart = t  # local t and not account for scr refresh
                    comp1_mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(comp1_mouse_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    comp1_mouse_2.status = STARTED
                    prevButtonState = comp1_mouse_2.getPressed()  # if button is down already this ISN'T a new click
                if comp1_mouse_2.status == STARTED:  # only update if started and not finished!
                    buttons = comp1_mouse_2.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            clickableList = environmenttools.getFromNames([comp1_resp1_2, comp1_resp2_2, comp1_resp3_2], namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
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
                                continueRoutine = False  # end routine on response
                
                # *check1_2* updates
                
                # if check1_2 is starting this frame...
                if check1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    check1_2.frameNStart = frameN  # exact frame index
                    check1_2.tStart = t  # local t and not account for scr refresh
                    check1_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(check1_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    check1_2.status = STARTED
                    check1_2.setAutoDraw(True)
                
                # if check1_2 is active this frame...
                if check1_2.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
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
            thisExp.addData('comprehension1_2.stopped', globalClock.getTime(format='float'))
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
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
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
                globals()[paramName] = thisCompr1_completed[paramName]
        
        for thisCompr1_completed in compr1_completed:
            currentLoop = compr1_completed
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisCompr1_completed.rgb)
            if thisCompr1_completed != None:
                for paramName in thisCompr1_completed:
                    globals()[paramName] = thisCompr1_completed[paramName]
            
            # set up handler to look after randomisation of conditions etc
            stage1_trials = data.TrialHandler(nReps=6.0, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('stage1_certain.xlsx'),
                seed=None, name='stage1_trials')
            thisExp.addLoop(stage1_trials)  # add the loop to the experiment
            thisStage1_trial = stage1_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisStage1_trial.rgb)
            if thisStage1_trial != None:
                for paramName in thisStage1_trial:
                    globals()[paramName] = thisStage1_trial[paramName]
            
            for thisStage1_trial in stage1_trials:
                currentLoop = stage1_trials
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisStage1_trial.rgb)
                if thisStage1_trial != None:
                    for paramName in thisStage1_trial:
                        globals()[paramName] = thisStage1_trial[paramName]
                
                # --- Prepare to start Routine "cue_o__trial" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('cue_o__trial.started', globalClock.getTime(format='float'))
                # Run 'Begin Routine' code from cue_random
                if cue1 == "A":
                    stim1 = reorder_cues[0]
                elif cue1 == "B":
                    stim1 = reorder_cues[1]
                elif cue1 == "C":
                    stim1 = reorder_cues[2]
                elif cue1 == "D":
                    stim1 = reorder_cues[3]
                
                if cue2 == "X":
                    stim2 = reorder_cues[4]
                elif cue2 == "Y":
                    stim2 = reorder_cues[5]
                elif cue2 == "W":
                    stim2 = reorder_cues[6]
                elif cue2 == "Z":
                    stim2 = reorder_cues[7]
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
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 11.5:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *blank_training* updates
                    
                    # if blank_training is starting this frame...
                    if blank_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        blank_training.frameNStart = frameN  # exact frame index
                        blank_training.tStart = t  # local t and not account for scr refresh
                        blank_training.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(blank_training, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        blank_training.status = STARTED
                        blank_training.setAutoDraw(True)
                    
                    # if blank_training is active this frame...
                    if blank_training.status == STARTED:
                        # update params
                        pass
                    
                    # if blank_training is stopping this frame...
                    if blank_training.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > blank_training.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            blank_training.tStop = t  # not accounting for scr refresh
                            blank_training.tStopRefresh = tThisFlipGlobal  # on global time
                            blank_training.frameNStop = frameN  # exact frame index
                            # update status
                            blank_training.status = FINISHED
                            blank_training.setAutoDraw(False)
                    
                    # *predictive_cue* updates
                    
                    # if predictive_cue is starting this frame...
                    if predictive_cue.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        predictive_cue.frameNStart = frameN  # exact frame index
                        predictive_cue.tStart = t  # local t and not account for scr refresh
                        predictive_cue.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(predictive_cue, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        predictive_cue.status = STARTED
                        predictive_cue.setAutoDraw(True)
                    
                    # if predictive_cue is active this frame...
                    if predictive_cue.status == STARTED:
                        # update params
                        pass
                    
                    # if predictive_cue is stopping this frame...
                    if predictive_cue.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > predictive_cue.tStartRefresh + 10-frameTolerance:
                            # keep track of stop time/frame for later
                            predictive_cue.tStop = t  # not accounting for scr refresh
                            predictive_cue.tStopRefresh = tThisFlipGlobal  # on global time
                            predictive_cue.frameNStop = frameN  # exact frame index
                            # update status
                            predictive_cue.status = FINISHED
                            predictive_cue.setAutoDraw(False)
                    
                    # *non_predictive_cue* updates
                    
                    # if non_predictive_cue is starting this frame...
                    if non_predictive_cue.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        non_predictive_cue.frameNStart = frameN  # exact frame index
                        non_predictive_cue.tStart = t  # local t and not account for scr refresh
                        non_predictive_cue.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(non_predictive_cue, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        non_predictive_cue.status = STARTED
                        non_predictive_cue.setAutoDraw(True)
                    
                    # if non_predictive_cue is active this frame...
                    if non_predictive_cue.status == STARTED:
                        # update params
                        pass
                    
                    # if non_predictive_cue is stopping this frame...
                    if non_predictive_cue.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > non_predictive_cue.tStartRefresh + 10-frameTolerance:
                            # keep track of stop time/frame for later
                            non_predictive_cue.tStop = t  # not accounting for scr refresh
                            non_predictive_cue.tStopRefresh = tThisFlipGlobal  # on global time
                            non_predictive_cue.frameNStop = frameN  # exact frame index
                            # update status
                            non_predictive_cue.status = FINISHED
                            non_predictive_cue.setAutoDraw(False)
                    
                    # *o1_image* updates
                    
                    # if o1_image is starting this frame...
                    if o1_image.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        o1_image.frameNStart = frameN  # exact frame index
                        o1_image.tStart = t  # local t and not account for scr refresh
                        o1_image.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(o1_image, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        o1_image.status = STARTED
                        o1_image.setAutoDraw(True)
                    
                    # if o1_image is active this frame...
                    if o1_image.status == STARTED:
                        # update params
                        pass
                    
                    # if o1_image is stopping this frame...
                    if o1_image.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > o1_image.tStartRefresh + 10-frameTolerance:
                            # keep track of stop time/frame for later
                            o1_image.tStop = t  # not accounting for scr refresh
                            o1_image.tStopRefresh = tThisFlipGlobal  # on global time
                            o1_image.frameNStop = frameN  # exact frame index
                            # update status
                            o1_image.status = FINISHED
                            o1_image.setAutoDraw(False)
                    
                    # *o2_image* updates
                    
                    # if o2_image is starting this frame...
                    if o2_image.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        o2_image.frameNStart = frameN  # exact frame index
                        o2_image.tStart = t  # local t and not account for scr refresh
                        o2_image.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(o2_image, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        o2_image.status = STARTED
                        o2_image.setAutoDraw(True)
                    
                    # if o2_image is active this frame...
                    if o2_image.status == STARTED:
                        # update params
                        pass
                    
                    # if o2_image is stopping this frame...
                    if o2_image.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > o2_image.tStartRefresh + 10-frameTolerance:
                            # keep track of stop time/frame for later
                            o2_image.tStop = t  # not accounting for scr refresh
                            o2_image.tStopRefresh = tThisFlipGlobal  # on global time
                            o2_image.frameNStop = frameN  # exact frame index
                            # update status
                            o2_image.status = FINISHED
                            o2_image.setAutoDraw(False)
                    # *cue_o_mouse* updates
                    
                    # if cue_o_mouse is starting this frame...
                    if cue_o_mouse.status == NOT_STARTED and t >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        cue_o_mouse.frameNStart = frameN  # exact frame index
                        cue_o_mouse.tStart = t  # local t and not account for scr refresh
                        cue_o_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cue_o_mouse, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        cue_o_mouse.status = STARTED
                        cue_o_mouse.mouseClock.reset()
                        prevButtonState = cue_o_mouse.getPressed()  # if button is down already this ISN'T a new click
                    
                    # if cue_o_mouse is stopping this frame...
                    if cue_o_mouse.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > cue_o_mouse.tStartRefresh + 10-frameTolerance:
                            # keep track of stop time/frame for later
                            cue_o_mouse.tStop = t  # not accounting for scr refresh
                            cue_o_mouse.tStopRefresh = tThisFlipGlobal  # on global time
                            cue_o_mouse.frameNStop = frameN  # exact frame index
                            # update status
                            cue_o_mouse.status = FINISHED
                    if cue_o_mouse.status == STARTED:  # only update if started and not finished!
                        buttons = cue_o_mouse.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                clickableList = environmenttools.getFromNames([o1_image, o2_image], namespace=locals())
                                for obj in clickableList:
                                    # is this object clicked on?
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
                                    continueRoutine = False  # end routine on response
                    
                    # *timeout_text* updates
                    
                    # if timeout_text is starting this frame...
                    if timeout_text.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
                        # keep track of start time/frame for later
                        timeout_text.frameNStart = frameN  # exact frame index
                        timeout_text.tStart = t  # local t and not account for scr refresh
                        timeout_text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(timeout_text, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        timeout_text.status = STARTED
                        timeout_text.setAutoDraw(True)
                    
                    # if timeout_text is active this frame...
                    if timeout_text.status == STARTED:
                        # update params
                        pass
                    
                    # if timeout_text is stopping this frame...
                    if timeout_text.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > timeout_text.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            timeout_text.tStop = t  # not accounting for scr refresh
                            timeout_text.tStopRefresh = tThisFlipGlobal  # on global time
                            timeout_text.frameNStop = frameN  # exact frame index
                            # update status
                            timeout_text.status = FINISHED
                            timeout_text.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    
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
                thisExp.addData('cue_o__trial.stopped', globalClock.getTime(format='float'))
                # Run 'End Routine' code from cue_random
                thisExp.addData("order", order)
                # Run 'End Routine' code from position
                thisExp.addData ('cue_order', cue_positions)
                thisExp.addData ('out_order', out_positions)
                # store data for stage1_trials (TrialHandler)
                stage1_trials.addData('cue_o_mouse.x', cue_o_mouse.x)
                stage1_trials.addData('cue_o_mouse.y', cue_o_mouse.y)
                stage1_trials.addData('cue_o_mouse.leftButton', cue_o_mouse.leftButton)
                stage1_trials.addData('cue_o_mouse.midButton', cue_o_mouse.midButton)
                stage1_trials.addData('cue_o_mouse.rightButton', cue_o_mouse.rightButton)
                stage1_trials.addData('cue_o_mouse.time', cue_o_mouse.time)
                stage1_trials.addData('cue_o_mouse.clicked_name', cue_o_mouse.clicked_name)
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
                        globals()[paramName] = thisFeedback_loop[paramName]
                
                for thisFeedback_loop in feedback_loop:
                    currentLoop = feedback_loop
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisFeedback_loop.rgb)
                    if thisFeedback_loop != None:
                        for paramName in thisFeedback_loop:
                            globals()[paramName] = thisFeedback_loop[paramName]
                    
                    # --- Prepare to start Routine "cue_selection" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('cue_selection.started', globalClock.getTime(format='float'))
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
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 0.5:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *predictive_cue_selection* updates
                        
                        # if predictive_cue_selection is starting this frame...
                        if predictive_cue_selection.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            predictive_cue_selection.frameNStart = frameN  # exact frame index
                            predictive_cue_selection.tStart = t  # local t and not account for scr refresh
                            predictive_cue_selection.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(predictive_cue_selection, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            predictive_cue_selection.status = STARTED
                            predictive_cue_selection.setAutoDraw(True)
                        
                        # if predictive_cue_selection is active this frame...
                        if predictive_cue_selection.status == STARTED:
                            # update params
                            pass
                        
                        # if predictive_cue_selection is stopping this frame...
                        if predictive_cue_selection.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > predictive_cue_selection.tStartRefresh + 0.5-frameTolerance:
                                # keep track of stop time/frame for later
                                predictive_cue_selection.tStop = t  # not accounting for scr refresh
                                predictive_cue_selection.tStopRefresh = tThisFlipGlobal  # on global time
                                predictive_cue_selection.frameNStop = frameN  # exact frame index
                                # update status
                                predictive_cue_selection.status = FINISHED
                                predictive_cue_selection.setAutoDraw(False)
                        
                        # *non_predictive_cue_selection* updates
                        
                        # if non_predictive_cue_selection is starting this frame...
                        if non_predictive_cue_selection.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            non_predictive_cue_selection.frameNStart = frameN  # exact frame index
                            non_predictive_cue_selection.tStart = t  # local t and not account for scr refresh
                            non_predictive_cue_selection.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(non_predictive_cue_selection, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            non_predictive_cue_selection.status = STARTED
                            non_predictive_cue_selection.setAutoDraw(True)
                        
                        # if non_predictive_cue_selection is active this frame...
                        if non_predictive_cue_selection.status == STARTED:
                            # update params
                            pass
                        
                        # if non_predictive_cue_selection is stopping this frame...
                        if non_predictive_cue_selection.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > non_predictive_cue_selection.tStartRefresh + 0.5-frameTolerance:
                                # keep track of stop time/frame for later
                                non_predictive_cue_selection.tStop = t  # not accounting for scr refresh
                                non_predictive_cue_selection.tStopRefresh = tThisFlipGlobal  # on global time
                                non_predictive_cue_selection.frameNStop = frameN  # exact frame index
                                # update status
                                non_predictive_cue_selection.status = FINISHED
                                non_predictive_cue_selection.setAutoDraw(False)
                        
                        # *o1_image_selection* updates
                        
                        # if o1_image_selection is starting this frame...
                        if o1_image_selection.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            o1_image_selection.frameNStart = frameN  # exact frame index
                            o1_image_selection.tStart = t  # local t and not account for scr refresh
                            o1_image_selection.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(o1_image_selection, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            o1_image_selection.status = STARTED
                            o1_image_selection.setAutoDraw(True)
                        
                        # if o1_image_selection is active this frame...
                        if o1_image_selection.status == STARTED:
                            # update params
                            pass
                        
                        # if o1_image_selection is stopping this frame...
                        if o1_image_selection.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > o1_image_selection.tStartRefresh + 0.5-frameTolerance:
                                # keep track of stop time/frame for later
                                o1_image_selection.tStop = t  # not accounting for scr refresh
                                o1_image_selection.tStopRefresh = tThisFlipGlobal  # on global time
                                o1_image_selection.frameNStop = frameN  # exact frame index
                                # update status
                                o1_image_selection.status = FINISHED
                                o1_image_selection.setAutoDraw(False)
                        
                        # *o2_image_selection* updates
                        
                        # if o2_image_selection is starting this frame...
                        if o2_image_selection.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            o2_image_selection.frameNStart = frameN  # exact frame index
                            o2_image_selection.tStart = t  # local t and not account for scr refresh
                            o2_image_selection.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(o2_image_selection, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            o2_image_selection.status = STARTED
                            o2_image_selection.setAutoDraw(True)
                        
                        # if o2_image_selection is active this frame...
                        if o2_image_selection.status == STARTED:
                            # update params
                            pass
                        
                        # if o2_image_selection is stopping this frame...
                        if o2_image_selection.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > o2_image_selection.tStartRefresh + 0.5-frameTolerance:
                                # keep track of stop time/frame for later
                                o2_image_selection.tStop = t  # not accounting for scr refresh
                                o2_image_selection.tStopRefresh = tThisFlipGlobal  # on global time
                                o2_image_selection.frameNStop = frameN  # exact frame index
                                # update status
                                o2_image_selection.status = FINISHED
                                o2_image_selection.setAutoDraw(False)
                        
                        # *yellow_frame* updates
                        
                        # if yellow_frame is starting this frame...
                        if yellow_frame.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            yellow_frame.frameNStart = frameN  # exact frame index
                            yellow_frame.tStart = t  # local t and not account for scr refresh
                            yellow_frame.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(yellow_frame, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            yellow_frame.status = STARTED
                            yellow_frame.setAutoDraw(True)
                        
                        # if yellow_frame is active this frame...
                        if yellow_frame.status == STARTED:
                            # update params
                            pass
                        
                        # if yellow_frame is stopping this frame...
                        if yellow_frame.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > yellow_frame.tStartRefresh + 0.5-frameTolerance:
                                # keep track of stop time/frame for later
                                yellow_frame.tStop = t  # not accounting for scr refresh
                                yellow_frame.tStopRefresh = tThisFlipGlobal  # on global time
                                yellow_frame.frameNStop = frameN  # exact frame index
                                # update status
                                yellow_frame.status = FINISHED
                                yellow_frame.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        
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
                    thisExp.addData('cue_selection.stopped', globalClock.getTime(format='float'))
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-0.500000)
                    
                    # --- Prepare to start Routine "feedback" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('feedback.started', globalClock.getTime(format='float'))
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
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 2.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *feedback_text* updates
                        
                        # if feedback_text is starting this frame...
                        if feedback_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            feedback_text.frameNStart = frameN  # exact frame index
                            feedback_text.tStart = t  # local t and not account for scr refresh
                            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            feedback_text.status = STARTED
                            feedback_text.setAutoDraw(True)
                        
                        # if feedback_text is active this frame...
                        if feedback_text.status == STARTED:
                            # update params
                            pass
                        
                        # if feedback_text is stopping this frame...
                        if feedback_text.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > feedback_text.tStartRefresh + 2-frameTolerance:
                                # keep track of stop time/frame for later
                                feedback_text.tStop = t  # not accounting for scr refresh
                                feedback_text.tStopRefresh = tThisFlipGlobal  # on global time
                                feedback_text.frameNStop = frameN  # exact frame index
                                # update status
                                feedback_text.status = FINISHED
                                feedback_text.setAutoDraw(False)
                        
                        # *predictive_cue_feedback* updates
                        
                        # if predictive_cue_feedback is starting this frame...
                        if predictive_cue_feedback.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            predictive_cue_feedback.frameNStart = frameN  # exact frame index
                            predictive_cue_feedback.tStart = t  # local t and not account for scr refresh
                            predictive_cue_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(predictive_cue_feedback, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            predictive_cue_feedback.status = STARTED
                            predictive_cue_feedback.setAutoDraw(True)
                        
                        # if predictive_cue_feedback is active this frame...
                        if predictive_cue_feedback.status == STARTED:
                            # update params
                            pass
                        
                        # if predictive_cue_feedback is stopping this frame...
                        if predictive_cue_feedback.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > predictive_cue_feedback.tStartRefresh + 2-frameTolerance:
                                # keep track of stop time/frame for later
                                predictive_cue_feedback.tStop = t  # not accounting for scr refresh
                                predictive_cue_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                                predictive_cue_feedback.frameNStop = frameN  # exact frame index
                                # update status
                                predictive_cue_feedback.status = FINISHED
                                predictive_cue_feedback.setAutoDraw(False)
                        
                        # *non_predictive_cue_feedback* updates
                        
                        # if non_predictive_cue_feedback is starting this frame...
                        if non_predictive_cue_feedback.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            non_predictive_cue_feedback.frameNStart = frameN  # exact frame index
                            non_predictive_cue_feedback.tStart = t  # local t and not account for scr refresh
                            non_predictive_cue_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(non_predictive_cue_feedback, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            non_predictive_cue_feedback.status = STARTED
                            non_predictive_cue_feedback.setAutoDraw(True)
                        
                        # if non_predictive_cue_feedback is active this frame...
                        if non_predictive_cue_feedback.status == STARTED:
                            # update params
                            pass
                        
                        # if non_predictive_cue_feedback is stopping this frame...
                        if non_predictive_cue_feedback.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > non_predictive_cue_feedback.tStartRefresh + 2-frameTolerance:
                                # keep track of stop time/frame for later
                                non_predictive_cue_feedback.tStop = t  # not accounting for scr refresh
                                non_predictive_cue_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                                non_predictive_cue_feedback.frameNStop = frameN  # exact frame index
                                # update status
                                non_predictive_cue_feedback.status = FINISHED
                                non_predictive_cue_feedback.setAutoDraw(False)
                        
                        # *o1_image_feedback* updates
                        
                        # if o1_image_feedback is starting this frame...
                        if o1_image_feedback.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            o1_image_feedback.frameNStart = frameN  # exact frame index
                            o1_image_feedback.tStart = t  # local t and not account for scr refresh
                            o1_image_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(o1_image_feedback, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            o1_image_feedback.status = STARTED
                            o1_image_feedback.setAutoDraw(True)
                        
                        # if o1_image_feedback is active this frame...
                        if o1_image_feedback.status == STARTED:
                            # update params
                            pass
                        
                        # if o1_image_feedback is stopping this frame...
                        if o1_image_feedback.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > o1_image_feedback.tStartRefresh + 2-frameTolerance:
                                # keep track of stop time/frame for later
                                o1_image_feedback.tStop = t  # not accounting for scr refresh
                                o1_image_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                                o1_image_feedback.frameNStop = frameN  # exact frame index
                                # update status
                                o1_image_feedback.status = FINISHED
                                o1_image_feedback.setAutoDraw(False)
                        
                        # *o2_image_feedback* updates
                        
                        # if o2_image_feedback is starting this frame...
                        if o2_image_feedback.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            o2_image_feedback.frameNStart = frameN  # exact frame index
                            o2_image_feedback.tStart = t  # local t and not account for scr refresh
                            o2_image_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(o2_image_feedback, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            o2_image_feedback.status = STARTED
                            o2_image_feedback.setAutoDraw(True)
                        
                        # if o2_image_feedback is active this frame...
                        if o2_image_feedback.status == STARTED:
                            # update params
                            pass
                        
                        # if o2_image_feedback is stopping this frame...
                        if o2_image_feedback.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > o2_image_feedback.tStartRefresh + 2-frameTolerance:
                                # keep track of stop time/frame for later
                                o2_image_feedback.tStop = t  # not accounting for scr refresh
                                o2_image_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                                o2_image_feedback.frameNStop = frameN  # exact frame index
                                # update status
                                o2_image_feedback.status = FINISHED
                                o2_image_feedback.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        
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
                    thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-2.000000)
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed feedback_reps repeats of 'feedback_loop'
                
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 6.0 repeats of 'stage1_trials'
            
            
            # set up handler to look after randomisation of conditions etc
            stage2_trials = data.TrialHandler(nReps=stage2Reps, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions(stage2File),
                seed=None, name='stage2_trials')
            thisExp.addLoop(stage2_trials)  # add the loop to the experiment
            thisStage2_trial = stage2_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisStage2_trial.rgb)
            if thisStage2_trial != None:
                for paramName in thisStage2_trial:
                    globals()[paramName] = thisStage2_trial[paramName]
            
            for thisStage2_trial in stage2_trials:
                currentLoop = stage2_trials
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisStage2_trial.rgb)
                if thisStage2_trial != None:
                    for paramName in thisStage2_trial:
                        globals()[paramName] = thisStage2_trial[paramName]
                
                # --- Prepare to start Routine "cue_o__trial" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('cue_o__trial.started', globalClock.getTime(format='float'))
                # Run 'Begin Routine' code from cue_random
                if cue1 == "A":
                    stim1 = reorder_cues[0]
                elif cue1 == "B":
                    stim1 = reorder_cues[1]
                elif cue1 == "C":
                    stim1 = reorder_cues[2]
                elif cue1 == "D":
                    stim1 = reorder_cues[3]
                
                if cue2 == "X":
                    stim2 = reorder_cues[4]
                elif cue2 == "Y":
                    stim2 = reorder_cues[5]
                elif cue2 == "W":
                    stim2 = reorder_cues[6]
                elif cue2 == "Z":
                    stim2 = reorder_cues[7]
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
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 11.5:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *blank_training* updates
                    
                    # if blank_training is starting this frame...
                    if blank_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        blank_training.frameNStart = frameN  # exact frame index
                        blank_training.tStart = t  # local t and not account for scr refresh
                        blank_training.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(blank_training, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        blank_training.status = STARTED
                        blank_training.setAutoDraw(True)
                    
                    # if blank_training is active this frame...
                    if blank_training.status == STARTED:
                        # update params
                        pass
                    
                    # if blank_training is stopping this frame...
                    if blank_training.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > blank_training.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            blank_training.tStop = t  # not accounting for scr refresh
                            blank_training.tStopRefresh = tThisFlipGlobal  # on global time
                            blank_training.frameNStop = frameN  # exact frame index
                            # update status
                            blank_training.status = FINISHED
                            blank_training.setAutoDraw(False)
                    
                    # *predictive_cue* updates
                    
                    # if predictive_cue is starting this frame...
                    if predictive_cue.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        predictive_cue.frameNStart = frameN  # exact frame index
                        predictive_cue.tStart = t  # local t and not account for scr refresh
                        predictive_cue.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(predictive_cue, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        predictive_cue.status = STARTED
                        predictive_cue.setAutoDraw(True)
                    
                    # if predictive_cue is active this frame...
                    if predictive_cue.status == STARTED:
                        # update params
                        pass
                    
                    # if predictive_cue is stopping this frame...
                    if predictive_cue.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > predictive_cue.tStartRefresh + 10-frameTolerance:
                            # keep track of stop time/frame for later
                            predictive_cue.tStop = t  # not accounting for scr refresh
                            predictive_cue.tStopRefresh = tThisFlipGlobal  # on global time
                            predictive_cue.frameNStop = frameN  # exact frame index
                            # update status
                            predictive_cue.status = FINISHED
                            predictive_cue.setAutoDraw(False)
                    
                    # *non_predictive_cue* updates
                    
                    # if non_predictive_cue is starting this frame...
                    if non_predictive_cue.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        non_predictive_cue.frameNStart = frameN  # exact frame index
                        non_predictive_cue.tStart = t  # local t and not account for scr refresh
                        non_predictive_cue.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(non_predictive_cue, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        non_predictive_cue.status = STARTED
                        non_predictive_cue.setAutoDraw(True)
                    
                    # if non_predictive_cue is active this frame...
                    if non_predictive_cue.status == STARTED:
                        # update params
                        pass
                    
                    # if non_predictive_cue is stopping this frame...
                    if non_predictive_cue.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > non_predictive_cue.tStartRefresh + 10-frameTolerance:
                            # keep track of stop time/frame for later
                            non_predictive_cue.tStop = t  # not accounting for scr refresh
                            non_predictive_cue.tStopRefresh = tThisFlipGlobal  # on global time
                            non_predictive_cue.frameNStop = frameN  # exact frame index
                            # update status
                            non_predictive_cue.status = FINISHED
                            non_predictive_cue.setAutoDraw(False)
                    
                    # *o1_image* updates
                    
                    # if o1_image is starting this frame...
                    if o1_image.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        o1_image.frameNStart = frameN  # exact frame index
                        o1_image.tStart = t  # local t and not account for scr refresh
                        o1_image.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(o1_image, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        o1_image.status = STARTED
                        o1_image.setAutoDraw(True)
                    
                    # if o1_image is active this frame...
                    if o1_image.status == STARTED:
                        # update params
                        pass
                    
                    # if o1_image is stopping this frame...
                    if o1_image.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > o1_image.tStartRefresh + 10-frameTolerance:
                            # keep track of stop time/frame for later
                            o1_image.tStop = t  # not accounting for scr refresh
                            o1_image.tStopRefresh = tThisFlipGlobal  # on global time
                            o1_image.frameNStop = frameN  # exact frame index
                            # update status
                            o1_image.status = FINISHED
                            o1_image.setAutoDraw(False)
                    
                    # *o2_image* updates
                    
                    # if o2_image is starting this frame...
                    if o2_image.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        o2_image.frameNStart = frameN  # exact frame index
                        o2_image.tStart = t  # local t and not account for scr refresh
                        o2_image.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(o2_image, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        o2_image.status = STARTED
                        o2_image.setAutoDraw(True)
                    
                    # if o2_image is active this frame...
                    if o2_image.status == STARTED:
                        # update params
                        pass
                    
                    # if o2_image is stopping this frame...
                    if o2_image.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > o2_image.tStartRefresh + 10-frameTolerance:
                            # keep track of stop time/frame for later
                            o2_image.tStop = t  # not accounting for scr refresh
                            o2_image.tStopRefresh = tThisFlipGlobal  # on global time
                            o2_image.frameNStop = frameN  # exact frame index
                            # update status
                            o2_image.status = FINISHED
                            o2_image.setAutoDraw(False)
                    # *cue_o_mouse* updates
                    
                    # if cue_o_mouse is starting this frame...
                    if cue_o_mouse.status == NOT_STARTED and t >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        cue_o_mouse.frameNStart = frameN  # exact frame index
                        cue_o_mouse.tStart = t  # local t and not account for scr refresh
                        cue_o_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cue_o_mouse, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        cue_o_mouse.status = STARTED
                        cue_o_mouse.mouseClock.reset()
                        prevButtonState = cue_o_mouse.getPressed()  # if button is down already this ISN'T a new click
                    
                    # if cue_o_mouse is stopping this frame...
                    if cue_o_mouse.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > cue_o_mouse.tStartRefresh + 10-frameTolerance:
                            # keep track of stop time/frame for later
                            cue_o_mouse.tStop = t  # not accounting for scr refresh
                            cue_o_mouse.tStopRefresh = tThisFlipGlobal  # on global time
                            cue_o_mouse.frameNStop = frameN  # exact frame index
                            # update status
                            cue_o_mouse.status = FINISHED
                    if cue_o_mouse.status == STARTED:  # only update if started and not finished!
                        buttons = cue_o_mouse.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                clickableList = environmenttools.getFromNames([o1_image, o2_image], namespace=locals())
                                for obj in clickableList:
                                    # is this object clicked on?
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
                                    continueRoutine = False  # end routine on response
                    
                    # *timeout_text* updates
                    
                    # if timeout_text is starting this frame...
                    if timeout_text.status == NOT_STARTED and tThisFlip >= 10.5-frameTolerance:
                        # keep track of start time/frame for later
                        timeout_text.frameNStart = frameN  # exact frame index
                        timeout_text.tStart = t  # local t and not account for scr refresh
                        timeout_text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(timeout_text, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        timeout_text.status = STARTED
                        timeout_text.setAutoDraw(True)
                    
                    # if timeout_text is active this frame...
                    if timeout_text.status == STARTED:
                        # update params
                        pass
                    
                    # if timeout_text is stopping this frame...
                    if timeout_text.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > timeout_text.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            timeout_text.tStop = t  # not accounting for scr refresh
                            timeout_text.tStopRefresh = tThisFlipGlobal  # on global time
                            timeout_text.frameNStop = frameN  # exact frame index
                            # update status
                            timeout_text.status = FINISHED
                            timeout_text.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    
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
                thisExp.addData('cue_o__trial.stopped', globalClock.getTime(format='float'))
                # Run 'End Routine' code from cue_random
                thisExp.addData("order", order)
                # Run 'End Routine' code from position
                thisExp.addData ('cue_order', cue_positions)
                thisExp.addData ('out_order', out_positions)
                # store data for stage2_trials (TrialHandler)
                stage2_trials.addData('cue_o_mouse.x', cue_o_mouse.x)
                stage2_trials.addData('cue_o_mouse.y', cue_o_mouse.y)
                stage2_trials.addData('cue_o_mouse.leftButton', cue_o_mouse.leftButton)
                stage2_trials.addData('cue_o_mouse.midButton', cue_o_mouse.midButton)
                stage2_trials.addData('cue_o_mouse.rightButton', cue_o_mouse.rightButton)
                stage2_trials.addData('cue_o_mouse.time', cue_o_mouse.time)
                stage2_trials.addData('cue_o_mouse.clicked_name', cue_o_mouse.clicked_name)
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
                stage2_feedback_loop = data.TrialHandler(nReps=feedback_reps, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=[None],
                    seed=None, name='stage2_feedback_loop')
                thisExp.addLoop(stage2_feedback_loop)  # add the loop to the experiment
                thisStage2_feedback_loop = stage2_feedback_loop.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisStage2_feedback_loop.rgb)
                if thisStage2_feedback_loop != None:
                    for paramName in thisStage2_feedback_loop:
                        globals()[paramName] = thisStage2_feedback_loop[paramName]
                
                for thisStage2_feedback_loop in stage2_feedback_loop:
                    currentLoop = stage2_feedback_loop
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisStage2_feedback_loop.rgb)
                    if thisStage2_feedback_loop != None:
                        for paramName in thisStage2_feedback_loop:
                            globals()[paramName] = thisStage2_feedback_loop[paramName]
                    
                    # --- Prepare to start Routine "cue_selection" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('cue_selection.started', globalClock.getTime(format='float'))
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
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 0.5:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *predictive_cue_selection* updates
                        
                        # if predictive_cue_selection is starting this frame...
                        if predictive_cue_selection.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            predictive_cue_selection.frameNStart = frameN  # exact frame index
                            predictive_cue_selection.tStart = t  # local t and not account for scr refresh
                            predictive_cue_selection.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(predictive_cue_selection, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            predictive_cue_selection.status = STARTED
                            predictive_cue_selection.setAutoDraw(True)
                        
                        # if predictive_cue_selection is active this frame...
                        if predictive_cue_selection.status == STARTED:
                            # update params
                            pass
                        
                        # if predictive_cue_selection is stopping this frame...
                        if predictive_cue_selection.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > predictive_cue_selection.tStartRefresh + 0.5-frameTolerance:
                                # keep track of stop time/frame for later
                                predictive_cue_selection.tStop = t  # not accounting for scr refresh
                                predictive_cue_selection.tStopRefresh = tThisFlipGlobal  # on global time
                                predictive_cue_selection.frameNStop = frameN  # exact frame index
                                # update status
                                predictive_cue_selection.status = FINISHED
                                predictive_cue_selection.setAutoDraw(False)
                        
                        # *non_predictive_cue_selection* updates
                        
                        # if non_predictive_cue_selection is starting this frame...
                        if non_predictive_cue_selection.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            non_predictive_cue_selection.frameNStart = frameN  # exact frame index
                            non_predictive_cue_selection.tStart = t  # local t and not account for scr refresh
                            non_predictive_cue_selection.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(non_predictive_cue_selection, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            non_predictive_cue_selection.status = STARTED
                            non_predictive_cue_selection.setAutoDraw(True)
                        
                        # if non_predictive_cue_selection is active this frame...
                        if non_predictive_cue_selection.status == STARTED:
                            # update params
                            pass
                        
                        # if non_predictive_cue_selection is stopping this frame...
                        if non_predictive_cue_selection.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > non_predictive_cue_selection.tStartRefresh + 0.5-frameTolerance:
                                # keep track of stop time/frame for later
                                non_predictive_cue_selection.tStop = t  # not accounting for scr refresh
                                non_predictive_cue_selection.tStopRefresh = tThisFlipGlobal  # on global time
                                non_predictive_cue_selection.frameNStop = frameN  # exact frame index
                                # update status
                                non_predictive_cue_selection.status = FINISHED
                                non_predictive_cue_selection.setAutoDraw(False)
                        
                        # *o1_image_selection* updates
                        
                        # if o1_image_selection is starting this frame...
                        if o1_image_selection.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            o1_image_selection.frameNStart = frameN  # exact frame index
                            o1_image_selection.tStart = t  # local t and not account for scr refresh
                            o1_image_selection.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(o1_image_selection, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            o1_image_selection.status = STARTED
                            o1_image_selection.setAutoDraw(True)
                        
                        # if o1_image_selection is active this frame...
                        if o1_image_selection.status == STARTED:
                            # update params
                            pass
                        
                        # if o1_image_selection is stopping this frame...
                        if o1_image_selection.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > o1_image_selection.tStartRefresh + 0.5-frameTolerance:
                                # keep track of stop time/frame for later
                                o1_image_selection.tStop = t  # not accounting for scr refresh
                                o1_image_selection.tStopRefresh = tThisFlipGlobal  # on global time
                                o1_image_selection.frameNStop = frameN  # exact frame index
                                # update status
                                o1_image_selection.status = FINISHED
                                o1_image_selection.setAutoDraw(False)
                        
                        # *o2_image_selection* updates
                        
                        # if o2_image_selection is starting this frame...
                        if o2_image_selection.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            o2_image_selection.frameNStart = frameN  # exact frame index
                            o2_image_selection.tStart = t  # local t and not account for scr refresh
                            o2_image_selection.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(o2_image_selection, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            o2_image_selection.status = STARTED
                            o2_image_selection.setAutoDraw(True)
                        
                        # if o2_image_selection is active this frame...
                        if o2_image_selection.status == STARTED:
                            # update params
                            pass
                        
                        # if o2_image_selection is stopping this frame...
                        if o2_image_selection.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > o2_image_selection.tStartRefresh + 0.5-frameTolerance:
                                # keep track of stop time/frame for later
                                o2_image_selection.tStop = t  # not accounting for scr refresh
                                o2_image_selection.tStopRefresh = tThisFlipGlobal  # on global time
                                o2_image_selection.frameNStop = frameN  # exact frame index
                                # update status
                                o2_image_selection.status = FINISHED
                                o2_image_selection.setAutoDraw(False)
                        
                        # *yellow_frame* updates
                        
                        # if yellow_frame is starting this frame...
                        if yellow_frame.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            yellow_frame.frameNStart = frameN  # exact frame index
                            yellow_frame.tStart = t  # local t and not account for scr refresh
                            yellow_frame.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(yellow_frame, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            yellow_frame.status = STARTED
                            yellow_frame.setAutoDraw(True)
                        
                        # if yellow_frame is active this frame...
                        if yellow_frame.status == STARTED:
                            # update params
                            pass
                        
                        # if yellow_frame is stopping this frame...
                        if yellow_frame.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > yellow_frame.tStartRefresh + 0.5-frameTolerance:
                                # keep track of stop time/frame for later
                                yellow_frame.tStop = t  # not accounting for scr refresh
                                yellow_frame.tStopRefresh = tThisFlipGlobal  # on global time
                                yellow_frame.frameNStop = frameN  # exact frame index
                                # update status
                                yellow_frame.status = FINISHED
                                yellow_frame.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        
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
                    thisExp.addData('cue_selection.stopped', globalClock.getTime(format='float'))
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-0.500000)
                    
                    # --- Prepare to start Routine "feedback" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('feedback.started', globalClock.getTime(format='float'))
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
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 2.0:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *feedback_text* updates
                        
                        # if feedback_text is starting this frame...
                        if feedback_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            feedback_text.frameNStart = frameN  # exact frame index
                            feedback_text.tStart = t  # local t and not account for scr refresh
                            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            feedback_text.status = STARTED
                            feedback_text.setAutoDraw(True)
                        
                        # if feedback_text is active this frame...
                        if feedback_text.status == STARTED:
                            # update params
                            pass
                        
                        # if feedback_text is stopping this frame...
                        if feedback_text.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > feedback_text.tStartRefresh + 2-frameTolerance:
                                # keep track of stop time/frame for later
                                feedback_text.tStop = t  # not accounting for scr refresh
                                feedback_text.tStopRefresh = tThisFlipGlobal  # on global time
                                feedback_text.frameNStop = frameN  # exact frame index
                                # update status
                                feedback_text.status = FINISHED
                                feedback_text.setAutoDraw(False)
                        
                        # *predictive_cue_feedback* updates
                        
                        # if predictive_cue_feedback is starting this frame...
                        if predictive_cue_feedback.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            predictive_cue_feedback.frameNStart = frameN  # exact frame index
                            predictive_cue_feedback.tStart = t  # local t and not account for scr refresh
                            predictive_cue_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(predictive_cue_feedback, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            predictive_cue_feedback.status = STARTED
                            predictive_cue_feedback.setAutoDraw(True)
                        
                        # if predictive_cue_feedback is active this frame...
                        if predictive_cue_feedback.status == STARTED:
                            # update params
                            pass
                        
                        # if predictive_cue_feedback is stopping this frame...
                        if predictive_cue_feedback.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > predictive_cue_feedback.tStartRefresh + 2-frameTolerance:
                                # keep track of stop time/frame for later
                                predictive_cue_feedback.tStop = t  # not accounting for scr refresh
                                predictive_cue_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                                predictive_cue_feedback.frameNStop = frameN  # exact frame index
                                # update status
                                predictive_cue_feedback.status = FINISHED
                                predictive_cue_feedback.setAutoDraw(False)
                        
                        # *non_predictive_cue_feedback* updates
                        
                        # if non_predictive_cue_feedback is starting this frame...
                        if non_predictive_cue_feedback.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            non_predictive_cue_feedback.frameNStart = frameN  # exact frame index
                            non_predictive_cue_feedback.tStart = t  # local t and not account for scr refresh
                            non_predictive_cue_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(non_predictive_cue_feedback, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            non_predictive_cue_feedback.status = STARTED
                            non_predictive_cue_feedback.setAutoDraw(True)
                        
                        # if non_predictive_cue_feedback is active this frame...
                        if non_predictive_cue_feedback.status == STARTED:
                            # update params
                            pass
                        
                        # if non_predictive_cue_feedback is stopping this frame...
                        if non_predictive_cue_feedback.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > non_predictive_cue_feedback.tStartRefresh + 2-frameTolerance:
                                # keep track of stop time/frame for later
                                non_predictive_cue_feedback.tStop = t  # not accounting for scr refresh
                                non_predictive_cue_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                                non_predictive_cue_feedback.frameNStop = frameN  # exact frame index
                                # update status
                                non_predictive_cue_feedback.status = FINISHED
                                non_predictive_cue_feedback.setAutoDraw(False)
                        
                        # *o1_image_feedback* updates
                        
                        # if o1_image_feedback is starting this frame...
                        if o1_image_feedback.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            o1_image_feedback.frameNStart = frameN  # exact frame index
                            o1_image_feedback.tStart = t  # local t and not account for scr refresh
                            o1_image_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(o1_image_feedback, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            o1_image_feedback.status = STARTED
                            o1_image_feedback.setAutoDraw(True)
                        
                        # if o1_image_feedback is active this frame...
                        if o1_image_feedback.status == STARTED:
                            # update params
                            pass
                        
                        # if o1_image_feedback is stopping this frame...
                        if o1_image_feedback.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > o1_image_feedback.tStartRefresh + 2-frameTolerance:
                                # keep track of stop time/frame for later
                                o1_image_feedback.tStop = t  # not accounting for scr refresh
                                o1_image_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                                o1_image_feedback.frameNStop = frameN  # exact frame index
                                # update status
                                o1_image_feedback.status = FINISHED
                                o1_image_feedback.setAutoDraw(False)
                        
                        # *o2_image_feedback* updates
                        
                        # if o2_image_feedback is starting this frame...
                        if o2_image_feedback.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            o2_image_feedback.frameNStart = frameN  # exact frame index
                            o2_image_feedback.tStart = t  # local t and not account for scr refresh
                            o2_image_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(o2_image_feedback, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            o2_image_feedback.status = STARTED
                            o2_image_feedback.setAutoDraw(True)
                        
                        # if o2_image_feedback is active this frame...
                        if o2_image_feedback.status == STARTED:
                            # update params
                            pass
                        
                        # if o2_image_feedback is stopping this frame...
                        if o2_image_feedback.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > o2_image_feedback.tStartRefresh + 2-frameTolerance:
                                # keep track of stop time/frame for later
                                o2_image_feedback.tStop = t  # not accounting for scr refresh
                                o2_image_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                                o2_image_feedback.frameNStop = frameN  # exact frame index
                                # update status
                                o2_image_feedback.status = FINISHED
                                o2_image_feedback.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        
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
                    thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-2.000000)
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed feedback_reps repeats of 'stage2_feedback_loop'
                
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed stage2Reps repeats of 'stage2_trials'
            
            
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
                    globals()[paramName] = thisVsubtle_loop[paramName]
            
            for thisVsubtle_loop in vsubtle_loop:
                currentLoop = vsubtle_loop
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisVsubtle_loop.rgb)
                if thisVsubtle_loop != None:
                    for paramName in thisVsubtle_loop:
                        globals()[paramName] = thisVsubtle_loop[paramName]
                
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
                        globals()[paramName] = thisTask3_instr_vsubtle[paramName]
                
                for thisTask3_instr_vsubtle in task3_instr_vsubtle:
                    currentLoop = task3_instr_vsubtle
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisTask3_instr_vsubtle.rgb)
                    if thisTask3_instr_vsubtle != None:
                        for paramName in thisTask3_instr_vsubtle:
                            globals()[paramName] = thisTask3_instr_vsubtle[paramName]
                    
                    # --- Prepare to start Routine "test2_vsubtle_inst" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('test2_vsubtle_inst.started', globalClock.getTime(format='float'))
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
                    routineForceEnded = not continueRoutine
                    while continueRoutine:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *cont_test2_vsubtle* updates
                        
                        # if cont_test2_vsubtle is starting this frame...
                        if cont_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            cont_test2_vsubtle.frameNStart = frameN  # exact frame index
                            cont_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                            cont_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(cont_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            cont_test2_vsubtle.status = STARTED
                            cont_test2_vsubtle.setAutoDraw(True)
                        
                        # if cont_test2_vsubtle is active this frame...
                        if cont_test2_vsubtle.status == STARTED:
                            # update params
                            pass
                        # *cont_mouse_test2_vsubtle* updates
                        
                        # if cont_mouse_test2_vsubtle is starting this frame...
                        if cont_mouse_test2_vsubtle.status == NOT_STARTED and t >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            cont_mouse_test2_vsubtle.frameNStart = frameN  # exact frame index
                            cont_mouse_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                            cont_mouse_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(cont_mouse_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                            # update status
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
                                    clickableList = environmenttools.getFromNames(cont_test2_vsubtle, namespace=locals())
                                    for obj in clickableList:
                                        # is this object clicked on?
                                        if obj.contains(cont_mouse_test2_vsubtle):
                                            gotValidClick = True
                                            cont_mouse_test2_vsubtle.clicked_name.append(obj.name)
                                    if gotValidClick:  
                                        continueRoutine = False  # end routine on response
                        
                        # *instructions_test2_vsubtle* updates
                        
                        # if instructions_test2_vsubtle is starting this frame...
                        if instructions_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            instructions_test2_vsubtle.frameNStart = frameN  # exact frame index
                            instructions_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                            instructions_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(instructions_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            instructions_test2_vsubtle.status = STARTED
                            instructions_test2_vsubtle.setAutoDraw(True)
                        
                        # if instructions_test2_vsubtle is active this frame...
                        if instructions_test2_vsubtle.status == STARTED:
                            # update params
                            pass
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        
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
                    thisExp.addData('test2_vsubtle_inst.stopped', globalClock.getTime(format='float'))
                    # store data for task3_instr_vsubtle (TrialHandler)
                    # the Routine "test2_vsubtle_inst" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed 1.0 repeats of 'task3_instr_vsubtle'
                
                
                # --- Prepare to start Routine "comprehension3" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('comprehension3.started', globalClock.getTime(format='float'))
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
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *comp3_resp2* updates
                    
                    # if comp3_resp2 is starting this frame...
                    if comp3_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        comp3_resp2.frameNStart = frameN  # exact frame index
                        comp3_resp2.tStart = t  # local t and not account for scr refresh
                        comp3_resp2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(comp3_resp2, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        comp3_resp2.status = STARTED
                        comp3_resp2.setAutoDraw(True)
                    
                    # if comp3_resp2 is active this frame...
                    if comp3_resp2.status == STARTED:
                        # update params
                        pass
                    
                    # *comp3_resp1* updates
                    
                    # if comp3_resp1 is starting this frame...
                    if comp3_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        comp3_resp1.frameNStart = frameN  # exact frame index
                        comp3_resp1.tStart = t  # local t and not account for scr refresh
                        comp3_resp1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(comp3_resp1, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        comp3_resp1.status = STARTED
                        comp3_resp1.setAutoDraw(True)
                    
                    # if comp3_resp1 is active this frame...
                    if comp3_resp1.status == STARTED:
                        # update params
                        pass
                    
                    # *comp3_resp3* updates
                    
                    # if comp3_resp3 is starting this frame...
                    if comp3_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        comp3_resp3.frameNStart = frameN  # exact frame index
                        comp3_resp3.tStart = t  # local t and not account for scr refresh
                        comp3_resp3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(comp3_resp3, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        comp3_resp3.status = STARTED
                        comp3_resp3.setAutoDraw(True)
                    
                    # if comp3_resp3 is active this frame...
                    if comp3_resp3.status == STARTED:
                        # update params
                        pass
                    # *comp3_mouse* updates
                    
                    # if comp3_mouse is starting this frame...
                    if comp3_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        comp3_mouse.frameNStart = frameN  # exact frame index
                        comp3_mouse.tStart = t  # local t and not account for scr refresh
                        comp3_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(comp3_mouse, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        comp3_mouse.status = STARTED
                        prevButtonState = comp3_mouse.getPressed()  # if button is down already this ISN'T a new click
                    if comp3_mouse.status == STARTED:  # only update if started and not finished!
                        buttons = comp3_mouse.getPressed()
                        if buttons != prevButtonState:  # button state changed?
                            prevButtonState = buttons
                            if sum(buttons) > 0:  # state changed to a new click
                                # check if the mouse was inside our 'clickable' objects
                                gotValidClick = False
                                clickableList = environmenttools.getFromNames([comp3_resp1, comp3_resp2, comp3_resp3], namespace=locals())
                                for obj in clickableList:
                                    # is this object clicked on?
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
                                    continueRoutine = False  # end routine on response
                    
                    # *check3* updates
                    
                    # if check3 is starting this frame...
                    if check3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        check3.frameNStart = frameN  # exact frame index
                        check3.tStart = t  # local t and not account for scr refresh
                        check3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(check3, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        check3.status = STARTED
                        check3.setAutoDraw(True)
                    
                    # if check3 is active this frame...
                    if check3.status == STARTED:
                        # update params
                        pass
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    
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
                thisExp.addData('comprehension3.stopped', globalClock.getTime(format='float'))
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
                    trialList=data.importConditions('test2.xlsx'),
                    seed=None, name='test2_vsubtle_trials')
                thisExp.addLoop(test2_vsubtle_trials)  # add the loop to the experiment
                thisTest2_vsubtle_trial = test2_vsubtle_trials.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTest2_vsubtle_trial.rgb)
                if thisTest2_vsubtle_trial != None:
                    for paramName in thisTest2_vsubtle_trial:
                        globals()[paramName] = thisTest2_vsubtle_trial[paramName]
                
                for thisTest2_vsubtle_trial in test2_vsubtle_trials:
                    currentLoop = test2_vsubtle_trials
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisTest2_vsubtle_trial.rgb)
                    if thisTest2_vsubtle_trial != None:
                        for paramName in thisTest2_vsubtle_trial:
                            globals()[paramName] = thisTest2_vsubtle_trial[paramName]
                    
                    # --- Prepare to start Routine "test2_vsubtle_choice" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('test2_vsubtle_choice.started', globalClock.getTime(format='float'))
                    # Run 'Begin Routine' code from target_determination_2
                    if target == 1:
                        stim1 = reorder_cues[0]
                    elif target == 2:
                        stim1 = reorder_cues[1]
                    elif target == 3:
                        stim1 = reorder_cues[2]
                    elif target == 4:
                        stim1 = reorder_cues[3]
                    elif target == 5:
                        stim1 = reorder_cues[4]
                    elif target == 6:
                        stim1 = reorder_cues[5]
                    elif target == 7:
                        stim1 = reorder_cues[6]
                    elif target == 8:
                        stim1 = reorder_cues[7]
                    # Run 'Begin Routine' code from distractor_presentation_test2_vsubtle
                    if distractor_test2 == 1:
                        distractor = reorder_vsubtle[0]
                    elif distractor_test2 == 2:
                        distractor = reorder_vsubtle[1]
                    elif distractor_test2 == 3:
                        distractor = reorder_vsubtle[2]
                    elif distractor_test2 == 4:
                        distractor = reorder_vsubtle[3]
                    elif distractor_test2 == 5:
                        distractor = reorder_vsubtle[4]
                    elif distractor_test2 == 6:
                        distractor = reorder_vsubtle[5]
                    elif distractor_test2 == 7:
                        distractor = reorder_vsubtle[6]
                    elif distractor_test2 == 8:
                        distractor = reorder_vsubtle[7]
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
                    routineForceEnded = not continueRoutine
                    while continueRoutine:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *blank_test2_vsubtle* updates
                        
                        # if blank_test2_vsubtle is starting this frame...
                        if blank_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            blank_test2_vsubtle.frameNStart = frameN  # exact frame index
                            blank_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                            blank_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(blank_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            blank_test2_vsubtle.status = STARTED
                            blank_test2_vsubtle.setAutoDraw(True)
                        
                        # if blank_test2_vsubtle is active this frame...
                        if blank_test2_vsubtle.status == STARTED:
                            # update params
                            pass
                        
                        # if blank_test2_vsubtle is stopping this frame...
                        if blank_test2_vsubtle.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > blank_test2_vsubtle.tStartRefresh + 0.5-frameTolerance:
                                # keep track of stop time/frame for later
                                blank_test2_vsubtle.tStop = t  # not accounting for scr refresh
                                blank_test2_vsubtle.tStopRefresh = tThisFlipGlobal  # on global time
                                blank_test2_vsubtle.frameNStop = frameN  # exact frame index
                                # update status
                                blank_test2_vsubtle.status = FINISHED
                                blank_test2_vsubtle.setAutoDraw(False)
                        
                        # *target_test2_vsubtle* updates
                        
                        # if target_test2_vsubtle is starting this frame...
                        if target_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                            # keep track of start time/frame for later
                            target_test2_vsubtle.frameNStart = frameN  # exact frame index
                            target_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                            target_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(target_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            target_test2_vsubtle.status = STARTED
                            target_test2_vsubtle.setAutoDraw(True)
                        
                        # if target_test2_vsubtle is active this frame...
                        if target_test2_vsubtle.status == STARTED:
                            # update params
                            pass
                        
                        # *distractor_test2_vsubtle* updates
                        
                        # if distractor_test2_vsubtle is starting this frame...
                        if distractor_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                            # keep track of start time/frame for later
                            distractor_test2_vsubtle.frameNStart = frameN  # exact frame index
                            distractor_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                            distractor_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(distractor_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            distractor_test2_vsubtle.status = STARTED
                            distractor_test2_vsubtle.setAutoDraw(True)
                        
                        # if distractor_test2_vsubtle is active this frame...
                        if distractor_test2_vsubtle.status == STARTED:
                            # update params
                            pass
                        # *mouse_test2_vsubtle* updates
                        
                        # if mouse_test2_vsubtle is starting this frame...
                        if mouse_test2_vsubtle.status == NOT_STARTED and t >= 0.5-frameTolerance:
                            # keep track of start time/frame for later
                            mouse_test2_vsubtle.frameNStart = frameN  # exact frame index
                            mouse_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                            mouse_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(mouse_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                            # update status
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
                                    clickableList = environmenttools.getFromNames([target_test2_vsubtle, distractor_test2_vsubtle], namespace=locals())
                                    for obj in clickableList:
                                        # is this object clicked on?
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
                                        continueRoutine = False  # end routine on response
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        
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
                    thisExp.addData('test2_vsubtle_choice.stopped', globalClock.getTime(format='float'))
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
                    # update component parameters for each repeat
                    thisExp.addData('test2_vsubtle_rate.started', globalClock.getTime(format='float'))
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
                    routineForceEnded = not continueRoutine
                    while continueRoutine:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *slider_text_test2_vsubtle* updates
                        
                        # if slider_text_test2_vsubtle is starting this frame...
                        if slider_text_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            slider_text_test2_vsubtle.frameNStart = frameN  # exact frame index
                            slider_text_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                            slider_text_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(slider_text_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            slider_text_test2_vsubtle.status = STARTED
                            slider_text_test2_vsubtle.setAutoDraw(True)
                        
                        # if slider_text_test2_vsubtle is active this frame...
                        if slider_text_test2_vsubtle.status == STARTED:
                            # update params
                            pass
                        
                        # *slider_test2_vsubtle* updates
                        
                        # if slider_test2_vsubtle is starting this frame...
                        if slider_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            slider_test2_vsubtle.frameNStart = frameN  # exact frame index
                            slider_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                            slider_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(slider_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            slider_test2_vsubtle.status = STARTED
                            slider_test2_vsubtle.setAutoDraw(True)
                        
                        # if slider_test2_vsubtle is active this frame...
                        if slider_test2_vsubtle.status == STARTED:
                            # update params
                            pass
                        
                        # *slider_target_test2_vsubtle* updates
                        
                        # if slider_target_test2_vsubtle is starting this frame...
                        if slider_target_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            slider_target_test2_vsubtle.frameNStart = frameN  # exact frame index
                            slider_target_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                            slider_target_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(slider_target_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            slider_target_test2_vsubtle.status = STARTED
                            slider_target_test2_vsubtle.setAutoDraw(True)
                        
                        # if slider_target_test2_vsubtle is active this frame...
                        if slider_target_test2_vsubtle.status == STARTED:
                            # update params
                            pass
                        
                        # *slider_distractor_test2_vsubtle* updates
                        
                        # if slider_distractor_test2_vsubtle is starting this frame...
                        if slider_distractor_test2_vsubtle.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            slider_distractor_test2_vsubtle.frameNStart = frameN  # exact frame index
                            slider_distractor_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                            slider_distractor_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(slider_distractor_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            slider_distractor_test2_vsubtle.status = STARTED
                            slider_distractor_test2_vsubtle.setAutoDraw(True)
                        
                        # if slider_distractor_test2_vsubtle is active this frame...
                        if slider_distractor_test2_vsubtle.status == STARTED:
                            # update params
                            pass
                        # Run 'Each Frame' code from show_continue_rate_test2_vsubtle
                        slid2 = slider_test2_vsubtle.getRating()
                        
                        if slid2:
                            show_continue_test2_vsubtle = True
                        else:
                            show_continue_test2_vsubtle = False
                        
                        # *continue_rate_test2_vsubtle* updates
                        
                        # if continue_rate_test2_vsubtle is starting this frame...
                        if continue_rate_test2_vsubtle.status == NOT_STARTED and show_continue_test2_vsubtle:
                            # keep track of start time/frame for later
                            continue_rate_test2_vsubtle.frameNStart = frameN  # exact frame index
                            continue_rate_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                            continue_rate_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(continue_rate_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                            # update status
                            continue_rate_test2_vsubtle.status = STARTED
                            continue_rate_test2_vsubtle.setAutoDraw(True)
                        
                        # if continue_rate_test2_vsubtle is active this frame...
                        if continue_rate_test2_vsubtle.status == STARTED:
                            # update params
                            pass
                        # *mouse_continue_test2_vsubtle* updates
                        
                        # if mouse_continue_test2_vsubtle is starting this frame...
                        if mouse_continue_test2_vsubtle.status == NOT_STARTED and t >= show_continue_test2_vsubtle-frameTolerance:
                            # keep track of start time/frame for later
                            mouse_continue_test2_vsubtle.frameNStart = frameN  # exact frame index
                            mouse_continue_test2_vsubtle.tStart = t  # local t and not account for scr refresh
                            mouse_continue_test2_vsubtle.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(mouse_continue_test2_vsubtle, 'tStartRefresh')  # time at next scr refresh
                            # update status
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
                                    clickableList = environmenttools.getFromNames(continue_rate_test2_vsubtle, namespace=locals())
                                    for obj in clickableList:
                                        # is this object clicked on?
                                        if obj.contains(mouse_continue_test2_vsubtle):
                                            gotValidClick = True
                                            mouse_continue_test2_vsubtle.clicked_name.append(obj.name)
                                    if gotValidClick:  
                                        continueRoutine = False  # end routine on response
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        
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
                    thisExp.addData('test2_vsubtle_rate.stopped', globalClock.getTime(format='float'))
                    test2_vsubtle_trials.addData('slider_test2_vsubtle.response', slider_test2_vsubtle.getRating())
                    test2_vsubtle_trials.addData('slider_test2_vsubtle.rt', slider_test2_vsubtle.getRT())
                    # store data for test2_vsubtle_trials (TrialHandler)
                    # the Routine "test2_vsubtle_rate" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed 1.0 repeats of 'test2_vsubtle_trials'
                
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 1.0 repeats of 'vsubtle_loop'
            
            
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
                    globals()[paramName] = thisDebrief_loop[paramName]
            
            for thisDebrief_loop in debrief_loop:
                currentLoop = debrief_loop
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisDebrief_loop.rgb)
                if thisDebrief_loop != None:
                    for paramName in thisDebrief_loop:
                        globals()[paramName] = thisDebrief_loop[paramName]
                
                # --- Prepare to start Routine "debrief" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('debrief.started', globalClock.getTime(format='float'))
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
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *cont_debrief* updates
                    
                    # if cont_debrief is starting this frame...
                    if cont_debrief.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_debrief.frameNStart = frameN  # exact frame index
                        cont_debrief.tStart = t  # local t and not account for scr refresh
                        cont_debrief.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_debrief, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        cont_debrief.status = STARTED
                        cont_debrief.setAutoDraw(True)
                    
                    # if cont_debrief is active this frame...
                    if cont_debrief.status == STARTED:
                        # update params
                        pass
                    # *cont_debrief_mouse* updates
                    
                    # if cont_debrief_mouse is starting this frame...
                    if cont_debrief_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        cont_debrief_mouse.frameNStart = frameN  # exact frame index
                        cont_debrief_mouse.tStart = t  # local t and not account for scr refresh
                        cont_debrief_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(cont_debrief_mouse, 'tStartRefresh')  # time at next scr refresh
                        # update status
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
                                clickableList = environmenttools.getFromNames(cont_debrief, namespace=locals())
                                for obj in clickableList:
                                    # is this object clicked on?
                                    if obj.contains(cont_debrief_mouse):
                                        gotValidClick = True
                                        cont_debrief_mouse.clicked_name.append(obj.name)
                                if gotValidClick:  
                                    continueRoutine = False  # end routine on response
                    
                    # *debrief_image* updates
                    
                    # if debrief_image is starting this frame...
                    if debrief_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        debrief_image.frameNStart = frameN  # exact frame index
                        debrief_image.tStart = t  # local t and not account for scr refresh
                        debrief_image.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(debrief_image, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        debrief_image.status = STARTED
                        debrief_image.setAutoDraw(True)
                    
                    # if debrief_image is active this frame...
                    if debrief_image.status == STARTED:
                        # update params
                        pass
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    
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
                thisExp.addData('debrief.stopped', globalClock.getTime(format='float'))
                # store data for debrief_loop (TrialHandler)
                # the Routine "debrief" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 1.0 repeats of 'debrief_loop'
            
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
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
                globals()[paramName] = thisNo_compr_loop[paramName]
        
        for thisNo_compr_loop in no_compr_loop:
            currentLoop = no_compr_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisNo_compr_loop.rgb)
            if thisNo_compr_loop != None:
                for paramName in thisNo_compr_loop:
                    globals()[paramName] = thisNo_compr_loop[paramName]
            
            # --- Prepare to start Routine "no_comprehension" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('no_comprehension.started', globalClock.getTime(format='float'))
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
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *no_compr_textbox* updates
                
                # if no_compr_textbox is starting this frame...
                if no_compr_textbox.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    no_compr_textbox.frameNStart = frameN  # exact frame index
                    no_compr_textbox.tStart = t  # local t and not account for scr refresh
                    no_compr_textbox.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(no_compr_textbox, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    no_compr_textbox.status = STARTED
                    no_compr_textbox.setAutoDraw(True)
                
                # if no_compr_textbox is active this frame...
                if no_compr_textbox.status == STARTED:
                    # update params
                    pass
                
                # *exit_box_no_compr* updates
                
                # if exit_box_no_compr is starting this frame...
                if exit_box_no_compr.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    exit_box_no_compr.frameNStart = frameN  # exact frame index
                    exit_box_no_compr.tStart = t  # local t and not account for scr refresh
                    exit_box_no_compr.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(exit_box_no_compr, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    exit_box_no_compr.status = STARTED
                    exit_box_no_compr.setAutoDraw(True)
                
                # if exit_box_no_compr is active this frame...
                if exit_box_no_compr.status == STARTED:
                    # update params
                    pass
                # *mouse_exit_no_compr* updates
                
                # if mouse_exit_no_compr is starting this frame...
                if mouse_exit_no_compr.status == NOT_STARTED and t >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_exit_no_compr.frameNStart = frameN  # exact frame index
                    mouse_exit_no_compr.tStart = t  # local t and not account for scr refresh
                    mouse_exit_no_compr.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_exit_no_compr, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('mouse_exit_no_compr.started', t)
                    # update status
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
                            clickableList = environmenttools.getFromNames(exit_box_no_compr, namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(mouse_exit_no_compr):
                                    gotValidClick = True
                                    mouse_exit_no_compr.clicked_name.append(obj.name)
                            if gotValidClick:  
                                continueRoutine = False  # end routine on response
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
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
            thisExp.addData('no_comprehension.stopped', globalClock.getTime(format='float'))
            # store data for no_compr_loop (TrialHandler)
            # the Routine "no_comprehension" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed no_compr repeats of 'no_compr_loop'
        
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
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
            globals()[paramName] = thisNo_consent_loop[paramName]
    
    for thisNo_consent_loop in no_consent_loop:
        currentLoop = no_consent_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisNo_consent_loop.rgb)
        if thisNo_consent_loop != None:
            for paramName in thisNo_consent_loop:
                globals()[paramName] = thisNo_consent_loop[paramName]
        
        # --- Prepare to start Routine "no_consent_trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('no_consent_trial.started', globalClock.getTime(format='float'))
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
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *no_consent_textbox* updates
            
            # if no_consent_textbox is starting this frame...
            if no_consent_textbox.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                no_consent_textbox.frameNStart = frameN  # exact frame index
                no_consent_textbox.tStart = t  # local t and not account for scr refresh
                no_consent_textbox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(no_consent_textbox, 'tStartRefresh')  # time at next scr refresh
                # update status
                no_consent_textbox.status = STARTED
                no_consent_textbox.setAutoDraw(True)
            
            # if no_consent_textbox is active this frame...
            if no_consent_textbox.status == STARTED:
                # update params
                pass
            
            # *exit_box* updates
            
            # if exit_box is starting this frame...
            if exit_box.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                exit_box.frameNStart = frameN  # exact frame index
                exit_box.tStart = t  # local t and not account for scr refresh
                exit_box.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(exit_box, 'tStartRefresh')  # time at next scr refresh
                # update status
                exit_box.status = STARTED
                exit_box.setAutoDraw(True)
            
            # if exit_box is active this frame...
            if exit_box.status == STARTED:
                # update params
                pass
            # *mouse_exit* updates
            
            # if mouse_exit is starting this frame...
            if mouse_exit.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                mouse_exit.frameNStart = frameN  # exact frame index
                mouse_exit.tStart = t  # local t and not account for scr refresh
                mouse_exit.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_exit, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_exit.started', t)
                # update status
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
                        clickableList = environmenttools.getFromNames(exit_box, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_exit):
                                gotValidClick = True
                                mouse_exit.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
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
        thisExp.addData('no_consent_trial.stopped', globalClock.getTime(format='float'))
        # store data for no_consent_loop (TrialHandler)
        # the Routine "no_consent_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed no_consent repeats of 'no_consent_loop'
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='comma')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
