#!/usr/bin/env python
#
# Produces a progress bar on the terminals.
#
# Usage:
# Initialize by running ./shell_progress_bar.py START END
# where START and END are integers
#
# Increment progress bar by running ./shell_progress_bar.py INCREMENT
#
# When the counter hits END, the progress will read 100% from then on.
#
# The counter stores its state in a file called ".progress".

DEFAULT_FILENAME = ".progress"


def save_state(start, end, filename=DEFAULT_FILENAME):
    if start >= end:
        from os.path import isfile
        from os import remove

        if isfile(filename):
            remove(filename)
        return

    with open(filename, 'w') as progfile:
        progfile.write("{0}\t{1}\n".format(start, end))


def get_state(filename=DEFAULT_FILENAME):
    from os.path import isfile
    if not isfile(filename):
        return None

    with open(filename, "r") as progfile:
        return [int(i) for i in progfile.readline().strip().split()]


def display_progress(start, end):
    from sys import stdout
    WIDTH = 40

    stdout.write("\r")

    progress = float(start) / end

    if progress > 1:
        progress = 1

    num_stops = int(WIDTH * progress)
    num_spaces = WIDTH - num_stops

    stdout.write("%s%%" % int(progress*100))

    stdout.write("|")
    stdout.write("=" * num_stops)
    stdout.write(" " * num_spaces)
    stdout.write("|")


if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    start = None
    end = None

    if not args:
        display_progress(*get_state())
        exit(0)

    if args:
        start = int(args[0])

    if len(args) > 1:
        end = int(args[1])

    if end:
        display_progress(start, end)
        state = (start, end)
    else:
        state = get_state()
        state[0] += start
        display_progress(state[0], state[1])

    save_state(*state)
