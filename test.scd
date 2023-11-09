s.boot

{SinOsc.ar(261.26, pi, 0.7)}.scope;

{
	var wave;
	wave = SinOsc.ar(261.26, pi, Pulse.kr(1.0, 0.5, 1));
	BPF.ar(SinOsc.kr(261.26, pi, 0.5), 261.26, 0.8).scope;
}

{ BPF.ar(SinOsc.ar(261.26, pi, 0.5), FSinOsc.kr(XLine.kr(0.7,300,20),0,3600,4000), 0.3) }.play;
{ BPF.ar(SinOsc.ar(261.26, pi, 0.5), MouseX.kr(100, 10000, 1), 0.1) }.play;


// Freq modulation as sine
{ LPF.ar(SinOsc.ar(261.26, pi, 0.7), SinOsc.kr(XLine.kr(100, 300, 10), pi, 1), 70) }.play;


// Wobble, sine as freq mod at 300, q 70
{
	var freq = 293.66
	LPF.ar(SinOsc.ar(freq, pi, 0.7), SinOsc.kr(freq, pi, 1), 70).scope;
}


(
SynthDef("simpleWobble",
	{arg myfreq=293.66, phaser=pi, amplitude=0.7, gain=0;
    Out.ar([0, 1],
			LPF18.ar(SinOsc.ar(myfreq, phaser, amplitude, gain),
			SinOsc.kr(myfreq, phaser, amplitude, gain), 90))
    }).writeDefFile;
)

(
a = SpectrogramWindow.new;
//{SinOsc.ar(MouseY.kr(22050, 1).poll(10, "frequency: "))}.play
{ LPF18.ar(SinOsc.ar(293.6, pi, 0.7, 0), SinOsc.kr(293.6, pi, 0.7, 0), 90) }.play;
a.start;
)


// Additive synthesis
(
    var total_waves = 4;
    var freq = 36.71;
    {
        Mix.fill(total_waves, {
            freq = freq * 2;
            freq.postln;
            SinOsc.ar(freq , 0, 1 / total_waves)
        })
    }.play;
)

(
    var total_waves = 4;
    var freq = 36.71;
    {
        Mix.fill(total_waves, {
            freq = freq * 2;
            freq.postln;
            LPF.ar(SinOsc.ar(freq, pi, 1 / total_waves, 0), SinOsc.kr(freq, pi, 0.7, 0), 90)
        })
    }.play;
)


(
    var total_waves = 4;
    var freq = 36.71;
    {
        Mix.fill(total_waves, {
            freq = freq * 2;
            freq.postln;
    		LPF.ar(SinOsc.ar(freq, pi, 1 / total_waves, 0), SinOsc.kr(freq, pi, 0.7, 0), 90)
        })
    }.play;
)



// Additive SynthDef
(
SynthDef("additiveSynth",
	{arg total_waves = 4, freq=36.71, oscfreq=36.71, phaser=pi, amplitude=0.7, gain=0;
    Out.ar([0, 1],
			Mix.fill(total_waves, {
            freq = freq * 2;
            freq.postln;
            LPF.ar(SinOsc.ar(freq, pi, 1 / total_waves, 0), SinOsc.kr(freq, pi, 0.7, 0), 90)
			})
    )}).writeDefFile;
)


(
(1, 2, 4, 6).do{|num|
    SynthDef("wob%".format(num), {|freq=36.71, amp=1 / 4|
        var oscs;
        oscs = Mix.fill(num, {|index|
            SinOsc.ar(freq * index)
        });
        Out.ar(0, oscs * amp);
    }).add;

}
)


(
SynthDef("rotatingWobble",
	{arg myfreq=293.66, phaser=pi;
		Out.ar([0, 1], LPF.ar(SinOsc.ar(myfreq, pi, 0.7), SinOsc.kr(myfreq, phaser, 1), 70))
    }).writeDefFile;
)

w = Synth("simpleWobble", [myfreq:293.66, phaser:pi, amplitude:0.7, gain:0.001]);

w = Synth("rotatingWobble", [myfreq:300, phaser:pi]);

// LPF.ar(SinOsc.ar(261.26, pi, 0.7), SinOsc.kr(300, pi, 1), 70) }.scope;

// Freq modulation as 0.1 pulse
{ LPF.ar(SinOsc.ar(261.26, pi, 0.7), PulseDPW.kr(XLine.kr(100, 300, 10), 0.1, 1), 20) }.play;

{ LPF18.ar(SinOsc.ar(261.26, pi, 0.7), PulseDPW.kr(XLine.kr(100, 300, 10), 0.1, 1), 20) }.play;

{ BPF.ar(SinOsc.ar(261.26, pi, 0.7), PulseDPW.kr(XLine.kr(100, 300, 10), 0.1, 1), 20) }.play;


{SinOsc.ar(261.26, pi, LFNoise1.kr(1 / 0.5))}.scope;

{SinOsc.ar(261.26, pi, Ramp.kr(Pulse.kr(0.1, 0.5, 1), 0.5))}.scope;

{SinOsc.ar(261.26, pi, Ramp.kr(0.3, 0.3))}.scope;



{ Pulse.ar(261.26, SinOsc.kr(0.2).range(0.01, 0.99), 0.2) }.play

{ Pulse.ar(261.26, 0.5, 0.2) }.play

{ Pan2.ar( Mix.fill( 8, { LFSaw.ar(200 + 200.0.rand, 0, 1 / 8) }), SinOsc.kr( 0.5 ) )  }.play;

Platform.userExtensionDir

Quarks.gui

//(
//  SynthDef("sinewave",
//    {arg myfreq=261.626, myvol=0.5;
//    Out.ar([0, 1], SinOsc.ar(myfreq, 0, myvol))
//    }).writeDefFile;
//)

{SinOsc.ar(Ramp.kr(LFPulse.kr(4, 0, 0.5, 50, 400), Line.kr(0, 1, 15)), 0, 0.3)}.play;

s.quit;