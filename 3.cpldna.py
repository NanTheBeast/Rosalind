#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @IDE: PyCharm
# @date: Sep-18-2018 9:49 AM
# @author: nhu


"""
Usage   Python3 CompeletingDNA.py -h for help.
        Python3 CompeletingDNA.py -f for filename.
        The result is the complementing strand of DNA.
"""


import argparse

def ComplementDNA(s):
    cs = s.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()
    return cs[::-1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", type=str, help= "input filename")
    args = parser.parse_args()

    file = args.filename if args.filename is not None else input("input a filename:")

    f = open(file,"r")
    nt = f.read().strip('\n')
    f.close()

    tmp = ComplementDNA(nt)
    # print(tmp)
    ff = open("3.revc_results.txt","w")
    ff.write(tmp)
    ff.close()
