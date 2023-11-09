# SuperCollider Python Framework

boot server
s.boot

SinOsc: Sinusoidal Oscilator  
ar: generate audio signal  
kr: generate control signal  
arg 1: Freq as float (261.26) in Hz's  
  midiValue(0 - 127).midicps: Notes via midi values  
arg 2: Phase offset in radians (Position from which the wave starts)  
arg 3: Wave amplitude - Volume  
  
{SinOsc.ar(261.26, 0, 0.7)}.play;  
{SinOsc.ar(60.midicps, 0, 0.7)}.play  
  
Naming parameters (any order):  
{SinOsc.ar(mul:0.7, freq:261.26, phase:pi)}.play;  
  
Execute: CTRL+ENTER  
Terminate: CTRL+.  
  
.play: Sound  
.scope: Scope  
.plot: Snapshot (.1s by default)  
    .plot(1): Arg for plot length in seconds  
  
Left for channel 0 (default)  
{SinOsc.ar(261.26, 0, 0.7)}.play;  
  
Right channel:  
{SinOsc.ar([0, 300], pi, 0.7)}.play;  
  
Both channels, different parameters  
{SinOsc.ar([261.26, 300], pi, [0.7, 0.5])}.play; // {[nil, SinOsc.ar(300, pi, 0.7)]}.play;  
  
Manipulate stereo  
x = {SinOsc.ar(261.26, pi, 0.7)}.play;  
y = {[nil, SinOsc.ar(300, pi, 0.5)]}.play;  
x.free;  
y.free;  
  
LFO to amplitude  
{LFSaw.ar(200, 0, 1 * SinOsc.kr(1, 0, 1))}.scope;  
  
PanN function, args are audio signal and pan (-1 (left) and +1 (right)), N depends on channels nº  
{Pan2.ar( LFSaw.ar(200, 0, 1 * SinOsc.kr(1, 0, 1).abs), SinOsc.kr(0.5))}.play;  
  
  
Mix.fill -> Additive synthesis of multiple waves, arg1 are the number of waves  
  
(  
  var waves=8;  
   
  {Pan2.ar  
    (Mix.fill(waves,  
      { LFSaw.ar(200 + 200.0.rand, 0, 1 / waves) }  
      ),  
      SinOsc.kr(0.5)  
    )}.play;  
)  
  
  
SynthDef -> def of a synth  
arg1: Name  
arg2:  
    - args  
    - Out.ar (write to channel[0,1] left and right, audio signal)  
    - .add / .writeDefFile (add it to the server / initiate it on runtime)  
(  
SynthDef("sinewave",  
  {arg myfreq=261.626, myvol=0.5;  
  Out.ar([0, 1], SinOsc.ar(myfreq, 0, myvol))  
  }).add;  
)  
  
Initiate  
x=Synth("sinewave");  
  
Initiate with args  
x=Synth("sinewave", [myfreq:400]);  
  
Manipulate in real time  
x.set("myfreq", 200)  
