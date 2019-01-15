#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @IDE: PyCharm
# @date: Jan-15-2019 11:19 AM
# @author: nhu


"""
Usage   Python3 wabbits.py -h for help.
        Python3 wabbits.py -f for filename.
        The result is the number of rabbits at n_th generation.
"""


import argparse

def fib(n, k):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, k*a + b
    return b


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", type=str, help= "input filename")
    args = parser.parse_args()

    file = args.filename if args.filename is not None else input("input a filename:")

    f = open(file,"r")
    nt = f.read().strip('\n')
    a = nt.split(" ")[0]
    b = nt.split(" ")[1]
    f.close()

    tmp = fib(int(a),int(b))
    tmp = str(tmp)
    print(tmp)
    
    ff = open("out.txt","w")
    ff.write(tmp)
    ff.close()

#print(fib(33, 5))
