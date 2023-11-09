from time import sleep
# from sc3f import server_boot, server_quit, set_synth, start_synth, stop_synth
from sc3f import Server_MGMT, Synths_MGMT
from sc3.all import Synth, synthdef, SinOsc, EnvGen, Env, Out

servers = Server_MGMT()
s = servers.server_boot()

@synthdef
def sine(freq=440, amp=1, gate=1):
    sig = SinOsc(freq) * amp
    env = EnvGen(Env.adsr(), gate, done_action=2)
    Out(0, (sig * env).dup())

sine.dump_ugens()
sleep(20)

n = Synth('sine')
n.set('amp', 0.05)
n.set('freq', 550)
sleep(20)

n.release()
# synths = Synths_MGMT()
# synth_name = synths.set_synth()
# synth = synths.start_synth(synth_name)

# synths.stop_synth(synth)

servers.server_quit(s)
