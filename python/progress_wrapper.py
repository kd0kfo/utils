#!/usr/bin/env python
#
# Convenient class for progressbar package
# https://pypi.python.org/pypi/progressbar
# Tested with version 2.2.


class Progress:
    def __init__(self, num_steps):
        from progressbar import ProgressBar, Percentage, Bar

        self.progress_counter = 0
        self.num_steps = num_steps
        self.progress_bar = ProgressBar(widgets = [Percentage(), Bar()], maxval=num_steps).start()

    def update(self):
        self.progress_counter += 1
        self.progress_bar.update(self.progress_counter)

    def reset_stdout(self):
        print("")
