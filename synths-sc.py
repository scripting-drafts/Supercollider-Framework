from cmath import pi
from time import sleep
from sc3.all import *
from sc3.all import SinOsc, EnvGen, Out

# s.quit()
# s.free_nodes()
# s.boot()
# s.dump_tree(True)
# sleep(10)

@synthdef
def sine(freq=440, amp=1, gate=1):
    sig = SinOsc(freq) * amp
    env = EnvGen(Env.adsr(), gate, done_action=2)
    Out(0, (sig * env).dup())

sine.dump_ugens()

x = Synth("sine")

# SinOsc(300)

# count = 10
# while count:
#     sleep(1)
#     count -= 1

# @synthdef
# def new(total_waves = 4, freq = 36.71, amp = 0.1, gate = 1):
#     env = EnvGen(Env.adsr(), gate, done_action=2)
#     freqs = []
    
#     for _ in range(total_waves):
#         freqs.append(freq)
#         freq = freq * 2

#     sigs = [SinOsc(x) * amp for x in freqs]
#     # sigs = [sig * env for sig in sigs]
#     Mix()

#     Out(0, (sig * env).dup())

# new.dump_ugens()

# x = Synth("new")

# sleep(20)

x.release()
# s.free_nodes()
# s.quit()