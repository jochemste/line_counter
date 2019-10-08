import os
import glob

class Line_counter():
    ctr: int
    def __init__(self):
        self.ctr = 0

    def __del__(self):
        pass

    def count_lines_dir(self, path_dir=os.getcwd()):
        self.ctr = 0
        for filename in os.listdir(path_dir):
            with open(filename, 'r') as fd:
                fd = fd.readlines()
                for line in fd:
                    self.ctr += 1
        return self.ctr    

    def count_lines_dir_w_ext(self, ext: str, path_dir=os.getcwd()):
        self.ctr = 0
        if not('.' in ext):
            ext = '.' + ext
        for filename in glob.glob(os.path.join(path_dir, ('*' + ext))):
            with open(filename, 'r') as fd:
                fd = fd.readlines()
                for line in fd:
                    self.ctr += 1
        return self.ctr

    def count_lines_file(self, path_file=__file__):
        self.ctr = 0
        with open(path_file, 'r') as fd:
            fd = fd.readlines()
            for line in fd:
                self.ctr += 1
        return self.ctr
