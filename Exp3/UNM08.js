/************** 
 * Unm08 Test *
 **************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'UNM08';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'age': '',
    'gender': ["male", "female", "non-binary", "other"],
    'condition': `${util.randint(3, 4)}`,
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(counterbalanceRoutineBegin());
flowScheduler.add(counterbalanceRoutineEachFrame());
flowScheduler.add(counterbalanceRoutineEnd());
const information_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(information_loopLoopBegin(information_loopLoopScheduler));
flowScheduler.add(information_loopLoopScheduler);
flowScheduler.add(information_loopLoopEnd);
flowScheduler.add(consentRoutineBegin());
flowScheduler.add(consentRoutineEachFrame());
flowScheduler.add(consentRoutineEnd());
const consent_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(consent_loopLoopBegin(consent_loopLoopScheduler));
flowScheduler.add(consent_loopLoopScheduler);
flowScheduler.add(consent_loopLoopEnd);
const no_consent_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(no_consent_loopLoopBegin(no_consent_loopLoopScheduler));
flowScheduler.add(no_consent_loopLoopScheduler);
flowScheduler.add(no_consent_loopLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'stimuli/cue_a8.png', 'path': 'stimuli/cue_a8.png'},
    {'name': 'task3_instructions.xlsx', 'path': 'task3_instructions.xlsx'},
    {'name': 'debrief.xlsx', 'path': 'debrief.xlsx'},
    {'name': 'instructions/debrief1.png', 'path': 'instructions/debrief1.png'},
    {'name': 'info.xlsx', 'path': 'info.xlsx'},
    {'name': 'stimuli/out2.png', 'path': 'stimuli/out2.png'},
    {'name': 'stimuli/correct_out2.png', 'path': 'stimuli/correct_out2.png'},
    {'name': 'instructions/check1_2.png', 'path': 'instructions/check1_2.png'},
    {'name': 'stimuli/cue_a6.png', 'path': 'stimuli/cue_a6.png'},
    {'name': 'stage2_certain.xlsx', 'path': 'stage2_certain.xlsx'},
    {'name': 'stimuli/cue_a2.png', 'path': 'stimuli/cue_a2.png'},
    {'name': 'stimuli/cue_b1.png', 'path': 'stimuli/cue_b1.png'},
    {'name': 'stimuli/cue_b3.png', 'path': 'stimuli/cue_b3.png'},
    {'name': 'instructions/task3_2.png', 'path': 'instructions/task3_2.png'},
    {'name': 'stimuli/cue_b7.png', 'path': 'stimuli/cue_b7.png'},
    {'name': 'stimuli/yellow_frame.png', 'path': 'stimuli/yellow_frame.png'},
    {'name': 'stage2_uncertain.xlsx', 'path': 'stage2_uncertain.xlsx'},
    {'name': 'stimuli/cue_b5.png', 'path': 'stimuli/cue_b5.png'},
    {'name': 'instructions/task3.png', 'path': 'instructions/task3.png'},
    {'name': 'instructions/task1_3.png', 'path': 'instructions/task1_3.png'},
    {'name': 'instructions/task3_1.png', 'path': 'instructions/task3_1.png'},
    {'name': 'stimuli/cue_b2.png', 'path': 'stimuli/cue_b2.png'},
    {'name': 'stimuli/correct_out1.png', 'path': 'stimuli/correct_out1.png'},
    {'name': 'stimuli/cue_b6.png', 'path': 'stimuli/cue_b6.png'},
    {'name': 'instructions/debrief2.png', 'path': 'instructions/debrief2.png'},
    {'name': 'stimuli/cue_a5.png', 'path': 'stimuli/cue_a5.png'},
    {'name': 'instructions/task1_2.png', 'path': 'instructions/task1_2.png'},
    {'name': 'task1_instructions.xlsx', 'path': 'task1_instructions.xlsx'},
    {'name': 'test2.xlsx', 'path': 'test2.xlsx'},
    {'name': 'stage1_certain.xlsx', 'path': 'stage1_certain.xlsx'},
    {'name': 'stimuli/cue_b4.png', 'path': 'stimuli/cue_b4.png'},
    {'name': 'instructions/task1_1.png', 'path': 'instructions/task1_1.png'},
    {'name': 'stimuli/cue_a1.png', 'path': 'stimuli/cue_a1.png'},
    {'name': 'instructions/check1.png', 'path': 'instructions/check1.png'},
    {'name': 'instructions/check3.png', 'path': 'instructions/check3.png'},
    {'name': 'instructions/info1.png', 'path': 'instructions/info1.png'},
    {'name': 'instructions/debrief3.png', 'path': 'instructions/debrief3.png'},
    {'name': 'stimuli/cue_b8.png', 'path': 'stimuli/cue_b8.png'},
    {'name': 'stimuli/out1.png', 'path': 'stimuli/out1.png'},
    {'name': 'stimuli/cue_a7.png', 'path': 'stimuli/cue_a7.png'},
    {'name': 'instructions/info2.png', 'path': 'instructions/info2.png'},
    {'name': 'stimuli/cue_a4.png', 'path': 'stimuli/cue_a4.png'},
    {'name': 'stimuli/cue_a3.png', 'path': 'stimuli/cue_a3.png'},
    {'name': 'instructions/info3.png', 'path': 'instructions/info3.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://app.prolific.com/submissions/complete?cc=C1FGHRA9', '');

  return Scheduler.Event.NEXT;
}


var counterbalanceClock;
var stage2File;
var stage2Reps;
var informationClock;
var continue_info;
var mouse_info;
var image_info;
var consentClock;
var c1;
var c2;
var c3;
var c4;
var c5;
var c6;
var slider_1;
var slider_2;
var slider_3;
var slider_4;
var slider_5;
var slider_6;
var mouse_consent;
var consent_box;
var instructions_1Clock;
var cont_train_instr;
var cont_train_instr_mouse;
var train_instructions;
var comprehension1Clock;
var comp1_resp1;
var comp1_resp2;
var comp1_resp3;
var comp1_mouse;
var check1;
var comprehension1_2Clock;
var comp1_resp1_2;
var comp1_resp2_2;
var comp1_resp3_2;
var comp1_mouse_2;
var check1_2;
var cue_o__trialClock;
var cues;
var distractors_vsubtle;
var order;
var reorder_cues;
var reorder_vsubtle;
var blank_training;
var predictive_cue;
var non_predictive_cue;
var o1_image;
var o2_image;
var cue_o_mouse;
var timeout_text;
var cue_selectionClock;
var predictive_cue_selection;
var non_predictive_cue_selection;
var o1_image_selection;
var o2_image_selection;
var yellow_frame;
var feedbackClock;
var feedback_text;
var predictive_cue_feedback;
var non_predictive_cue_feedback;
var o1_image_feedback;
var o2_image_feedback;
var test2_vsubtle_instClock;
var cont_test2_vsubtle;
var cont_mouse_test2_vsubtle;
var instructions_test2_vsubtle;
var comprehension3Clock;
var comp3_resp2;
var comp3_resp1;
var comp3_resp3;
var comp3_mouse;
var check3;
var test2_vsubtle_choiceClock;
var blank_test2_vsubtle;
var target_test2_vsubtle;
var distractor_test2_vsubtle;
var mouse_test2_vsubtle;
var test2_vsubtle_rateClock;
var slider_text_test2_vsubtle;
var slider_test2_vsubtle;
var slider_target_test2_vsubtle;
var slider_distractor_test2_vsubtle;
var continue_rate_test2_vsubtle;
var mouse_continue_test2_vsubtle;
var debriefClock;
var cont_debrief;
var cont_debrief_mouse;
var debrief_image;
var no_comprehensionClock;
var no_compr_textbox;
var exit_box_no_compr;
var mouse_exit_no_compr;
var no_consent_trialClock;
var no_consent_textbox;
var exit_box;
var mouse_exit;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "counterbalance"
  counterbalanceClock = new util.Clock();
  if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    quitPsychoJS('Mobile device detected. Goodbye!', false)
  }
  
  // Run 'Begin Experiment' code from counterbalance_2
  if ((Number.parseInt(expInfo["condition"]) === 1)) {
      stage2File = "stage2_certain.xlsx";
      stage2Reps = 4;
  } else {
      if ((Number.parseInt(expInfo["condition"]) === 2)) {
          stage2File = "stage2_uncertain.xlsx";
          stage2Reps = 4;
      } else {
          if ((Number.parseInt(expInfo["condition"]) === 3)) {
              stage2File = "stage2_uncertain.xlsx";
              stage2Reps = 0;
          }
      }
  }
  
  // Initialize components for Routine "information"
  informationClock = new util.Clock();
  continue_info = new visual.TextBox({
    win: psychoJS.window,
    name: 'continue_info',
    text: 'CONTINUE',
    font: 'Trebuchet MS',
    pos: [0, (- 0.45)], letterHeight: 0.03,
    size: [0.2, 0.065],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: 'darkgrey', borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  mouse_info = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_info.mouseClock = new util.Clock();
  image_info = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_info', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.45, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "consent"
  consentClock = new util.Clock();
  c1 = new visual.TextBox({
    win: psychoJS.window,
    name: 'c1',
    text: 'I agree to participate in the study on learning the predictive value of cues as described. I understand that my responses will be treated confidentially and that I have the option to withdraw from the study.',
    font: 'Trebuchet MS',
    pos: [(- 0.2), 0.35], letterHeight: 0.028,
    size: [0.7, 0.2],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  c2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'c2',
    text: 'I understand my participation is completely voluntary.',
    font: 'Trebuchet MS',
    pos: [(- 0.2), 0.2], letterHeight: 0.028,
    size: [0.7, 0.2],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  c3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'c3',
    text: 'I understand I have the right to withdraw from the study at any time during or at the end of the study without giving a reason and with no adverse consequences.',
    font: 'Trebuchet MS',
    pos: [(- 0.2), 0.05], letterHeight: 0.028,
    size: [0.7, 0.2],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  c4 = new visual.TextBox({
    win: psychoJS.window,
    name: 'c4',
    text: 'I have been given full information about what the study entails.',
    font: 'Trebuchet MS',
    pos: [(- 0.2), (- 0.125)], letterHeight: 0.028,
    size: [0.7, 0.2],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  c5 = new visual.TextBox({
    win: psychoJS.window,
    name: 'c5',
    text: 'I have been given contact information for the research team.',
    font: 'Trebuchet MS',
    pos: [(- 0.2), (- 0.25)], letterHeight: 0.028,
    size: [0.7, 0.2],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  c6 = new visual.TextBox({
    win: psychoJS.window,
    name: 'c6',
    text: 'I understand my responses will be fully anonymized.',
    font: 'Trebuchet MS',
    pos: [(- 0.2), (- 0.35)], letterHeight: 0.028,
    size: [0.7, 0.2],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -5.0 
  });
  
  slider_1 = new visual.Slider({
    win: psychoJS.window, name: 'slider_1',
    startValue: undefined,
    size: [0.065, 0.02], pos: [0.37, 0.35], ori: 0.0, units: 'height',
    labels: ["Yes", "No"], fontSize: 0.025, ticks: [1, 2],
    granularity: 1.0, style: ["RADIO"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -6, 
    flip: false,
  });
  
  slider_2 = new visual.Slider({
    win: psychoJS.window, name: 'slider_2',
    startValue: undefined,
    size: [0.065, 0.02], pos: [0.37, 0.2], ori: 0.0, units: 'height',
    labels: ["Yes", "No"], fontSize: 0.025, ticks: [1, 2],
    granularity: 1.0, style: ["RADIO"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -7, 
    flip: false,
  });
  
  slider_3 = new visual.Slider({
    win: psychoJS.window, name: 'slider_3',
    startValue: undefined,
    size: [0.065, 0.02], pos: [0.37, 0.05], ori: 0.0, units: 'height',
    labels: ["Yes", "No"], fontSize: 0.025, ticks: [1, 2],
    granularity: 1.0, style: ["RADIO"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -8, 
    flip: false,
  });
  
  slider_4 = new visual.Slider({
    win: psychoJS.window, name: 'slider_4',
    startValue: undefined,
    size: [0.065, 0.02], pos: [0.37, (- 0.125)], ori: 0.0, units: 'height',
    labels: ["Yes", "No"], fontSize: 0.025, ticks: [1, 2],
    granularity: 1.0, style: ["RADIO"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -9, 
    flip: false,
  });
  
  slider_5 = new visual.Slider({
    win: psychoJS.window, name: 'slider_5',
    startValue: undefined,
    size: [0.065, 0.02], pos: [0.37, (- 0.25)], ori: 0.0, units: 'height',
    labels: ["Yes", "No"], fontSize: 0.025, ticks: [1, 2],
    granularity: 1.0, style: ["RADIO"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -10, 
    flip: false,
  });
  
  slider_6 = new visual.Slider({
    win: psychoJS.window, name: 'slider_6',
    startValue: undefined,
    size: [0.065, 0.02], pos: [0.37, (- 0.35)], ori: 0.0, units: 'height',
    labels: ["Yes", "No"], fontSize: 0.025, ticks: [1, 2],
    granularity: 1.0, style: ["RADIO"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -11, 
    flip: false,
  });
  
  mouse_consent = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_consent.mouseClock = new util.Clock();
  consent_box = new visual.TextBox({
    win: psychoJS.window,
    name: 'consent_box',
    text: 'CONTINUE',
    font: 'Trebuchet MS',
    pos: [0, (- 0.45)], letterHeight: 0.03,
    size: [0.2, 0.065],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: 'darkgrey', borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -14.0 
  });
  
  // Initialize components for Routine "instructions_1"
  instructions_1Clock = new util.Clock();
  cont_train_instr = new visual.TextBox({
    win: psychoJS.window,
    name: 'cont_train_instr',
    text: 'CONTINUE',
    font: 'Trebuchet MS',
    pos: [0, (- 0.45)], letterHeight: 0.03,
    size: [0.2, 0.065],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: 'darkgrey', borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  cont_train_instr_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  cont_train_instr_mouse.mouseClock = new util.Clock();
  train_instructions = new visual.ImageStim({
    win : psychoJS.window,
    name : 'train_instructions', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.4, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "comprehension1"
  comprehension1Clock = new util.Clock();
  comp1_resp1 = new visual.TextBox({
    win: psychoJS.window,
    name: 'comp1_resp1',
    text: 'Learn which mutant would result of each chemicals combination',
    font: 'Trebuchet MS',
    pos: [(- 0.71), (- 0.2)], letterHeight: 0.035,
    size: [1.5, 0.05],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center-left',
    depth: -1.0 
  });
  
  comp1_resp2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'comp1_resp2',
    text: 'Predict which mutant would take over the world',
    font: 'Trebuchet MS',
    pos: [(- 0.71), (- 0.26)], letterHeight: 0.035,
    size: [1.5, 0.05],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center-left',
    depth: -2.0 
  });
  
  comp1_resp3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'comp1_resp3',
    text: 'Decide if the chemicals are organic or inorganic',
    font: 'Trebuchet MS',
    pos: [(- 0.71), (- 0.32)], letterHeight: 0.035,
    size: [1.5, 0.05],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center-left',
    depth: -3.0 
  });
  
  comp1_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  comp1_mouse.mouseClock = new util.Clock();
  check1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'check1', units : undefined, 
    image : 'instructions/check1.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.45, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "comprehension1_2"
  comprehension1_2Clock = new util.Clock();
  comp1_resp1_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'comp1_resp1_2',
    text: 'Learn which mutant would result of each chemicals combination',
    font: 'Trebuchet MS',
    pos: [(- 0.71), (- 0.2)], letterHeight: 0.035,
    size: [1.5, 0.05],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center-left',
    depth: -1.0 
  });
  
  comp1_resp2_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'comp1_resp2_2',
    text: 'Predict which mutant would take over the world',
    font: 'Trebuchet MS',
    pos: [(- 0.71), (- 0.26)], letterHeight: 0.035,
    size: [1.5, 0.05],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center-left',
    depth: -2.0 
  });
  
  comp1_resp3_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'comp1_resp3_2',
    text: 'Decide if the chemicals are organic or inorganic',
    font: 'Trebuchet MS',
    pos: [(- 0.71), (- 0.32)], letterHeight: 0.035,
    size: [1.5, 0.05],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center-left',
    depth: -3.0 
  });
  
  comp1_mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  comp1_mouse_2.mouseClock = new util.Clock();
  check1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'check1_2', units : undefined, 
    image : 'instructions/check1_2.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.45, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "cue_o__trial"
  cue_o__trialClock = new util.Clock();
  // Run 'Begin Experiment' code from cue_random
  cues = ["stimuli/cue_a1.png", "stimuli/cue_a2.png", "stimuli/cue_a3.png", "stimuli/cue_a4.png", "stimuli/cue_a5.png", "stimuli/cue_a6.png", "stimuli/cue_a7.png", "stimuli/cue_a8.png"];
  distractors_vsubtle = ["stimuli/cue_b1.png", "stimuli/cue_b2.png", "stimuli/cue_b3.png", "stimuli/cue_b4.png", "stimuli/cue_b5.png", "stimuli/cue_b6.png", "stimuli/cue_b7.png", "stimuli/cue_b8.png"];
  order = [1, 2, 3, 4, 5, 6, 7, 8];
  util.shuffle(order);
  reorder_cues = function () {
      var _pj_a = [], _pj_b = order;
      for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
          var i = _pj_b[_pj_c];
          _pj_a.push(cues[(i - 1)]);
      }
      return _pj_a;
  }
  .call(this);
  reorder_vsubtle = function () {
      var _pj_a = [], _pj_b = order;
      for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
          var i = _pj_b[_pj_c];
          _pj_a.push(distractors_vsubtle[(i - 1)]);
      }
      return _pj_a;
  }
  .call(this);
  
  blank_training = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank_training',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  predictive_cue = new visual.ImageStim({
    win : psychoJS.window,
    name : 'predictive_cue', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  non_predictive_cue = new visual.ImageStim({
    win : psychoJS.window,
    name : 'non_predictive_cue', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  o1_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'o1_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.16, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  o2_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'o2_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.16, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  cue_o_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  cue_o_mouse.mouseClock = new util.Clock();
  timeout_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'timeout_text',
    text: 'TIMEOUT - TOO SLOW',
    font: 'Trebuchet MS',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: undefined,
    depth: -10.0 
  });
  
  // Initialize components for Routine "cue_selection"
  cue_selectionClock = new util.Clock();
  predictive_cue_selection = new visual.ImageStim({
    win : psychoJS.window,
    name : 'predictive_cue_selection', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  non_predictive_cue_selection = new visual.ImageStim({
    win : psychoJS.window,
    name : 'non_predictive_cue_selection', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  o1_image_selection = new visual.ImageStim({
    win : psychoJS.window,
    name : 'o1_image_selection', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.16, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  o2_image_selection = new visual.ImageStim({
    win : psychoJS.window,
    name : 'o2_image_selection', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.16, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  yellow_frame = new visual.ImageStim({
    win : psychoJS.window,
    name : 'yellow_frame', units : undefined, 
    image : 'stimuli/yellow_frame.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.16, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: '',
    font: 'Trebuchet MS',
    units: undefined, 
    pos: [0, (- 0.05)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  predictive_cue_feedback = new visual.ImageStim({
    win : psychoJS.window,
    name : 'predictive_cue_feedback', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  non_predictive_cue_feedback = new visual.ImageStim({
    win : psychoJS.window,
    name : 'non_predictive_cue_feedback', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  o1_image_feedback = new visual.ImageStim({
    win : psychoJS.window,
    name : 'o1_image_feedback', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.16, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  o2_image_feedback = new visual.ImageStim({
    win : psychoJS.window,
    name : 'o2_image_feedback', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.16, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "test2_vsubtle_inst"
  test2_vsubtle_instClock = new util.Clock();
  cont_test2_vsubtle = new visual.TextBox({
    win: psychoJS.window,
    name: 'cont_test2_vsubtle',
    text: 'CONTINUE',
    font: 'Trebuchet MS',
    pos: [0, (- 0.45)], letterHeight: 0.03,
    size: [0.2, 0.065],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: 'darkgrey', borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  cont_mouse_test2_vsubtle = new core.Mouse({
    win: psychoJS.window,
  });
  cont_mouse_test2_vsubtle.mouseClock = new util.Clock();
  instructions_test2_vsubtle = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructions_test2_vsubtle', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.4, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "comprehension3"
  comprehension3Clock = new util.Clock();
  comp3_resp2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'comp3_resp2',
    text: 'Click on the mutant that would result of each chemicals combination',
    font: 'Trebuchet MS',
    pos: [(- 0.71), (- 0.2)], letterHeight: 0.035,
    size: [1.5, 0.05],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center-left',
    depth: 0.0 
  });
  
  comp3_resp1 = new visual.TextBox({
    win: psychoJS.window,
    name: 'comp3_resp1',
    text: 'Select the chemical you have seen in Task 1',
    font: 'Trebuchet MS',
    pos: [(- 0.71), (- 0.26)], letterHeight: 0.035,
    size: [1.5, 0.05],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center-left',
    depth: -1.0 
  });
  
  comp3_resp3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'comp3_resp3',
    text: 'Rate how beautiful the chemicals presented are',
    font: 'Trebuchet MS',
    pos: [(- 0.71), (- 0.32)], letterHeight: 0.035,
    size: [1.5, 0.05],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center-left',
    depth: -2.0 
  });
  
  comp3_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  comp3_mouse.mouseClock = new util.Clock();
  check3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'check3', units : undefined, 
    image : 'instructions/check3.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.45, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  // Initialize components for Routine "test2_vsubtle_choice"
  test2_vsubtle_choiceClock = new util.Clock();
  blank_test2_vsubtle = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank_test2_vsubtle',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  target_test2_vsubtle = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_test2_vsubtle', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  distractor_test2_vsubtle = new visual.ImageStim({
    win : psychoJS.window,
    name : 'distractor_test2_vsubtle', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  mouse_test2_vsubtle = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_test2_vsubtle.mouseClock = new util.Clock();
  // Initialize components for Routine "test2_vsubtle_rate"
  test2_vsubtle_rateClock = new util.Clock();
  slider_text_test2_vsubtle = new visual.TextStim({
    win: psychoJS.window,
    name: 'slider_text_test2_vsubtle',
    text: 'How confident are you of your response?',
    font: 'Trebuchet MS',
    units: undefined, 
    pos: [0, (- 0.15)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  slider_test2_vsubtle = new visual.Slider({
    win: psychoJS.window, name: 'slider_test2_vsubtle',
    startValue: 5.5,
    size: [0.5, 0.025], pos: [0, (- 0.2)], ori: 0.0, units: 'height',
    labels: ["I am guessing", "I am certain"], fontSize: 0.028, ticks: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    granularity: 0.5, style: ["RATING"],
    color: new util.Color('white'), markerColor: new util.Color('Red'), lineColor: new util.Color('white'), 
    opacity: undefined, fontFamily: 'Trebuchet MS', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  slider_target_test2_vsubtle = new visual.ImageStim({
    win : psychoJS.window,
    name : 'slider_target_test2_vsubtle', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  slider_distractor_test2_vsubtle = new visual.ImageStim({
    win : psychoJS.window,
    name : 'slider_distractor_test2_vsubtle', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  continue_rate_test2_vsubtle = new visual.TextBox({
    win: psychoJS.window,
    name: 'continue_rate_test2_vsubtle',
    text: 'CONTINUE',
    font: 'Trebuchet MS',
    pos: [0, (- 0.45)], letterHeight: 0.03,
    size: [0.2, 0.065],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: 'darkgrey', borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -5.0 
  });
  
  mouse_continue_test2_vsubtle = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_continue_test2_vsubtle.mouseClock = new util.Clock();
  // Initialize components for Routine "debrief"
  debriefClock = new util.Clock();
  cont_debrief = new visual.TextBox({
    win: psychoJS.window,
    name: 'cont_debrief',
    text: 'CONTINUE',
    font: 'Trebuchet MS',
    pos: [0, (- 0.45)], letterHeight: 0.03,
    size: [0.2, 0.065],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: 'darkgrey', borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  cont_debrief_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  cont_debrief_mouse.mouseClock = new util.Clock();
  debrief_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'debrief_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.4, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "no_comprehension"
  no_comprehensionClock = new util.Clock();
  no_compr_textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'no_compr_textbox',
    text: "You did not pass the comprehension check.\nPlease, click the button below to leave the experiment and return the experiment clicking 'Stop Without Completing' on Prolific.",
    font: 'Trebuchet MS',
    pos: [0, 0], letterHeight: 0.03,
    size: [0.65, 0.5],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  exit_box_no_compr = new visual.TextBox({
    win: psychoJS.window,
    name: 'exit_box_no_compr',
    text: 'EXIT',
    font: 'Trebuchet MS',
    pos: [0, (- 0.4)], letterHeight: 0.03,
    size: [0.2, 0.065],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: 'darkgrey', borderColor: 'white',
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  mouse_exit_no_compr = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_exit_no_compr.mouseClock = new util.Clock();
  // Initialize components for Routine "no_consent_trial"
  no_consent_trialClock = new util.Clock();
  no_consent_textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'no_consent_textbox',
    text: 'Thank you for considering our study. You did not consent to participate.',
    font: 'Trebuchet MS',
    pos: [0, 0], letterHeight: 0.03,
    size: [0.65, 0.5],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  exit_box = new visual.TextBox({
    win: psychoJS.window,
    name: 'exit_box',
    text: 'EXIT',
    font: 'Trebuchet MS',
    pos: [0, (- 0.4)], letterHeight: 0.03,
    size: [0.2, 0.065],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: 'darkgrey', borderColor: 'white',
    languageStyle: 'LTR',
    bold: true, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  mouse_exit = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_exit.mouseClock = new util.Clock();
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var counterbalanceComponents;
function counterbalanceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'counterbalance' ---
    t = 0;
    counterbalanceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    counterbalanceComponents = [];
    
    for (const thisComponent of counterbalanceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function counterbalanceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'counterbalance' ---
    // get current time
    t = counterbalanceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of counterbalanceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function counterbalanceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'counterbalance' ---
    for (const thisComponent of counterbalanceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "counterbalance" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var information_loop;
function information_loopLoopBegin(information_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    information_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'info.xlsx',
      seed: undefined, name: 'information_loop'
    });
    psychoJS.experiment.addLoop(information_loop); // add the loop to the experiment
    currentLoop = information_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisInformation_loop of information_loop) {
      snapshot = information_loop.getSnapshot();
      information_loopLoopScheduler.add(importConditions(snapshot));
      information_loopLoopScheduler.add(informationRoutineBegin(snapshot));
      information_loopLoopScheduler.add(informationRoutineEachFrame());
      information_loopLoopScheduler.add(informationRoutineEnd(snapshot));
      information_loopLoopScheduler.add(information_loopLoopEndIteration(information_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function information_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(information_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function information_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var consent_loop;
function consent_loopLoopBegin(consent_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    consent_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: consent, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'consent_loop'
    });
    psychoJS.experiment.addLoop(consent_loop); // add the loop to the experiment
    currentLoop = consent_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisConsent_loop of consent_loop) {
      snapshot = consent_loop.getSnapshot();
      consent_loopLoopScheduler.add(importConditions(snapshot));
      const task1_instrLoopScheduler = new Scheduler(psychoJS);
      consent_loopLoopScheduler.add(task1_instrLoopBegin(task1_instrLoopScheduler, snapshot));
      consent_loopLoopScheduler.add(task1_instrLoopScheduler);
      consent_loopLoopScheduler.add(task1_instrLoopEnd);
      consent_loopLoopScheduler.add(comprehension1RoutineBegin(snapshot));
      consent_loopLoopScheduler.add(comprehension1RoutineEachFrame());
      consent_loopLoopScheduler.add(comprehension1RoutineEnd(snapshot));
      const comp1_loopLoopScheduler = new Scheduler(psychoJS);
      consent_loopLoopScheduler.add(comp1_loopLoopBegin(comp1_loopLoopScheduler, snapshot));
      consent_loopLoopScheduler.add(comp1_loopLoopScheduler);
      consent_loopLoopScheduler.add(comp1_loopLoopEnd);
      const compr1_completedLoopScheduler = new Scheduler(psychoJS);
      consent_loopLoopScheduler.add(compr1_completedLoopBegin(compr1_completedLoopScheduler, snapshot));
      consent_loopLoopScheduler.add(compr1_completedLoopScheduler);
      consent_loopLoopScheduler.add(compr1_completedLoopEnd);
      const no_compr_loopLoopScheduler = new Scheduler(psychoJS);
      consent_loopLoopScheduler.add(no_compr_loopLoopBegin(no_compr_loopLoopScheduler, snapshot));
      consent_loopLoopScheduler.add(no_compr_loopLoopScheduler);
      consent_loopLoopScheduler.add(no_compr_loopLoopEnd);
      consent_loopLoopScheduler.add(consent_loopLoopEndIteration(consent_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var task1_instr;
function task1_instrLoopBegin(task1_instrLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    task1_instr = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'task1_instructions.xlsx',
      seed: undefined, name: 'task1_instr'
    });
    psychoJS.experiment.addLoop(task1_instr); // add the loop to the experiment
    currentLoop = task1_instr;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTask1_instr of task1_instr) {
      snapshot = task1_instr.getSnapshot();
      task1_instrLoopScheduler.add(importConditions(snapshot));
      task1_instrLoopScheduler.add(instructions_1RoutineBegin(snapshot));
      task1_instrLoopScheduler.add(instructions_1RoutineEachFrame());
      task1_instrLoopScheduler.add(instructions_1RoutineEnd(snapshot));
      task1_instrLoopScheduler.add(task1_instrLoopEndIteration(task1_instrLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function task1_instrLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(task1_instr);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function task1_instrLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var comp1_loop;
function comp1_loopLoopBegin(comp1_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    comp1_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: try_again, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'comp1_loop'
    });
    psychoJS.experiment.addLoop(comp1_loop); // add the loop to the experiment
    currentLoop = comp1_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisComp1_loop of comp1_loop) {
      snapshot = comp1_loop.getSnapshot();
      comp1_loopLoopScheduler.add(importConditions(snapshot));
      const task1_instr_againLoopScheduler = new Scheduler(psychoJS);
      comp1_loopLoopScheduler.add(task1_instr_againLoopBegin(task1_instr_againLoopScheduler, snapshot));
      comp1_loopLoopScheduler.add(task1_instr_againLoopScheduler);
      comp1_loopLoopScheduler.add(task1_instr_againLoopEnd);
      comp1_loopLoopScheduler.add(comprehension1_2RoutineBegin(snapshot));
      comp1_loopLoopScheduler.add(comprehension1_2RoutineEachFrame());
      comp1_loopLoopScheduler.add(comprehension1_2RoutineEnd(snapshot));
      comp1_loopLoopScheduler.add(comp1_loopLoopEndIteration(comp1_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var task1_instr_again;
function task1_instr_againLoopBegin(task1_instr_againLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    task1_instr_again = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'task1_instructions.xlsx',
      seed: undefined, name: 'task1_instr_again'
    });
    psychoJS.experiment.addLoop(task1_instr_again); // add the loop to the experiment
    currentLoop = task1_instr_again;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTask1_instr_again of task1_instr_again) {
      snapshot = task1_instr_again.getSnapshot();
      task1_instr_againLoopScheduler.add(importConditions(snapshot));
      task1_instr_againLoopScheduler.add(instructions_1RoutineBegin(snapshot));
      task1_instr_againLoopScheduler.add(instructions_1RoutineEachFrame());
      task1_instr_againLoopScheduler.add(instructions_1RoutineEnd(snapshot));
      task1_instr_againLoopScheduler.add(task1_instr_againLoopEndIteration(task1_instr_againLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function task1_instr_againLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(task1_instr_again);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function task1_instr_againLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function comp1_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(comp1_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function comp1_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var compr1_completed;
function compr1_completedLoopBegin(compr1_completedLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    compr1_completed = new TrialHandler({
      psychoJS: psychoJS,
      nReps: compr1_continue, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'compr1_completed'
    });
    psychoJS.experiment.addLoop(compr1_completed); // add the loop to the experiment
    currentLoop = compr1_completed;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCompr1_completed of compr1_completed) {
      snapshot = compr1_completed.getSnapshot();
      compr1_completedLoopScheduler.add(importConditions(snapshot));
      const stage1_trialsLoopScheduler = new Scheduler(psychoJS);
      compr1_completedLoopScheduler.add(stage1_trialsLoopBegin(stage1_trialsLoopScheduler, snapshot));
      compr1_completedLoopScheduler.add(stage1_trialsLoopScheduler);
      compr1_completedLoopScheduler.add(stage1_trialsLoopEnd);
      const stage2_trialsLoopScheduler = new Scheduler(psychoJS);
      compr1_completedLoopScheduler.add(stage2_trialsLoopBegin(stage2_trialsLoopScheduler, snapshot));
      compr1_completedLoopScheduler.add(stage2_trialsLoopScheduler);
      compr1_completedLoopScheduler.add(stage2_trialsLoopEnd);
      const vsubtle_loopLoopScheduler = new Scheduler(psychoJS);
      compr1_completedLoopScheduler.add(vsubtle_loopLoopBegin(vsubtle_loopLoopScheduler, snapshot));
      compr1_completedLoopScheduler.add(vsubtle_loopLoopScheduler);
      compr1_completedLoopScheduler.add(vsubtle_loopLoopEnd);
      const debrief_loopLoopScheduler = new Scheduler(psychoJS);
      compr1_completedLoopScheduler.add(debrief_loopLoopBegin(debrief_loopLoopScheduler, snapshot));
      compr1_completedLoopScheduler.add(debrief_loopLoopScheduler);
      compr1_completedLoopScheduler.add(debrief_loopLoopEnd);
      compr1_completedLoopScheduler.add(compr1_completedLoopEndIteration(compr1_completedLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var stage1_trials;
function stage1_trialsLoopBegin(stage1_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    stage1_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 6, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stage1_certain.xlsx',
      seed: undefined, name: 'stage1_trials'
    });
    psychoJS.experiment.addLoop(stage1_trials); // add the loop to the experiment
    currentLoop = stage1_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisStage1_trial of stage1_trials) {
      snapshot = stage1_trials.getSnapshot();
      stage1_trialsLoopScheduler.add(importConditions(snapshot));
      stage1_trialsLoopScheduler.add(cue_o__trialRoutineBegin(snapshot));
      stage1_trialsLoopScheduler.add(cue_o__trialRoutineEachFrame());
      stage1_trialsLoopScheduler.add(cue_o__trialRoutineEnd(snapshot));
      const feedback_loopLoopScheduler = new Scheduler(psychoJS);
      stage1_trialsLoopScheduler.add(feedback_loopLoopBegin(feedback_loopLoopScheduler, snapshot));
      stage1_trialsLoopScheduler.add(feedback_loopLoopScheduler);
      stage1_trialsLoopScheduler.add(feedback_loopLoopEnd);
      stage1_trialsLoopScheduler.add(stage1_trialsLoopEndIteration(stage1_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var feedback_loop;
function feedback_loopLoopBegin(feedback_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    feedback_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: feedback_reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'feedback_loop'
    });
    psychoJS.experiment.addLoop(feedback_loop); // add the loop to the experiment
    currentLoop = feedback_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisFeedback_loop of feedback_loop) {
      snapshot = feedback_loop.getSnapshot();
      feedback_loopLoopScheduler.add(importConditions(snapshot));
      feedback_loopLoopScheduler.add(cue_selectionRoutineBegin(snapshot));
      feedback_loopLoopScheduler.add(cue_selectionRoutineEachFrame());
      feedback_loopLoopScheduler.add(cue_selectionRoutineEnd(snapshot));
      feedback_loopLoopScheduler.add(feedbackRoutineBegin(snapshot));
      feedback_loopLoopScheduler.add(feedbackRoutineEachFrame());
      feedback_loopLoopScheduler.add(feedbackRoutineEnd(snapshot));
      feedback_loopLoopScheduler.add(feedback_loopLoopEndIteration(feedback_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function feedback_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(feedback_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function feedback_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function stage1_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(stage1_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function stage1_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var stage2_trials;
function stage2_trialsLoopBegin(stage2_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    stage2_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: stage2Reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: stage2File,
      seed: undefined, name: 'stage2_trials'
    });
    psychoJS.experiment.addLoop(stage2_trials); // add the loop to the experiment
    currentLoop = stage2_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisStage2_trial of stage2_trials) {
      snapshot = stage2_trials.getSnapshot();
      stage2_trialsLoopScheduler.add(importConditions(snapshot));
      stage2_trialsLoopScheduler.add(cue_o__trialRoutineBegin(snapshot));
      stage2_trialsLoopScheduler.add(cue_o__trialRoutineEachFrame());
      stage2_trialsLoopScheduler.add(cue_o__trialRoutineEnd(snapshot));
      const stage2_feedback_loopLoopScheduler = new Scheduler(psychoJS);
      stage2_trialsLoopScheduler.add(stage2_feedback_loopLoopBegin(stage2_feedback_loopLoopScheduler, snapshot));
      stage2_trialsLoopScheduler.add(stage2_feedback_loopLoopScheduler);
      stage2_trialsLoopScheduler.add(stage2_feedback_loopLoopEnd);
      stage2_trialsLoopScheduler.add(stage2_trialsLoopEndIteration(stage2_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var stage2_feedback_loop;
function stage2_feedback_loopLoopBegin(stage2_feedback_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    stage2_feedback_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: feedback_reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'stage2_feedback_loop'
    });
    psychoJS.experiment.addLoop(stage2_feedback_loop); // add the loop to the experiment
    currentLoop = stage2_feedback_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisStage2_feedback_loop of stage2_feedback_loop) {
      snapshot = stage2_feedback_loop.getSnapshot();
      stage2_feedback_loopLoopScheduler.add(importConditions(snapshot));
      stage2_feedback_loopLoopScheduler.add(cue_selectionRoutineBegin(snapshot));
      stage2_feedback_loopLoopScheduler.add(cue_selectionRoutineEachFrame());
      stage2_feedback_loopLoopScheduler.add(cue_selectionRoutineEnd(snapshot));
      stage2_feedback_loopLoopScheduler.add(feedbackRoutineBegin(snapshot));
      stage2_feedback_loopLoopScheduler.add(feedbackRoutineEachFrame());
      stage2_feedback_loopLoopScheduler.add(feedbackRoutineEnd(snapshot));
      stage2_feedback_loopLoopScheduler.add(stage2_feedback_loopLoopEndIteration(stage2_feedback_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function stage2_feedback_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(stage2_feedback_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function stage2_feedback_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function stage2_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(stage2_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function stage2_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var vsubtle_loop;
function vsubtle_loopLoopBegin(vsubtle_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    vsubtle_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'vsubtle_loop'
    });
    psychoJS.experiment.addLoop(vsubtle_loop); // add the loop to the experiment
    currentLoop = vsubtle_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisVsubtle_loop of vsubtle_loop) {
      snapshot = vsubtle_loop.getSnapshot();
      vsubtle_loopLoopScheduler.add(importConditions(snapshot));
      const task3_instr_vsubtleLoopScheduler = new Scheduler(psychoJS);
      vsubtle_loopLoopScheduler.add(task3_instr_vsubtleLoopBegin(task3_instr_vsubtleLoopScheduler, snapshot));
      vsubtle_loopLoopScheduler.add(task3_instr_vsubtleLoopScheduler);
      vsubtle_loopLoopScheduler.add(task3_instr_vsubtleLoopEnd);
      vsubtle_loopLoopScheduler.add(comprehension3RoutineBegin(snapshot));
      vsubtle_loopLoopScheduler.add(comprehension3RoutineEachFrame());
      vsubtle_loopLoopScheduler.add(comprehension3RoutineEnd(snapshot));
      const test2_vsubtle_trialsLoopScheduler = new Scheduler(psychoJS);
      vsubtle_loopLoopScheduler.add(test2_vsubtle_trialsLoopBegin(test2_vsubtle_trialsLoopScheduler, snapshot));
      vsubtle_loopLoopScheduler.add(test2_vsubtle_trialsLoopScheduler);
      vsubtle_loopLoopScheduler.add(test2_vsubtle_trialsLoopEnd);
      vsubtle_loopLoopScheduler.add(vsubtle_loopLoopEndIteration(vsubtle_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var task3_instr_vsubtle;
function task3_instr_vsubtleLoopBegin(task3_instr_vsubtleLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    task3_instr_vsubtle = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'task3_instructions.xlsx',
      seed: undefined, name: 'task3_instr_vsubtle'
    });
    psychoJS.experiment.addLoop(task3_instr_vsubtle); // add the loop to the experiment
    currentLoop = task3_instr_vsubtle;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTask3_instr_vsubtle of task3_instr_vsubtle) {
      snapshot = task3_instr_vsubtle.getSnapshot();
      task3_instr_vsubtleLoopScheduler.add(importConditions(snapshot));
      task3_instr_vsubtleLoopScheduler.add(test2_vsubtle_instRoutineBegin(snapshot));
      task3_instr_vsubtleLoopScheduler.add(test2_vsubtle_instRoutineEachFrame());
      task3_instr_vsubtleLoopScheduler.add(test2_vsubtle_instRoutineEnd(snapshot));
      task3_instr_vsubtleLoopScheduler.add(task3_instr_vsubtleLoopEndIteration(task3_instr_vsubtleLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function task3_instr_vsubtleLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(task3_instr_vsubtle);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function task3_instr_vsubtleLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var test2_vsubtle_trials;
function test2_vsubtle_trialsLoopBegin(test2_vsubtle_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    test2_vsubtle_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'test2.xlsx',
      seed: undefined, name: 'test2_vsubtle_trials'
    });
    psychoJS.experiment.addLoop(test2_vsubtle_trials); // add the loop to the experiment
    currentLoop = test2_vsubtle_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTest2_vsubtle_trial of test2_vsubtle_trials) {
      snapshot = test2_vsubtle_trials.getSnapshot();
      test2_vsubtle_trialsLoopScheduler.add(importConditions(snapshot));
      test2_vsubtle_trialsLoopScheduler.add(test2_vsubtle_choiceRoutineBegin(snapshot));
      test2_vsubtle_trialsLoopScheduler.add(test2_vsubtle_choiceRoutineEachFrame());
      test2_vsubtle_trialsLoopScheduler.add(test2_vsubtle_choiceRoutineEnd(snapshot));
      test2_vsubtle_trialsLoopScheduler.add(test2_vsubtle_rateRoutineBegin(snapshot));
      test2_vsubtle_trialsLoopScheduler.add(test2_vsubtle_rateRoutineEachFrame());
      test2_vsubtle_trialsLoopScheduler.add(test2_vsubtle_rateRoutineEnd(snapshot));
      test2_vsubtle_trialsLoopScheduler.add(test2_vsubtle_trialsLoopEndIteration(test2_vsubtle_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function test2_vsubtle_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(test2_vsubtle_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function test2_vsubtle_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function vsubtle_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(vsubtle_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function vsubtle_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var debrief_loop;
function debrief_loopLoopBegin(debrief_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    debrief_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'debrief.xlsx',
      seed: undefined, name: 'debrief_loop'
    });
    psychoJS.experiment.addLoop(debrief_loop); // add the loop to the experiment
    currentLoop = debrief_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDebrief_loop of debrief_loop) {
      snapshot = debrief_loop.getSnapshot();
      debrief_loopLoopScheduler.add(importConditions(snapshot));
      debrief_loopLoopScheduler.add(debriefRoutineBegin(snapshot));
      debrief_loopLoopScheduler.add(debriefRoutineEachFrame());
      debrief_loopLoopScheduler.add(debriefRoutineEnd(snapshot));
      debrief_loopLoopScheduler.add(debrief_loopLoopEndIteration(debrief_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function debrief_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(debrief_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function debrief_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function compr1_completedLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(compr1_completed);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function compr1_completedLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var no_compr_loop;
function no_compr_loopLoopBegin(no_compr_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    no_compr_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: no_compr, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'no_compr_loop'
    });
    psychoJS.experiment.addLoop(no_compr_loop); // add the loop to the experiment
    currentLoop = no_compr_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisNo_compr_loop of no_compr_loop) {
      snapshot = no_compr_loop.getSnapshot();
      no_compr_loopLoopScheduler.add(importConditions(snapshot));
      no_compr_loopLoopScheduler.add(no_comprehensionRoutineBegin(snapshot));
      no_compr_loopLoopScheduler.add(no_comprehensionRoutineEachFrame());
      no_compr_loopLoopScheduler.add(no_comprehensionRoutineEnd(snapshot));
      no_compr_loopLoopScheduler.add(no_compr_loopLoopEndIteration(no_compr_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function no_compr_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(no_compr_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function no_compr_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function consent_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(consent_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function consent_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var no_consent_loop;
function no_consent_loopLoopBegin(no_consent_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    no_consent_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: no_consent, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'no_consent_loop'
    });
    psychoJS.experiment.addLoop(no_consent_loop); // add the loop to the experiment
    currentLoop = no_consent_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisNo_consent_loop of no_consent_loop) {
      snapshot = no_consent_loop.getSnapshot();
      no_consent_loopLoopScheduler.add(importConditions(snapshot));
      no_consent_loopLoopScheduler.add(no_consent_trialRoutineBegin(snapshot));
      no_consent_loopLoopScheduler.add(no_consent_trialRoutineEachFrame());
      no_consent_loopLoopScheduler.add(no_consent_trialRoutineEnd(snapshot));
      no_consent_loopLoopScheduler.add(no_consent_loopLoopEndIteration(no_consent_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function no_consent_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(no_consent_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function no_consent_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var gotValidClick;
var informationComponents;
function informationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'information' ---
    t = 0;
    informationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_info
    mouse_info.clicked_name = [];
    gotValidClick = false; // until a click is received
    image_info.setImage(information);
    // keep track of which components have finished
    informationComponents = [];
    informationComponents.push(continue_info);
    informationComponents.push(mouse_info);
    informationComponents.push(image_info);
    
    for (const thisComponent of informationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
function informationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'information' ---
    // get current time
    t = informationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *continue_info* updates
    if (t >= 0.0 && continue_info.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_info.tStart = t;  // (not accounting for frame time here)
      continue_info.frameNStart = frameN;  // exact frame index
      
      continue_info.setAutoDraw(true);
    }

    // *mouse_info* updates
    if (t >= 0.0 && mouse_info.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_info.tStart = t;  // (not accounting for frame time here)
      mouse_info.frameNStart = frameN;  // exact frame index
      
      mouse_info.status = PsychoJS.Status.STARTED;
      mouse_info.mouseClock.reset();
      prevButtonState = mouse_info.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_info.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_info.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [continue_info]) {
            if (obj.contains(mouse_info)) {
              gotValidClick = true;
              mouse_info.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *image_info* updates
    if (t >= 0.0 && image_info.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_info.tStart = t;  // (not accounting for frame time here)
      image_info.frameNStart = frameN;  // exact frame index
      
      image_info.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of informationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function informationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'information' ---
    for (const thisComponent of informationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "information" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var show_consent;
var consent;
var consentComponents;
function consentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'consent' ---
    t = 0;
    consentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    slider_1.reset()
    slider_2.reset()
    slider_3.reset()
    slider_4.reset()
    slider_5.reset()
    slider_6.reset()
    // Run 'Begin Routine' code from show_consent_code
    show_consent = false;
    
    // setup some python lists for storing info about the mouse_consent
    mouse_consent.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from consent_code
    consent = 0;
    
    // keep track of which components have finished
    consentComponents = [];
    consentComponents.push(c1);
    consentComponents.push(c2);
    consentComponents.push(c3);
    consentComponents.push(c4);
    consentComponents.push(c5);
    consentComponents.push(c6);
    consentComponents.push(slider_1);
    consentComponents.push(slider_2);
    consentComponents.push(slider_3);
    consentComponents.push(slider_4);
    consentComponents.push(slider_5);
    consentComponents.push(slider_6);
    consentComponents.push(mouse_consent);
    consentComponents.push(consent_box);
    
    for (const thisComponent of consentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var s1;
var s2;
var s3;
var s4;
var s5;
var s6;
function consentRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'consent' ---
    // get current time
    t = consentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *c1* updates
    if (t >= 0.0 && c1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      c1.tStart = t;  // (not accounting for frame time here)
      c1.frameNStart = frameN;  // exact frame index
      
      c1.setAutoDraw(true);
    }

    
    // *c2* updates
    if (t >= 0.0 && c2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      c2.tStart = t;  // (not accounting for frame time here)
      c2.frameNStart = frameN;  // exact frame index
      
      c2.setAutoDraw(true);
    }

    
    // *c3* updates
    if (t >= 0.0 && c3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      c3.tStart = t;  // (not accounting for frame time here)
      c3.frameNStart = frameN;  // exact frame index
      
      c3.setAutoDraw(true);
    }

    
    // *c4* updates
    if (t >= 0.0 && c4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      c4.tStart = t;  // (not accounting for frame time here)
      c4.frameNStart = frameN;  // exact frame index
      
      c4.setAutoDraw(true);
    }

    
    // *c5* updates
    if (t >= 0.0 && c5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      c5.tStart = t;  // (not accounting for frame time here)
      c5.frameNStart = frameN;  // exact frame index
      
      c5.setAutoDraw(true);
    }

    
    // *c6* updates
    if (t >= 0.0 && c6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      c6.tStart = t;  // (not accounting for frame time here)
      c6.frameNStart = frameN;  // exact frame index
      
      c6.setAutoDraw(true);
    }

    
    // *slider_1* updates
    if (t >= 0 && slider_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_1.tStart = t;  // (not accounting for frame time here)
      slider_1.frameNStart = frameN;  // exact frame index
      
      slider_1.setAutoDraw(true);
    }

    
    // *slider_2* updates
    if (t >= 0 && slider_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_2.tStart = t;  // (not accounting for frame time here)
      slider_2.frameNStart = frameN;  // exact frame index
      
      slider_2.setAutoDraw(true);
    }

    
    // *slider_3* updates
    if (t >= 0 && slider_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_3.tStart = t;  // (not accounting for frame time here)
      slider_3.frameNStart = frameN;  // exact frame index
      
      slider_3.setAutoDraw(true);
    }

    
    // *slider_4* updates
    if (t >= 0 && slider_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_4.tStart = t;  // (not accounting for frame time here)
      slider_4.frameNStart = frameN;  // exact frame index
      
      slider_4.setAutoDraw(true);
    }

    
    // *slider_5* updates
    if (t >= 0 && slider_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_5.tStart = t;  // (not accounting for frame time here)
      slider_5.frameNStart = frameN;  // exact frame index
      
      slider_5.setAutoDraw(true);
    }

    
    // *slider_6* updates
    if (t >= 0 && slider_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_6.tStart = t;  // (not accounting for frame time here)
      slider_6.frameNStart = frameN;  // exact frame index
      
      slider_6.setAutoDraw(true);
    }

    // Run 'Each Frame' code from show_consent_code
    s1 = slider_1.getRating();
    s2 = slider_2.getRating();
    s3 = slider_3.getRating();
    s4 = slider_4.getRating();
    s5 = slider_5.getRating();
    s6 = slider_6.getRating();
    if (s1) {
        if (s2) {
            if (s3) {
                if (s4) {
                    if (s5) {
                        if (s6) {
                            show_consent = true;
                        }
                    }
                }
            }
        }
    }
    
    // *mouse_consent* updates
    if ((show_consent) && mouse_consent.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_consent.tStart = t;  // (not accounting for frame time here)
      mouse_consent.frameNStart = frameN;  // exact frame index
      
      mouse_consent.status = PsychoJS.Status.STARTED;
      mouse_consent.mouseClock.reset();
      prevButtonState = mouse_consent.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_consent.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_consent.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [consent_box]) {
            if (obj.contains(mouse_consent)) {
              gotValidClick = true;
              mouse_consent.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *consent_box* updates
    if ((show_consent) && consent_box.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consent_box.tStart = t;  // (not accounting for frame time here)
      consent_box.frameNStart = frameN;  // exact frame index
      
      consent_box.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of consentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var res1;
var res2;
var res3;
var res4;
var res5;
var res6;
var no_consent;
function consentRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'consent' ---
    for (const thisComponent of consentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('slider_1.response', slider_1.getRating());
    psychoJS.experiment.addData('slider_2.response', slider_2.getRating());
    psychoJS.experiment.addData('slider_3.response', slider_3.getRating());
    psychoJS.experiment.addData('slider_4.response', slider_4.getRating());
    psychoJS.experiment.addData('slider_5.response', slider_5.getRating());
    psychoJS.experiment.addData('slider_6.response', slider_6.getRating());
    // store data for psychoJS.experiment (ExperimentHandler)
    // Run 'End Routine' code from consent_code
    res1 = slider_1.getRating();
    res2 = slider_2.getRating();
    res3 = slider_3.getRating();
    res4 = slider_4.getRating();
    res5 = slider_5.getRating();
    res6 = slider_6.getRating();
    if ((res1 === 1)) {
        if ((res2 === 1)) {
            if ((res3 === 1)) {
                if ((res4 === 1)) {
                    if ((res5 === 1)) {
                        if ((res6 === 1)) {
                            consent = 1;
                            no_consent = 0;
                        } else {
                            consent = 0;
                            no_consent = 1;
                        }
                    } else {
                        consent = 0;
                        no_consent = 1;
                    }
                } else {
                    consent = 0;
                    no_consent = 1;
                }
            } else {
                consent = 0;
                no_consent = 1;
            }
        } else {
            consent = 0;
            no_consent = 1;
        }
    } else {
        consent = 0;
        no_consent = 1;
    }
    
    // the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instructions_1Components;
function instructions_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_1' ---
    t = 0;
    instructions_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the cont_train_instr_mouse
    cont_train_instr_mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    train_instructions.setImage(task1);
    // keep track of which components have finished
    instructions_1Components = [];
    instructions_1Components.push(cont_train_instr);
    instructions_1Components.push(cont_train_instr_mouse);
    instructions_1Components.push(train_instructions);
    
    for (const thisComponent of instructions_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructions_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_1' ---
    // get current time
    t = instructions_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cont_train_instr* updates
    if (t >= 0.0 && cont_train_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont_train_instr.tStart = t;  // (not accounting for frame time here)
      cont_train_instr.frameNStart = frameN;  // exact frame index
      
      cont_train_instr.setAutoDraw(true);
    }

    // *cont_train_instr_mouse* updates
    if (t >= 0.0 && cont_train_instr_mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont_train_instr_mouse.tStart = t;  // (not accounting for frame time here)
      cont_train_instr_mouse.frameNStart = frameN;  // exact frame index
      
      cont_train_instr_mouse.status = PsychoJS.Status.STARTED;
      cont_train_instr_mouse.mouseClock.reset();
      prevButtonState = cont_train_instr_mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (cont_train_instr_mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = cont_train_instr_mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [cont_train_instr]) {
            if (obj.contains(cont_train_instr_mouse)) {
              gotValidClick = true;
              cont_train_instr_mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *train_instructions* updates
    if (t >= 0.0 && train_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train_instructions.tStart = t;  // (not accounting for frame time here)
      train_instructions.frameNStart = frameN;  // exact frame index
      
      train_instructions.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructions_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_1' ---
    for (const thisComponent of instructions_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "instructions_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var comprehension1Components;
function comprehension1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'comprehension1' ---
    t = 0;
    comprehension1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the comp1_mouse
    // current position of the mouse:
    comp1_mouse.x = [];
    comp1_mouse.y = [];
    comp1_mouse.leftButton = [];
    comp1_mouse.midButton = [];
    comp1_mouse.rightButton = [];
    comp1_mouse.time = [];
    comp1_mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    comp1_mouse.mouseClock.reset();
    // keep track of which components have finished
    comprehension1Components = [];
    comprehension1Components.push(comp1_resp1);
    comprehension1Components.push(comp1_resp2);
    comprehension1Components.push(comp1_resp3);
    comprehension1Components.push(comp1_mouse);
    comprehension1Components.push(check1);
    
    for (const thisComponent of comprehension1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var _mouseXYs;
function comprehension1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'comprehension1' ---
    // get current time
    t = comprehension1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *comp1_resp1* updates
    if (t >= 0.0 && comp1_resp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comp1_resp1.tStart = t;  // (not accounting for frame time here)
      comp1_resp1.frameNStart = frameN;  // exact frame index
      
      comp1_resp1.setAutoDraw(true);
    }

    
    // *comp1_resp2* updates
    if (t >= 0.0 && comp1_resp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comp1_resp2.tStart = t;  // (not accounting for frame time here)
      comp1_resp2.frameNStart = frameN;  // exact frame index
      
      comp1_resp2.setAutoDraw(true);
    }

    
    // *comp1_resp3* updates
    if (t >= 0.0 && comp1_resp3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comp1_resp3.tStart = t;  // (not accounting for frame time here)
      comp1_resp3.frameNStart = frameN;  // exact frame index
      
      comp1_resp3.setAutoDraw(true);
    }

    // *comp1_mouse* updates
    if (t >= 0.0 && comp1_mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comp1_mouse.tStart = t;  // (not accounting for frame time here)
      comp1_mouse.frameNStart = frameN;  // exact frame index
      
      comp1_mouse.status = PsychoJS.Status.STARTED;
      prevButtonState = comp1_mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (comp1_mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = comp1_mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [comp1_resp1, comp1_resp2, comp1_resp3]) {
            if (obj.contains(comp1_mouse)) {
              gotValidClick = true;
              comp1_mouse.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = comp1_mouse.getPos();
          comp1_mouse.x.push(_mouseXYs[0]);
          comp1_mouse.y.push(_mouseXYs[1]);
          comp1_mouse.leftButton.push(_mouseButtons[0]);
          comp1_mouse.midButton.push(_mouseButtons[1]);
          comp1_mouse.rightButton.push(_mouseButtons[2]);
          comp1_mouse.time.push(comp1_mouse.mouseClock.getTime());
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *check1* updates
    if (t >= 0.0 && check1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      check1.tStart = t;  // (not accounting for frame time here)
      check1.frameNStart = frameN;  // exact frame index
      
      check1.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of comprehension1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var try_again;
var compr1_continue;
var no_compr;
function comprehension1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'comprehension1' ---
    for (const thisComponent of comprehension1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from comprehension_code
    if ((comp1_mouse.clicked_name[0] === "comp1_resp1")) {
        try_again = 0;
        compr1_continue = 1;
        no_compr = 0;
    } else {
        try_again = 1;
    }
    
    // store data for psychoJS.experiment (ExperimentHandler)
    if (comp1_mouse.x) {  psychoJS.experiment.addData('comp1_mouse.x', comp1_mouse.x[0])};
    if (comp1_mouse.y) {  psychoJS.experiment.addData('comp1_mouse.y', comp1_mouse.y[0])};
    if (comp1_mouse.leftButton) {  psychoJS.experiment.addData('comp1_mouse.leftButton', comp1_mouse.leftButton[0])};
    if (comp1_mouse.midButton) {  psychoJS.experiment.addData('comp1_mouse.midButton', comp1_mouse.midButton[0])};
    if (comp1_mouse.rightButton) {  psychoJS.experiment.addData('comp1_mouse.rightButton', comp1_mouse.rightButton[0])};
    if (comp1_mouse.time) {  psychoJS.experiment.addData('comp1_mouse.time', comp1_mouse.time[0])};
    if (comp1_mouse.clicked_name) {  psychoJS.experiment.addData('comp1_mouse.clicked_name', comp1_mouse.clicked_name[0])};
    
    // the Routine "comprehension1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var comprehension1_2Components;
function comprehension1_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'comprehension1_2' ---
    t = 0;
    comprehension1_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the comp1_mouse_2
    // current position of the mouse:
    comp1_mouse_2.x = [];
    comp1_mouse_2.y = [];
    comp1_mouse_2.leftButton = [];
    comp1_mouse_2.midButton = [];
    comp1_mouse_2.rightButton = [];
    comp1_mouse_2.time = [];
    comp1_mouse_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    comp1_mouse_2.mouseClock.reset();
    // keep track of which components have finished
    comprehension1_2Components = [];
    comprehension1_2Components.push(comp1_resp1_2);
    comprehension1_2Components.push(comp1_resp2_2);
    comprehension1_2Components.push(comp1_resp3_2);
    comprehension1_2Components.push(comp1_mouse_2);
    comprehension1_2Components.push(check1_2);
    
    for (const thisComponent of comprehension1_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function comprehension1_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'comprehension1_2' ---
    // get current time
    t = comprehension1_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *comp1_resp1_2* updates
    if (t >= 0.0 && comp1_resp1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comp1_resp1_2.tStart = t;  // (not accounting for frame time here)
      comp1_resp1_2.frameNStart = frameN;  // exact frame index
      
      comp1_resp1_2.setAutoDraw(true);
    }

    
    // *comp1_resp2_2* updates
    if (t >= 0.0 && comp1_resp2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comp1_resp2_2.tStart = t;  // (not accounting for frame time here)
      comp1_resp2_2.frameNStart = frameN;  // exact frame index
      
      comp1_resp2_2.setAutoDraw(true);
    }

    
    // *comp1_resp3_2* updates
    if (t >= 0.0 && comp1_resp3_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comp1_resp3_2.tStart = t;  // (not accounting for frame time here)
      comp1_resp3_2.frameNStart = frameN;  // exact frame index
      
      comp1_resp3_2.setAutoDraw(true);
    }

    // *comp1_mouse_2* updates
    if (t >= 0.0 && comp1_mouse_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comp1_mouse_2.tStart = t;  // (not accounting for frame time here)
      comp1_mouse_2.frameNStart = frameN;  // exact frame index
      
      comp1_mouse_2.status = PsychoJS.Status.STARTED;
      prevButtonState = comp1_mouse_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (comp1_mouse_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = comp1_mouse_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [comp1_resp1_2, comp1_resp2_2, comp1_resp3_2]) {
            if (obj.contains(comp1_mouse_2)) {
              gotValidClick = true;
              comp1_mouse_2.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = comp1_mouse_2.getPos();
          comp1_mouse_2.x.push(_mouseXYs[0]);
          comp1_mouse_2.y.push(_mouseXYs[1]);
          comp1_mouse_2.leftButton.push(_mouseButtons[0]);
          comp1_mouse_2.midButton.push(_mouseButtons[1]);
          comp1_mouse_2.rightButton.push(_mouseButtons[2]);
          comp1_mouse_2.time.push(comp1_mouse_2.mouseClock.getTime());
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *check1_2* updates
    if (t >= 0.0 && check1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      check1_2.tStart = t;  // (not accounting for frame time here)
      check1_2.frameNStart = frameN;  // exact frame index
      
      check1_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of comprehension1_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function comprehension1_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'comprehension1_2' ---
    for (const thisComponent of comprehension1_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from comprehension_code_2
    if ((comp1_mouse_2.clicked_name[0] === "comp1_resp1_2")) {
        compr1_continue = 1;
        no_compr = 0;
    } else {
        compr1_continue = 0;
        no_compr = 1;
    }
    
    // store data for psychoJS.experiment (ExperimentHandler)
    if (comp1_mouse_2.x) {  psychoJS.experiment.addData('comp1_mouse_2.x', comp1_mouse_2.x[0])};
    if (comp1_mouse_2.y) {  psychoJS.experiment.addData('comp1_mouse_2.y', comp1_mouse_2.y[0])};
    if (comp1_mouse_2.leftButton) {  psychoJS.experiment.addData('comp1_mouse_2.leftButton', comp1_mouse_2.leftButton[0])};
    if (comp1_mouse_2.midButton) {  psychoJS.experiment.addData('comp1_mouse_2.midButton', comp1_mouse_2.midButton[0])};
    if (comp1_mouse_2.rightButton) {  psychoJS.experiment.addData('comp1_mouse_2.rightButton', comp1_mouse_2.rightButton[0])};
    if (comp1_mouse_2.time) {  psychoJS.experiment.addData('comp1_mouse_2.time', comp1_mouse_2.time[0])};
    if (comp1_mouse_2.clicked_name) {  psychoJS.experiment.addData('comp1_mouse_2.clicked_name', comp1_mouse_2.clicked_name[0])};
    
    // the Routine "comprehension1_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var stim1;
var stim2;
var left_cue_pos;
var right_cue_pos;
var left_out_pos;
var right_out_pos;
var cue_positions;
var out_positions;
var msg;
var correct;
var cue_o__trialComponents;
function cue_o__trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'cue_o__trial' ---
    t = 0;
    cue_o__trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(11.500000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from cue_random
    if ((cue1 === 1)) {
        stim1 = reorder_cues[0];
    } else {
        if ((cue1 === 2)) {
            stim1 = reorder_cues[1];
        } else {
            if ((cue1 === 3)) {
                stim1 = reorder_cues[2];
            } else {
                if ((cue1 === 4)) {
                    stim1 = reorder_cues[3];
                }
            }
        }
    }
    if ((cue2 === 5)) {
        stim2 = reorder_cues[4];
    } else {
        if ((cue2 === 6)) {
            stim2 = reorder_cues[5];
        } else {
            if ((cue2 === 7)) {
                stim2 = reorder_cues[6];
            } else {
                if ((cue2 === 8)) {
                    stim2 = reorder_cues[7];
                }
            }
        }
    }
    
    // Run 'Begin Routine' code from position
    left_cue_pos = [(- 0.3), 0.2];
    right_cue_pos = [0.3, 0.2];
    left_out_pos = [(- 0.125), (- 0.2)];
    right_out_pos = [0.125, (- 0.2)];
    cue_positions = [left_cue_pos, right_cue_pos];
    out_positions = [left_out_pos, right_out_pos];
    util.shuffle(cue_positions);
    util.shuffle(out_positions);
    
    predictive_cue.setPos(cue_positions[0]);
    predictive_cue.setImage(stim1);
    non_predictive_cue.setPos(cue_positions[1]);
    non_predictive_cue.setImage(stim2);
    o1_image.setPos(out_positions[0]);
    o1_image.setImage('stimuli/out1.png');
    o2_image.setPos(out_positions[1]);
    o2_image.setImage('stimuli/out2.png');
    // setup some python lists for storing info about the cue_o_mouse
    // current position of the mouse:
    cue_o_mouse.x = [];
    cue_o_mouse.y = [];
    cue_o_mouse.leftButton = [];
    cue_o_mouse.midButton = [];
    cue_o_mouse.rightButton = [];
    cue_o_mouse.time = [];
    cue_o_mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from correct_click
    msg = "888";
    correct = 99;
    
    // keep track of which components have finished
    cue_o__trialComponents = [];
    cue_o__trialComponents.push(blank_training);
    cue_o__trialComponents.push(predictive_cue);
    cue_o__trialComponents.push(non_predictive_cue);
    cue_o__trialComponents.push(o1_image);
    cue_o__trialComponents.push(o2_image);
    cue_o__trialComponents.push(cue_o_mouse);
    cue_o__trialComponents.push(timeout_text);
    
    for (const thisComponent of cue_o__trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function cue_o__trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'cue_o__trial' ---
    // get current time
    t = cue_o__trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blank_training* updates
    if (t >= 0.0 && blank_training.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blank_training.tStart = t;  // (not accounting for frame time here)
      blank_training.frameNStart = frameN;  // exact frame index
      
      blank_training.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blank_training.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blank_training.setAutoDraw(false);
    }
    
    // *predictive_cue* updates
    if (t >= 0.5 && predictive_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      predictive_cue.tStart = t;  // (not accounting for frame time here)
      predictive_cue.frameNStart = frameN;  // exact frame index
      
      predictive_cue.setAutoDraw(true);
    }

    frameRemains = 0.5 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (predictive_cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      predictive_cue.setAutoDraw(false);
    }
    
    // *non_predictive_cue* updates
    if (t >= 0.5 && non_predictive_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      non_predictive_cue.tStart = t;  // (not accounting for frame time here)
      non_predictive_cue.frameNStart = frameN;  // exact frame index
      
      non_predictive_cue.setAutoDraw(true);
    }

    frameRemains = 0.5 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (non_predictive_cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      non_predictive_cue.setAutoDraw(false);
    }
    
    // *o1_image* updates
    if (t >= 0.5 && o1_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      o1_image.tStart = t;  // (not accounting for frame time here)
      o1_image.frameNStart = frameN;  // exact frame index
      
      o1_image.setAutoDraw(true);
    }

    frameRemains = 0.5 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (o1_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      o1_image.setAutoDraw(false);
    }
    
    // *o2_image* updates
    if (t >= 0.5 && o2_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      o2_image.tStart = t;  // (not accounting for frame time here)
      o2_image.frameNStart = frameN;  // exact frame index
      
      o2_image.setAutoDraw(true);
    }

    frameRemains = 0.5 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (o2_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      o2_image.setAutoDraw(false);
    }
    // *cue_o_mouse* updates
    if (t >= 0.5 && cue_o_mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cue_o_mouse.tStart = t;  // (not accounting for frame time here)
      cue_o_mouse.frameNStart = frameN;  // exact frame index
      
      cue_o_mouse.status = PsychoJS.Status.STARTED;
      cue_o_mouse.mouseClock.reset();
      prevButtonState = cue_o_mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    frameRemains = 0.5 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cue_o_mouse.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cue_o_mouse.status = PsychoJS.Status.FINISHED;
  }
    if (cue_o_mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = cue_o_mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [o1_image, o2_image]) {
            if (obj.contains(cue_o_mouse)) {
              gotValidClick = true;
              cue_o_mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { 
            _mouseXYs = cue_o_mouse.getPos();
            cue_o_mouse.x.push(_mouseXYs[0]);
            cue_o_mouse.y.push(_mouseXYs[1]);
            cue_o_mouse.leftButton.push(_mouseButtons[0]);
            cue_o_mouse.midButton.push(_mouseButtons[1]);
            cue_o_mouse.rightButton.push(_mouseButtons[2]);
            cue_o_mouse.time.push(cue_o_mouse.mouseClock.getTime());
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *timeout_text* updates
    if (t >= 10.5 && timeout_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      timeout_text.tStart = t;  // (not accounting for frame time here)
      timeout_text.frameNStart = frameN;  // exact frame index
      
      timeout_text.setAutoDraw(true);
    }

    frameRemains = 10.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (timeout_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      timeout_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of cue_o__trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var feedback_reps;
function cue_o__trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'cue_o__trial' ---
    for (const thisComponent of cue_o__trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from cue_random
    psychoJS.experiment.addData("order", order);
    
    // Run 'End Routine' code from position
    psychoJS.experiment.addData("cue_order", cue_positions);
    psychoJS.experiment.addData("out_order", out_positions);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    if (cue_o_mouse.x) {  psychoJS.experiment.addData('cue_o_mouse.x', cue_o_mouse.x[0])};
    if (cue_o_mouse.y) {  psychoJS.experiment.addData('cue_o_mouse.y', cue_o_mouse.y[0])};
    if (cue_o_mouse.leftButton) {  psychoJS.experiment.addData('cue_o_mouse.leftButton', cue_o_mouse.leftButton[0])};
    if (cue_o_mouse.midButton) {  psychoJS.experiment.addData('cue_o_mouse.midButton', cue_o_mouse.midButton[0])};
    if (cue_o_mouse.rightButton) {  psychoJS.experiment.addData('cue_o_mouse.rightButton', cue_o_mouse.rightButton[0])};
    if (cue_o_mouse.time) {  psychoJS.experiment.addData('cue_o_mouse.time', cue_o_mouse.time[0])};
    if (cue_o_mouse.clicked_name) {  psychoJS.experiment.addData('cue_o_mouse.clicked_name', cue_o_mouse.clicked_name[0])};
    
    // Run 'End Routine' code from timeout_code
    if ((cue_o_mouse.isPressedIn(o1_image) || cue_o_mouse.isPressedIn(o2_image))) {
        feedback_reps = 1;
    } else {
        feedback_reps = 0;
    }
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var yellow_frame_position;
var cue_selectionComponents;
function cue_selectionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'cue_selection' ---
    t = 0;
    cue_selectionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from clicked_outcome
    if ((cue_o_mouse.clicked_name[0] === "o1_image")) {
        yellow_frame_position = out_positions[0];
    } else {
        yellow_frame_position = out_positions[1];
    }
    if ((cue_o_mouse.clicked_name[0] === outcome)) {
        correct = 1;
    } else {
        correct = 0;
    }
    psychoJS.experiment.addData("correct_answer", correct);
    
    predictive_cue_selection.setPos(cue_positions[0]);
    predictive_cue_selection.setImage(stim1);
    non_predictive_cue_selection.setPos(cue_positions[1]);
    non_predictive_cue_selection.setImage(stim2);
    o1_image_selection.setPos(out_positions[0]);
    o1_image_selection.setImage('stimuli/out1.png');
    o2_image_selection.setPos(out_positions[1]);
    o2_image_selection.setImage('stimuli/out2.png');
    yellow_frame.setPos(yellow_frame_position);
    // keep track of which components have finished
    cue_selectionComponents = [];
    cue_selectionComponents.push(predictive_cue_selection);
    cue_selectionComponents.push(non_predictive_cue_selection);
    cue_selectionComponents.push(o1_image_selection);
    cue_selectionComponents.push(o2_image_selection);
    cue_selectionComponents.push(yellow_frame);
    
    for (const thisComponent of cue_selectionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function cue_selectionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'cue_selection' ---
    // get current time
    t = cue_selectionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *predictive_cue_selection* updates
    if (t >= 0 && predictive_cue_selection.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      predictive_cue_selection.tStart = t;  // (not accounting for frame time here)
      predictive_cue_selection.frameNStart = frameN;  // exact frame index
      
      predictive_cue_selection.setAutoDraw(true);
    }

    frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (predictive_cue_selection.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      predictive_cue_selection.setAutoDraw(false);
    }
    
    // *non_predictive_cue_selection* updates
    if (t >= 0 && non_predictive_cue_selection.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      non_predictive_cue_selection.tStart = t;  // (not accounting for frame time here)
      non_predictive_cue_selection.frameNStart = frameN;  // exact frame index
      
      non_predictive_cue_selection.setAutoDraw(true);
    }

    frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (non_predictive_cue_selection.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      non_predictive_cue_selection.setAutoDraw(false);
    }
    
    // *o1_image_selection* updates
    if (t >= 0 && o1_image_selection.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      o1_image_selection.tStart = t;  // (not accounting for frame time here)
      o1_image_selection.frameNStart = frameN;  // exact frame index
      
      o1_image_selection.setAutoDraw(true);
    }

    frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (o1_image_selection.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      o1_image_selection.setAutoDraw(false);
    }
    
    // *o2_image_selection* updates
    if (t >= 0 && o2_image_selection.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      o2_image_selection.tStart = t;  // (not accounting for frame time here)
      o2_image_selection.frameNStart = frameN;  // exact frame index
      
      o2_image_selection.setAutoDraw(true);
    }

    frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (o2_image_selection.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      o2_image_selection.setAutoDraw(false);
    }
    
    // *yellow_frame* updates
    if (t >= 0 && yellow_frame.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      yellow_frame.tStart = t;  // (not accounting for frame time here)
      yellow_frame.frameNStart = frameN;  // exact frame index
      
      yellow_frame.setAutoDraw(true);
    }

    frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (yellow_frame.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      yellow_frame.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of cue_selectionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function cue_selectionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'cue_selection' ---
    for (const thisComponent of cue_selectionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var msg_color;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from feedback_code
    if ((correct === 1)) {
        msg = "CORRECT!";
        msg_color = [(- 1.0), 1.0, (- 1.0)];
    } else {
        msg = "INCORRECT!";
        msg_color = "red";
    }
    
    feedback_text.setColor(new util.Color(msg_color));
    feedback_text.setText(msg);
    predictive_cue_feedback.setPos(cue_positions[0]);
    predictive_cue_feedback.setImage(stim1);
    non_predictive_cue_feedback.setPos(cue_positions[1]);
    non_predictive_cue_feedback.setImage(stim2);
    o1_image_feedback.setPos(out_positions[0]);
    o1_image_feedback.setImage(o1_feedback);
    o2_image_feedback.setPos(out_positions[1]);
    o2_image_feedback.setImage(o2_feedback);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(feedback_text);
    feedbackComponents.push(predictive_cue_feedback);
    feedbackComponents.push(non_predictive_cue_feedback);
    feedbackComponents.push(o1_image_feedback);
    feedbackComponents.push(o2_image_feedback);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text* updates
    if (t >= 0 && feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text.tStart = t;  // (not accounting for frame time here)
      feedback_text.frameNStart = frameN;  // exact frame index
      
      feedback_text.setAutoDraw(true);
    }

    frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text.setAutoDraw(false);
    }
    
    // *predictive_cue_feedback* updates
    if (t >= 0 && predictive_cue_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      predictive_cue_feedback.tStart = t;  // (not accounting for frame time here)
      predictive_cue_feedback.frameNStart = frameN;  // exact frame index
      
      predictive_cue_feedback.setAutoDraw(true);
    }

    frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (predictive_cue_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      predictive_cue_feedback.setAutoDraw(false);
    }
    
    // *non_predictive_cue_feedback* updates
    if (t >= 0 && non_predictive_cue_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      non_predictive_cue_feedback.tStart = t;  // (not accounting for frame time here)
      non_predictive_cue_feedback.frameNStart = frameN;  // exact frame index
      
      non_predictive_cue_feedback.setAutoDraw(true);
    }

    frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (non_predictive_cue_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      non_predictive_cue_feedback.setAutoDraw(false);
    }
    
    // *o1_image_feedback* updates
    if (t >= 0 && o1_image_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      o1_image_feedback.tStart = t;  // (not accounting for frame time here)
      o1_image_feedback.frameNStart = frameN;  // exact frame index
      
      o1_image_feedback.setAutoDraw(true);
    }

    frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (o1_image_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      o1_image_feedback.setAutoDraw(false);
    }
    
    // *o2_image_feedback* updates
    if (t >= 0 && o2_image_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      o2_image_feedback.tStart = t;  // (not accounting for frame time here)
      o2_image_feedback.frameNStart = frameN;  // exact frame index
      
      o2_image_feedback.setAutoDraw(true);
    }

    frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (o2_image_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      o2_image_feedback.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var test2_vsubtle_instComponents;
function test2_vsubtle_instRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test2_vsubtle_inst' ---
    t = 0;
    test2_vsubtle_instClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the cont_mouse_test2_vsubtle
    cont_mouse_test2_vsubtle.clicked_name = [];
    gotValidClick = false; // until a click is received
    instructions_test2_vsubtle.setImage(task3);
    // keep track of which components have finished
    test2_vsubtle_instComponents = [];
    test2_vsubtle_instComponents.push(cont_test2_vsubtle);
    test2_vsubtle_instComponents.push(cont_mouse_test2_vsubtle);
    test2_vsubtle_instComponents.push(instructions_test2_vsubtle);
    
    for (const thisComponent of test2_vsubtle_instComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function test2_vsubtle_instRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test2_vsubtle_inst' ---
    // get current time
    t = test2_vsubtle_instClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cont_test2_vsubtle* updates
    if (t >= 0.0 && cont_test2_vsubtle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont_test2_vsubtle.tStart = t;  // (not accounting for frame time here)
      cont_test2_vsubtle.frameNStart = frameN;  // exact frame index
      
      cont_test2_vsubtle.setAutoDraw(true);
    }

    // *cont_mouse_test2_vsubtle* updates
    if (t >= 0.0 && cont_mouse_test2_vsubtle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont_mouse_test2_vsubtle.tStart = t;  // (not accounting for frame time here)
      cont_mouse_test2_vsubtle.frameNStart = frameN;  // exact frame index
      
      cont_mouse_test2_vsubtle.status = PsychoJS.Status.STARTED;
      cont_mouse_test2_vsubtle.mouseClock.reset();
      prevButtonState = cont_mouse_test2_vsubtle.getPressed();  // if button is down already this ISN'T a new click
      }
    if (cont_mouse_test2_vsubtle.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = cont_mouse_test2_vsubtle.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [cont_test2_vsubtle]) {
            if (obj.contains(cont_mouse_test2_vsubtle)) {
              gotValidClick = true;
              cont_mouse_test2_vsubtle.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *instructions_test2_vsubtle* updates
    if (t >= 0.0 && instructions_test2_vsubtle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_test2_vsubtle.tStart = t;  // (not accounting for frame time here)
      instructions_test2_vsubtle.frameNStart = frameN;  // exact frame index
      
      instructions_test2_vsubtle.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test2_vsubtle_instComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test2_vsubtle_instRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test2_vsubtle_inst' ---
    for (const thisComponent of test2_vsubtle_instComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "test2_vsubtle_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var comprehension3Components;
function comprehension3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'comprehension3' ---
    t = 0;
    comprehension3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the comp3_mouse
    // current position of the mouse:
    comp3_mouse.x = [];
    comp3_mouse.y = [];
    comp3_mouse.leftButton = [];
    comp3_mouse.midButton = [];
    comp3_mouse.rightButton = [];
    comp3_mouse.time = [];
    comp3_mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    comp3_mouse.mouseClock.reset();
    // keep track of which components have finished
    comprehension3Components = [];
    comprehension3Components.push(comp3_resp2);
    comprehension3Components.push(comp3_resp1);
    comprehension3Components.push(comp3_resp3);
    comprehension3Components.push(comp3_mouse);
    comprehension3Components.push(check3);
    
    for (const thisComponent of comprehension3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function comprehension3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'comprehension3' ---
    // get current time
    t = comprehension3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *comp3_resp2* updates
    if (t >= 0.0 && comp3_resp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comp3_resp2.tStart = t;  // (not accounting for frame time here)
      comp3_resp2.frameNStart = frameN;  // exact frame index
      
      comp3_resp2.setAutoDraw(true);
    }

    
    // *comp3_resp1* updates
    if (t >= 0.0 && comp3_resp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comp3_resp1.tStart = t;  // (not accounting for frame time here)
      comp3_resp1.frameNStart = frameN;  // exact frame index
      
      comp3_resp1.setAutoDraw(true);
    }

    
    // *comp3_resp3* updates
    if (t >= 0.0 && comp3_resp3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comp3_resp3.tStart = t;  // (not accounting for frame time here)
      comp3_resp3.frameNStart = frameN;  // exact frame index
      
      comp3_resp3.setAutoDraw(true);
    }

    // *comp3_mouse* updates
    if (t >= 0.0 && comp3_mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      comp3_mouse.tStart = t;  // (not accounting for frame time here)
      comp3_mouse.frameNStart = frameN;  // exact frame index
      
      comp3_mouse.status = PsychoJS.Status.STARTED;
      prevButtonState = comp3_mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (comp3_mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = comp3_mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [comp3_resp1, comp3_resp2, comp3_resp3]) {
            if (obj.contains(comp3_mouse)) {
              gotValidClick = true;
              comp3_mouse.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = comp3_mouse.getPos();
          comp3_mouse.x.push(_mouseXYs[0]);
          comp3_mouse.y.push(_mouseXYs[1]);
          comp3_mouse.leftButton.push(_mouseButtons[0]);
          comp3_mouse.midButton.push(_mouseButtons[1]);
          comp3_mouse.rightButton.push(_mouseButtons[2]);
          comp3_mouse.time.push(comp3_mouse.mouseClock.getTime());
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *check3* updates
    if (t >= 0.0 && check3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      check3.tStart = t;  // (not accounting for frame time here)
      check3.frameNStart = frameN;  // exact frame index
      
      check3.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of comprehension3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function comprehension3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'comprehension3' ---
    for (const thisComponent of comprehension3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (comp3_mouse.x) {  psychoJS.experiment.addData('comp3_mouse.x', comp3_mouse.x[0])};
    if (comp3_mouse.y) {  psychoJS.experiment.addData('comp3_mouse.y', comp3_mouse.y[0])};
    if (comp3_mouse.leftButton) {  psychoJS.experiment.addData('comp3_mouse.leftButton', comp3_mouse.leftButton[0])};
    if (comp3_mouse.midButton) {  psychoJS.experiment.addData('comp3_mouse.midButton', comp3_mouse.midButton[0])};
    if (comp3_mouse.rightButton) {  psychoJS.experiment.addData('comp3_mouse.rightButton', comp3_mouse.rightButton[0])};
    if (comp3_mouse.time) {  psychoJS.experiment.addData('comp3_mouse.time', comp3_mouse.time[0])};
    if (comp3_mouse.clicked_name) {  psychoJS.experiment.addData('comp3_mouse.clicked_name', comp3_mouse.clicked_name[0])};
    
    // the Routine "comprehension3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var distractor;
var test2_vsubtle_choiceComponents;
function test2_vsubtle_choiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test2_vsubtle_choice' ---
    t = 0;
    test2_vsubtle_choiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from target_determination_2
    if ((target === 1)) {
        stim1 = reorder_cues[0];
    } else {
        if ((target === 2)) {
            stim1 = reorder_cues[1];
        } else {
            if ((target === 3)) {
                stim1 = reorder_cues[2];
            } else {
                if ((target === 4)) {
                    stim1 = reorder_cues[3];
                } else {
                    if ((target === 5)) {
                        stim1 = reorder_cues[4];
                    } else {
                        if ((target === 6)) {
                            stim1 = reorder_cues[5];
                        } else {
                            if ((target === 7)) {
                                stim1 = reorder_cues[6];
                            } else {
                                if ((target === 8)) {
                                    stim1 = reorder_cues[7];
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    // Run 'Begin Routine' code from distractor_presentation_test2_vsubtle
    if ((distractor_test2 === 1)) {
        distractor = reorder_vsubtle[0];
    } else {
        if ((distractor_test2 === 2)) {
            distractor = reorder_vsubtle[1];
        } else {
            if ((distractor_test2 === 3)) {
                distractor = reorder_vsubtle[2];
            } else {
                if ((distractor_test2 === 4)) {
                    distractor = reorder_vsubtle[3];
                } else {
                    if ((distractor_test2 === 5)) {
                        distractor = reorder_vsubtle[4];
                    } else {
                        if ((distractor_test2 === 6)) {
                            distractor = reorder_vsubtle[5];
                        } else {
                            if ((distractor_test2 === 7)) {
                                distractor = reorder_vsubtle[6];
                            } else {
                                if ((distractor_test2 === 8)) {
                                    distractor = reorder_vsubtle[7];
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    target_test2_vsubtle.setPos(target_position);
    target_test2_vsubtle.setImage(stim1);
    distractor_test2_vsubtle.setPos(distractor_position);
    distractor_test2_vsubtle.setImage(distractor);
    // setup some python lists for storing info about the mouse_test2_vsubtle
    // current position of the mouse:
    mouse_test2_vsubtle.x = [];
    mouse_test2_vsubtle.y = [];
    mouse_test2_vsubtle.leftButton = [];
    mouse_test2_vsubtle.midButton = [];
    mouse_test2_vsubtle.rightButton = [];
    mouse_test2_vsubtle.time = [];
    mouse_test2_vsubtle.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    test2_vsubtle_choiceComponents = [];
    test2_vsubtle_choiceComponents.push(blank_test2_vsubtle);
    test2_vsubtle_choiceComponents.push(target_test2_vsubtle);
    test2_vsubtle_choiceComponents.push(distractor_test2_vsubtle);
    test2_vsubtle_choiceComponents.push(mouse_test2_vsubtle);
    
    for (const thisComponent of test2_vsubtle_choiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function test2_vsubtle_choiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test2_vsubtle_choice' ---
    // get current time
    t = test2_vsubtle_choiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blank_test2_vsubtle* updates
    if (t >= 0.0 && blank_test2_vsubtle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blank_test2_vsubtle.tStart = t;  // (not accounting for frame time here)
      blank_test2_vsubtle.frameNStart = frameN;  // exact frame index
      
      blank_test2_vsubtle.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blank_test2_vsubtle.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blank_test2_vsubtle.setAutoDraw(false);
    }
    
    // *target_test2_vsubtle* updates
    if (t >= 0.5 && target_test2_vsubtle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_test2_vsubtle.tStart = t;  // (not accounting for frame time here)
      target_test2_vsubtle.frameNStart = frameN;  // exact frame index
      
      target_test2_vsubtle.setAutoDraw(true);
    }

    
    // *distractor_test2_vsubtle* updates
    if (t >= 0.5 && distractor_test2_vsubtle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      distractor_test2_vsubtle.tStart = t;  // (not accounting for frame time here)
      distractor_test2_vsubtle.frameNStart = frameN;  // exact frame index
      
      distractor_test2_vsubtle.setAutoDraw(true);
    }

    // *mouse_test2_vsubtle* updates
    if (t >= 0.5 && mouse_test2_vsubtle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_test2_vsubtle.tStart = t;  // (not accounting for frame time here)
      mouse_test2_vsubtle.frameNStart = frameN;  // exact frame index
      
      mouse_test2_vsubtle.status = PsychoJS.Status.STARTED;
      mouse_test2_vsubtle.mouseClock.reset();
      prevButtonState = mouse_test2_vsubtle.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_test2_vsubtle.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_test2_vsubtle.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [target_test2_vsubtle, distractor_test2_vsubtle]) {
            if (obj.contains(mouse_test2_vsubtle)) {
              gotValidClick = true;
              mouse_test2_vsubtle.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouse_test2_vsubtle.getPos();
            mouse_test2_vsubtle.x.push(_mouseXYs[0]);
            mouse_test2_vsubtle.y.push(_mouseXYs[1]);
            mouse_test2_vsubtle.leftButton.push(_mouseButtons[0]);
            mouse_test2_vsubtle.midButton.push(_mouseButtons[1]);
            mouse_test2_vsubtle.rightButton.push(_mouseButtons[2]);
            mouse_test2_vsubtle.time.push(mouse_test2_vsubtle.mouseClock.getTime());
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test2_vsubtle_choiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test2_vsubtle_choiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test2_vsubtle_choice' ---
    for (const thisComponent of test2_vsubtle_choiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_test2_vsubtle.x) {  psychoJS.experiment.addData('mouse_test2_vsubtle.x', mouse_test2_vsubtle.x[0])};
    if (mouse_test2_vsubtle.y) {  psychoJS.experiment.addData('mouse_test2_vsubtle.y', mouse_test2_vsubtle.y[0])};
    if (mouse_test2_vsubtle.leftButton) {  psychoJS.experiment.addData('mouse_test2_vsubtle.leftButton', mouse_test2_vsubtle.leftButton[0])};
    if (mouse_test2_vsubtle.midButton) {  psychoJS.experiment.addData('mouse_test2_vsubtle.midButton', mouse_test2_vsubtle.midButton[0])};
    if (mouse_test2_vsubtle.rightButton) {  psychoJS.experiment.addData('mouse_test2_vsubtle.rightButton', mouse_test2_vsubtle.rightButton[0])};
    if (mouse_test2_vsubtle.time) {  psychoJS.experiment.addData('mouse_test2_vsubtle.time', mouse_test2_vsubtle.time[0])};
    if (mouse_test2_vsubtle.clicked_name) {  psychoJS.experiment.addData('mouse_test2_vsubtle.clicked_name', mouse_test2_vsubtle.clicked_name[0])};
    
    // the Routine "test2_vsubtle_choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var show_continue_test2_vsubtle;
var test2_vsubtle_rateComponents;
function test2_vsubtle_rateRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test2_vsubtle_rate' ---
    t = 0;
    test2_vsubtle_rateClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    slider_test2_vsubtle.reset()
    slider_target_test2_vsubtle.setPos(target_position);
    slider_target_test2_vsubtle.setImage(stim1);
    slider_distractor_test2_vsubtle.setPos(distractor_position);
    slider_distractor_test2_vsubtle.setImage(distractor);
    // Run 'Begin Routine' code from show_continue_rate_test2_vsubtle
    show_continue_test2_vsubtle = false;
    
    // setup some python lists for storing info about the mouse_continue_test2_vsubtle
    mouse_continue_test2_vsubtle.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    test2_vsubtle_rateComponents = [];
    test2_vsubtle_rateComponents.push(slider_text_test2_vsubtle);
    test2_vsubtle_rateComponents.push(slider_test2_vsubtle);
    test2_vsubtle_rateComponents.push(slider_target_test2_vsubtle);
    test2_vsubtle_rateComponents.push(slider_distractor_test2_vsubtle);
    test2_vsubtle_rateComponents.push(continue_rate_test2_vsubtle);
    test2_vsubtle_rateComponents.push(mouse_continue_test2_vsubtle);
    
    for (const thisComponent of test2_vsubtle_rateComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var slid2;
function test2_vsubtle_rateRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test2_vsubtle_rate' ---
    // get current time
    t = test2_vsubtle_rateClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slider_text_test2_vsubtle* updates
    if (t >= 0.0 && slider_text_test2_vsubtle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_text_test2_vsubtle.tStart = t;  // (not accounting for frame time here)
      slider_text_test2_vsubtle.frameNStart = frameN;  // exact frame index
      
      slider_text_test2_vsubtle.setAutoDraw(true);
    }

    
    // *slider_test2_vsubtle* updates
    if (t >= 0.0 && slider_test2_vsubtle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_test2_vsubtle.tStart = t;  // (not accounting for frame time here)
      slider_test2_vsubtle.frameNStart = frameN;  // exact frame index
      
      slider_test2_vsubtle.setAutoDraw(true);
    }

    
    // *slider_target_test2_vsubtle* updates
    if (t >= 0.0 && slider_target_test2_vsubtle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_target_test2_vsubtle.tStart = t;  // (not accounting for frame time here)
      slider_target_test2_vsubtle.frameNStart = frameN;  // exact frame index
      
      slider_target_test2_vsubtle.setAutoDraw(true);
    }

    
    // *slider_distractor_test2_vsubtle* updates
    if (t >= 0 && slider_distractor_test2_vsubtle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_distractor_test2_vsubtle.tStart = t;  // (not accounting for frame time here)
      slider_distractor_test2_vsubtle.frameNStart = frameN;  // exact frame index
      
      slider_distractor_test2_vsubtle.setAutoDraw(true);
    }

    // Run 'Each Frame' code from show_continue_rate_test2_vsubtle
    slid2 = slider_test2_vsubtle.getRating();
    if (slid2) {
        show_continue_test2_vsubtle = true;
    } else {
        show_continue_test2_vsubtle = false;
    }
    
    
    // *continue_rate_test2_vsubtle* updates
    if ((show_continue_test2_vsubtle) && continue_rate_test2_vsubtle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_rate_test2_vsubtle.tStart = t;  // (not accounting for frame time here)
      continue_rate_test2_vsubtle.frameNStart = frameN;  // exact frame index
      
      continue_rate_test2_vsubtle.setAutoDraw(true);
    }

    // *mouse_continue_test2_vsubtle* updates
    if (t >= show_continue_test2_vsubtle && mouse_continue_test2_vsubtle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_continue_test2_vsubtle.tStart = t;  // (not accounting for frame time here)
      mouse_continue_test2_vsubtle.frameNStart = frameN;  // exact frame index
      
      mouse_continue_test2_vsubtle.status = PsychoJS.Status.STARTED;
      mouse_continue_test2_vsubtle.mouseClock.reset();
      prevButtonState = mouse_continue_test2_vsubtle.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_continue_test2_vsubtle.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_continue_test2_vsubtle.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [continue_rate_test2_vsubtle]) {
            if (obj.contains(mouse_continue_test2_vsubtle)) {
              gotValidClick = true;
              mouse_continue_test2_vsubtle.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test2_vsubtle_rateComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function test2_vsubtle_rateRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test2_vsubtle_rate' ---
    for (const thisComponent of test2_vsubtle_rateComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('slider_test2_vsubtle.response', slider_test2_vsubtle.getRating());
    psychoJS.experiment.addData('slider_test2_vsubtle.rt', slider_test2_vsubtle.getRT());
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "test2_vsubtle_rate" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var debriefComponents;
function debriefRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'debrief' ---
    t = 0;
    debriefClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the cont_debrief_mouse
    cont_debrief_mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    debrief_image.setImage(debrief_img);
    // keep track of which components have finished
    debriefComponents = [];
    debriefComponents.push(cont_debrief);
    debriefComponents.push(cont_debrief_mouse);
    debriefComponents.push(debrief_image);
    
    for (const thisComponent of debriefComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function debriefRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'debrief' ---
    // get current time
    t = debriefClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cont_debrief* updates
    if (t >= 0.0 && cont_debrief.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont_debrief.tStart = t;  // (not accounting for frame time here)
      cont_debrief.frameNStart = frameN;  // exact frame index
      
      cont_debrief.setAutoDraw(true);
    }

    // *cont_debrief_mouse* updates
    if (t >= 0.0 && cont_debrief_mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cont_debrief_mouse.tStart = t;  // (not accounting for frame time here)
      cont_debrief_mouse.frameNStart = frameN;  // exact frame index
      
      cont_debrief_mouse.status = PsychoJS.Status.STARTED;
      cont_debrief_mouse.mouseClock.reset();
      prevButtonState = cont_debrief_mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (cont_debrief_mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = cont_debrief_mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [cont_debrief]) {
            if (obj.contains(cont_debrief_mouse)) {
              gotValidClick = true;
              cont_debrief_mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *debrief_image* updates
    if (t >= 0.0 && debrief_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debrief_image.tStart = t;  // (not accounting for frame time here)
      debrief_image.frameNStart = frameN;  // exact frame index
      
      debrief_image.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of debriefComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function debriefRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'debrief' ---
    for (const thisComponent of debriefComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "debrief" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var no_comprehensionComponents;
function no_comprehensionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'no_comprehension' ---
    t = 0;
    no_comprehensionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_exit_no_compr
    mouse_exit_no_compr.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    no_comprehensionComponents = [];
    no_comprehensionComponents.push(no_compr_textbox);
    no_comprehensionComponents.push(exit_box_no_compr);
    no_comprehensionComponents.push(mouse_exit_no_compr);
    
    for (const thisComponent of no_comprehensionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function no_comprehensionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'no_comprehension' ---
    // get current time
    t = no_comprehensionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *no_compr_textbox* updates
    if (t >= 0 && no_compr_textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no_compr_textbox.tStart = t;  // (not accounting for frame time here)
      no_compr_textbox.frameNStart = frameN;  // exact frame index
      
      no_compr_textbox.setAutoDraw(true);
    }

    
    // *exit_box_no_compr* updates
    if (t >= 0 && exit_box_no_compr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      exit_box_no_compr.tStart = t;  // (not accounting for frame time here)
      exit_box_no_compr.frameNStart = frameN;  // exact frame index
      
      exit_box_no_compr.setAutoDraw(true);
    }

    // *mouse_exit_no_compr* updates
    if (t >= 0 && mouse_exit_no_compr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_exit_no_compr.tStart = t;  // (not accounting for frame time here)
      mouse_exit_no_compr.frameNStart = frameN;  // exact frame index
      
      mouse_exit_no_compr.status = PsychoJS.Status.STARTED;
      mouse_exit_no_compr.mouseClock.reset();
      prevButtonState = mouse_exit_no_compr.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_exit_no_compr.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_exit_no_compr.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [exit_box_no_compr]) {
            if (obj.contains(mouse_exit_no_compr)) {
              gotValidClick = true;
              mouse_exit_no_compr.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of no_comprehensionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function no_comprehensionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'no_comprehension' ---
    for (const thisComponent of no_comprehensionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "no_comprehension" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var no_consent_trialComponents;
function no_consent_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'no_consent_trial' ---
    t = 0;
    no_consent_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_exit
    mouse_exit.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    no_consent_trialComponents = [];
    no_consent_trialComponents.push(no_consent_textbox);
    no_consent_trialComponents.push(exit_box);
    no_consent_trialComponents.push(mouse_exit);
    
    for (const thisComponent of no_consent_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function no_consent_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'no_consent_trial' ---
    // get current time
    t = no_consent_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *no_consent_textbox* updates
    if (t >= 0 && no_consent_textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no_consent_textbox.tStart = t;  // (not accounting for frame time here)
      no_consent_textbox.frameNStart = frameN;  // exact frame index
      
      no_consent_textbox.setAutoDraw(true);
    }

    
    // *exit_box* updates
    if (t >= 0 && exit_box.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      exit_box.tStart = t;  // (not accounting for frame time here)
      exit_box.frameNStart = frameN;  // exact frame index
      
      exit_box.setAutoDraw(true);
    }

    // *mouse_exit* updates
    if (t >= 0 && mouse_exit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_exit.tStart = t;  // (not accounting for frame time here)
      mouse_exit.frameNStart = frameN;  // exact frame index
      
      mouse_exit.status = PsychoJS.Status.STARTED;
      mouse_exit.mouseClock.reset();
      prevButtonState = mouse_exit.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_exit.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_exit.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [exit_box]) {
            if (obj.contains(mouse_exit)) {
              gotValidClick = true;
              mouse_exit.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of no_consent_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function no_consent_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'no_consent_trial' ---
    for (const thisComponent of no_consent_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "no_consent_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
