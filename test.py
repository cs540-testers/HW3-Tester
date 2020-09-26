"""
HW3 is to be written in a file called nqueens.py with the following interface:

succ(state: list, static_x: int, static_y: int)
f(state: list)
choose_next(curr: list, static_x: int, static_y: int)
n_queens(initial_state: list, static_x: int, static_y: int)
n_queens_restart(n: int, k: int, static_x: int, static_y: int)

Make sure to set the random_seed to 1 otherwise your results will not match
"""
__author__ = "cs540-testers"
__credits__ = ["Saurabh Kulkarni", "Alex Moon", "Stephen Jasina", "haclark"]

import sys
from nqueens import *
import time
import difflib
import random

# we're still not sure about the solution to queens_restart yet
version = "V1.0"

if __name__ == '__main__':
    print("Tester %s" % version)

    backup_stdout = sys.stdout
    sys.stdout = open("test.txt", "w")

    starttime = time.time()

    # VERSION NUMBER IS NECESSARY. DO NOT MODIFY
    print("Version: %s\n" % (version))

    print("succ([0, 1, 2], 0, 0)")
    print(succ([0, 1, 2], 0, 0))
    print("succ([1, 1, 2], 0, 0)")
    print(succ([1, 1, 2], 0, 0))
    print("succ tests complete\n")

    print("f([1, 2, 2])")
    print(f([1, 2, 2]))
    print("f([2, 2, 2])")
    print(f([2, 2, 2]))
    print("f([0, 0, 2])")
    print(f([0, 0, 2]))
    print("f([0, 2, 0])")
    print(f([0, 2, 0]))
    print("f([0, 2, 1])")
    print(f([0, 2, 1]))
    print("f tests complete\n")

    print("choose_next([1, 1, 2], 1, 1)")
    print(choose_next([1, 1, 2], 1, 1))
    print("choose_next([0, 2, 0], 0, 0)")
    print(choose_next([0, 2, 0], 0, 0))
    print("choose_next([0, 1, 0], 0, 0)")
    print(choose_next([0, 1, 0], 0, 0))
    print("choose_next([0, 1, 0], 0, 1)")
    print(choose_next([0, 1, 0], 0, 1))
    print("choose_next tests complete\n")

    print("n_queens([0, 1, 2, 3, 5, 6, 6, 7], 1, 1)")
    print(n_queens([0, 1, 2, 3, 5, 6, 6, 7], 1, 1))
    print("n_queens([0, 7, 3, 4, 7, 1, 2, 2], 0, 0)")
    print(n_queens([0, 7, 3, 4, 7, 1, 2, 2], 0, 0))
    print("n_queens tests complete\n")

    # DO NOT SET YOUR OWN SEED FOR THESE TESTS
    # If you want, you can set it to 1 at the beginning of n_queens_restart
    # This tester expects you to make N - 1 randint() calls on each iteration
    # randrange(N) and randint(0, N-1) are identical
    # n_queens_restart does not return anything. it only prints.
    print("n_queens_restart(7, 10, 0, 0)")
    random.seed(1)
    n_queens_restart(7, 10, 0, 0)
    print("n_queens_restart(8, 1000, 0, 0)")
    random.seed(1)
    n_queens_restart(8, 1000, 0, 0)
    print("n_queens_restart tests complete\n")

    endtime = time.time()

    sys.stdout.close()
    sys.stdout = backup_stdout

    print("Elapsed time was: %.5fs" % (endtime - starttime))
    print("Reference runtime is ~0.75s")
    print("See diff below. "
        + "If you see nothing but the end message, you're good.")
    with open("test.txt", "r") as livefile:
        l_text = livefile.readlines()
        with open("ref.txt", "r") as reffile:
            r_text = reffile.readlines()
            for line in difflib.context_diff(l_text, r_text):
                print(line.strip())
    print("This is the end of the tester.\n\n"
          + "If you think you have a correct solution,\n"
          + "please copy the printed output of this tester\n"
          + "from 'Tester " + version
          + "' to 'This is the end of the tester.'\n"
          + "and paste it into an issue on \n"
          + "https://github.com/cs540-testers/HW3-Tester/issues")
