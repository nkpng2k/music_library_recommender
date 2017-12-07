import numpy as np
import os
import librosa


starting_dir = '/Users/npng/Music/iTunes/iTunes Media/Music'


def recursive_file_gen(mydir):
    for root, dirs, files in os.walk(mydir):
        for item in files:
            yield os.path.join(root, item)


all_music = recursive_file_gen(starting_dir)
all_music


print np.sqrt(2.0)
librosa.audio
