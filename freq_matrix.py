
import numpy as np
import matplotlib.pyplot as plt

dt_freq = 20000 * 1000  # 0.01
dt_amp = 0.001
amp_mul = [x for x in str(dt_freq) if x != "."]
freq_amp = [np.linspace(0., 20000., num=dt_freq), np.linspace(-1., 1., num=dt_freq)] # np.zeros(20000 * amp_mul[-1:0])
print(freq_amp)
amp_set = np.arange(-1, 1, dt_amp)

np.random.seed(19680801)

# plt.ylim()

fig, axs = plt.subplots(1, 1)
plot = plt.plot(freq_amp[0], freq_amp[1])


axs.axis([0, 20000, -1, 1])
axs.grid(True, which="major")
axs.set_xlabel("Frequency")
axs.set_ylabel("Amplitude")
axs.plot(plot)

# fig = plt.figure()
# ax = fig.add_subplot(freq_amp)

major_ticks = np.arange(0, 20001, 2000)
minor_ticks = np.arange(-1, 1, .25)

axs.set_xticks(major_ticks)
axs.set_xticks(minor_ticks, minor=True)
axs.set_yticks(major_ticks)
axs.set_yticks(minor_ticks, minor=True)

# ##################################################################
# fig = plt.figure()
# fig.subplots_adjust(top=0.8)
# ax1 = fig.add_subplot(211)
# ax1.set_ylabel('volts')
# # ax1.set_title('a sine wave')

# t = freq_amp[1]
# s = np.sin(2 * np.pi * t)
# line, = ax1.plot(t, s, lw=2)

# # Fixing random state for reproducibility
# np.random.seed(19680801)

# ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
# n, bins, patches = ax2.hist(np.random.randn(1000), 50)
# ax2.set_xlabel('time (s)')
# ###################################################################

for i in freq_amp[0].tolist():
    nse1 = 1 + np.random.randn(freq_amp[1][i])
    s1 = np.sin(2 * np.pi * 10 * i) + nse1
    plt.plot(freq_amp)
    plt.pause(0.01)

plt.show()