from time import sleep
# from sc3f import server_boot, server_quit, set_synth, start_synth, stop_synth
# from sc3f import Synths_MGMT
from sc3.all import Synth   #, synthdef, SinOsc, EnvGen, Env, Out
# import numpy as np

# harmonics = [1, 2, 4, 6, 8, 10]
# # freq_eq = [np.linspace(0, 20000, 0.1), np.array(np.linspace(0, 1, 0.001))]

# freq_eq = np.zeros((20000), 0.001)
# print(freq_eq)

# freq = [x for x in range(0., freq, 0.1)]

# waves_shapes = {
#     "LFSaw": LFSaw(),
#     "pure_wave": Osc(),
#     "sin_osc": SinOSC(),
#     "sync_saw": SyncSaw()
# }

# eq = {
#     "low_cut_LOW" : freq[0],
#     "high_cut_LOW" :freq[80],

#     "low_cut_MEDIUM_low" : freq[120] ,
#     "mid_cut_MEDIUM" : freq[300],
#     "high_cut_MEDIUM" : freq[600],

#     "low_cut_high" : freq[1200],
#     "mid_cut_high" : freq[3000],
#     "high_cut_high": freq[12000],

#     "top_cut": freq[-1]
# }

# n = [Synth('reso', f, 1 / len(freq_eq[0])) for f, e in freq_eq.tolist()]
# n.set('amp', 0.05)
# n.set('freq', 550)

n = Synth('ha_reso')
sleep(10)

n.release()
# synths = Synths_MGMT()
# synth_name = synths.set_synth()
# synth = synths.start_synth(synth_name)

# synths.stop_synth(synth)