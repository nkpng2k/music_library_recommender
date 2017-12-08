import os
import librosa


starting_dir = '/Users/npng/Music/iTunes/iTunes Media/Music'


def recursive_file_gen(mydir):
    for root, dirs, files in os.walk(mydir):
        for item in files:
            yield os.path.join(root, item)


def gen_music_load(all_music):
    for item in all_music:
        y, sr = librosa.load(item)
        yield y, sr


def get_tempo(loaded_gen):
    for y, sr in loaded_gen:
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        yield tempo, beat_frames


all_music = list(recursive_file_gen(starting_dir))

all_tempos = get_tempo(gen_music_load(all_music))

count = 0
for tempo, beat_frames in all_tempos:
    count += 1
    print tempo, beat_frames
    if count > 5:
        break
