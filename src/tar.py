#!/usr/bin/env python3

import os, sys
from sys import argv

sys.path.append("../lib")  # for framedIO

import framedIO as io 


class Archiver():
    def __init__(self):
        self.MAXARCHIVESIZE = 5*2**30  # max size for unpacking archive 5GB

    # frames files in argv and writes archive bytes to STDOUT
    def pack(self):
        fr = io.FramedReader()
        data = fr.read(argv[2:])

        bw = io.BufferedWriter(1)
        bw.write(data)
        bw.close
        
    # unframes bytestring in STDIN and writes files
    def unpack(self):
        br = io.BufferedReader(0)  # STDIN
        data = br.read(self.MAXARCHIVESIZE)
        br.close()

        fw = io.FramedWriter()
        fw.write(data)

    
### MAIN ###
arch = Archiver()

if len(argv) < 2:
    os.write(2, b"tar.py: Must specify one of c, x\n")  # STDERR message
    exit()

if argv[1] == 'x':
    arch.unpack()
elif argv[1] == 'c':
    for name in argv[2:]:
        if not os.path.exists(name):
            errstr = f"tar.py: file '{name}' does not exist"
            exit()
    arch.pack()
else:
    os.write(2, b"tar.py: Must specify one of c, x\n")  # STDERR message
    exit()


        
