import multiprocessing
import subprocess


class InkscapeWorker(multiprocessing.Process):
    def __init__(self, queue):
        super(InkscapeWorker, self).__init__()
        self.queue = queue

    def run(self):
        for svg_file, pdf_file_name, cached in iter(self.queue.get, None):
            # main working loop of the inkscape process
            # subprocess.call waits until process is finished
            if not cached:
                command = 'inkscape {0} -o {1}'.format(svg_file, pdf_file_name)
                ret = subprocess.call(command.split(" "))
                assert (ret == 0)
                print("  Converted {0}".format(pdf_file_name))
            else:
                print("  Skipping {0}".format(pdf_file_name))

