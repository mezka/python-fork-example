import os
import time

for i in range(2):
    print('**********{} by {} ***********'.format(i, os.getpid()))
    pid = os.fork()
    if pid == 0:
        # We are in the child process.
        print("We are in the child process {}, with parent {}".format(os.getpid(), os.getppid()))
    else:
        # We are in the parent process.
        print("We are in the parent process {}, just created {}.".format(os.getpid(), pid))