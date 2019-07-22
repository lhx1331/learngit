import numpy as np
import os
import midi
import midi_util
from essentia import *
from essentia.standard import *


sequence = midi_util.parse_midi_to_sequence(input_filename = './test.mid', time_step = 690, verbose = True)
print(sequence.shape)
audio = MonoLoader(filename = '../data/MAPS_ISOL_CH0.1_F_ENSTDkAm.wav')()
print(len(audio)/44100.0)
#sequence = sequence[:,21:109]
#print sequence.shape
