__author__ = 'shgli'
import sys
from termcolor import colored, cprint
def critical(self, s):
    cprint(s,'blue', attrs=['bold'], file=sys.stderr)
    sys.exit(-1)

def error(self, s):
    cprint(s,'red', attrs=['bold'], file=sys.stderr)

def warn(self, s):
    cprint(s,'yellow', attrs=['bold'], file=sys.stderr)

def info(self, s):
    cprint(s,'green', attrs=['bold'], file=sys.stderr)
