# Brython Server default Python

from browser import document, alert
import sys, time

class StdOut(object):
    def write(self, data):
        document["console"] <= data
        document["console"].focus()

class StdErr(object):
    def write(self, data):
        document["console"] <= data

_input = input

def input(prompt):
    print(prompt, end="")
    retval = _input(prompt)
    return retval if retval else ""

sys.stdout = StdOut()
sys.stderr = StdErr()

document["console"].clear()

print("** Welcome to Brython Server (Python {0}.{1}.{2}) **".format(*sys.version_info[:3]))
print("")