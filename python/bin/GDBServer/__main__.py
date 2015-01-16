#!/usr/bin/env python
import os
import sys

def _PathToGDB():
	return "/usr/bin/gdb"

def _PathToStartScript():
	return os.path.join(os.path.dirname(os.path.abspath(__file__)), "startscript.py")

if __name__ == "__main__":
	os.execv(_PathToGDB(), [_PathToGDB(), sys.argv[1], "-x", _PathToStartScript()])

