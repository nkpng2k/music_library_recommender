import os


class MusicProcessor(object):

    def __init__(self, train_dir):
        """
        Music Preprocessor for parsing audio files

        INPUT: train_dir --> STRING: filepath to top of directory tree
                                     containing all training audio files
        ATTRIBUTES: self.train_files --> LIST: all file names of training data
        """
        self.train_files = list(self._get_file_names(train_dir))

    def _get_file_names(self, start_dir):
        """
        Recursively search for all files under directory tree
        starting at <starting_dir>
        NOTE: recursive function, assumes start_dir points to files ONLY
              containing audio files (.mp3, .wav, .flac, etc.)

        INPUT: start_dir --> STRING path to directory containing all audio
                             files to be used.
        OUTPUT: generator object containing list of all files
        """
        for root, dirs, files in os.walk(start_dir):
            for item in files:
                yield os.path.join(root, item)


if __name__ == "__main__":
    start_dir = '/Users/npng/Music/iTunes/iTunes Media/Music'
    processor = MusicProcessor(start_dir)
