#!/usr/bin/python
import os

env = {
    "PATH":"/mnt/c/Users/shenl/programming/python-projects/python-journey/library/os/fork/",
    "XYZ":"Bla",
}

args = ("test", "abc")
os.execvpe("test.sh", args, env)
