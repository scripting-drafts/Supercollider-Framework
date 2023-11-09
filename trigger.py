import multiprocessing
from os import chdir
from subprocess import getoutput
from functools import partial
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


def get_files():
    chdir("Audio Files")
    # chdir("{}\\Audio Files".format(base_path))
    filenames = getoutput("ls").replace("\n", " ").split()[:-1]
    print(filenames)
    source_files = [wave.open(file, "r") for file in filenames]
    return filenames, source_files

def get_files_data(source_files):
    signals = [src.readframes(-1) for src in source_files]
    signals = [np.frombuffer(sig, np.int16) for sig in signals]
    fss = [src.getframerate() for src in source_files]
    durations = [np.linspace(0, len(sig) / fs, num=len(sig)) for sig, fs in zip(signals, fss)]
    return signals, durations

def stop_if_stereo(source_files):
    '''
    No Stereo support
    '''
    if source_files.getnchannels() == 2:
        print("Just mono files")
        sys.exit(0)

def prepare_data(filenames, durations, signals):
    fig, axs = plt.subplots(len(signals), 3, figsize=(9, 3), sharey=True, squeeze=False)
    axs = axs.flatten()
    args = [[x, title, time, sig] for x, title, time, sig in zip(axs, filenames, durations, signals)]
    return fig, args

def generate_drawing_instances(args):
    pool = multiprocessing.Pool()
    func = partial(draw_subplot,)
    pool.map(func, args)
    # pool.close()
    # pool.join()

def draw_subplot(args):
    axs, fileName, time, sig = args
    axs.title.set_text(fileName)
    axs[0].bar(time, sig)
    axs[1].scatter(time, sig)
    axs[2].plot(time, sig)