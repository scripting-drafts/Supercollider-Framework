# from time import sleep
from math import pi
# from sc3f import server_boot, server_quit, set_synth, start_synth, stop_synth
from sc3.all import SinOsc, EnvGen, Out, SinOsc, EnvGen, Env, Out, Mix, play

# @synthdef
# def sig_reso(freq=36.71, amp=1):
    
#     harmonics = [2, 4, 6, 8, 10]
#     amp = amp / len(harmonics)
#     base_sigs = [SinOsc(freq * h, phase=pi) * amp for h in harmonics]
#     return base_sigs
    
env = EnvGen(Env.adsr(), gate=1, done_action=2)
# 
# base_sigs = Synth('sig_reso')
# base_sigs = sig_reso(freq=36.71, amp=1)

amp = 1
freq=36.71
harmonics = [2, 4, 6, 8, 10]
amp = amp / len(harmonics)

sig = Mix.new([SinOsc(freq * h, phase=pi) * amp for h in harmonics])
out = Out(0, (LPF18(source_audio, LPF_control, 0.9, 90)* env).dup())
n = play(out, length=20)

# n = Synth('multi_reso')
# n.set('amp', 0.05)
# n.set('freq', 550)
# sleep(10)

n = False
# synths = Synths_MGMT()
# synth_name = synths.set_synth()
# synth = synths.start_synth(synth_name)

# synths.stop_synth(synth)