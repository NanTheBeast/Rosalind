#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @IDE: PyCharm
# @date: Sep-17-2018 5:05 PM
# @author: nhu

"""
Usage 	python3 CountingDNA -h for help.
		python3 CountingDNA -f filename .
		the results is the number of "ACGT" respectively.
"""

import argparse

def CountDNA(s):
    a=str(s.count("A"))
    c=str(s.count("C"))
    g=str(s.count("G"))
    t=str(s.count("T"))
    result = a+' '+c+' '+g+' '+t
    return(result)


if __name__ == "__main__":
    # parse the arguments, users can input file
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--filename", type=str, help = "input filename")
    args = parser.parse_args()

    file = args.filename if args.filename is not None else input("input a filename:")

    f = open(file,"r")
    nt = f.read().strip('\n')
    f.close()
    tmp = CountDNA(nt)
    print(tmp)
