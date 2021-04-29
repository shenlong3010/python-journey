#!/usr/bin/python

import os
args = ("test", "abc")
os.execvp("test.sh", args)
