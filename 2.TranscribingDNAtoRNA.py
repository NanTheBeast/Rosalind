#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @IDE: PyCharm
# @date: Sep-17-2018 7:46 PM
# @author: nhu


"""
Usage 	python3 Transcribing -h for help.
		python3 Transcribing -f filename .
		the results is the RNA nucleotides.
"""

import argparse

def Transcribing(s):
    return(s.replace("T", "U"))

if __name__ == '__main__':
    # parse the arguments, users can input file
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--filename", type=str, help = "input filename")
    args = parser.parse_args()

    file = args.filename if args.filename is not None else input("input a filename:")

    f = open(file,"r")
    nt = f.read().strip('\n')
    f.close()

    tmp = Transcribing(nt)
    print(tmp)
    ff = open("2.rna_results.txt","w")
    ff.write(tmp)
    ff.close()
