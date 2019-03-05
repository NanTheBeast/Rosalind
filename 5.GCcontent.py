#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @IDE: PyCharm
# @date: Mar-5-2019 8:15 AM
# @author: nhu


"""
Usage   Python3 5.GCcontent.py -h for help.
        Python3 5.GCcontent.py -f for filename.
        The result is the the percentage of its bases that are either cytosine or guanine..
"""


import argparse

def GCcontent(nt):
    nt=nt.upper()
    GC=0
    for i in nt:
        if i=="G" or i=="C":
            GC+=1
    percent=GC/len(nt)
    return percent

def compareGC(dict):
    maxpercent=list(dict.values())
    for id, percent in dict.items():
        if percent == maxpercent:
            print(id,"\n",percent)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", type=str, help= "input filename")
    args = parser.parse_args()

    file = args.filename if args.filename is not None else input("input a filename:")

    with open(file, "r") as fin:
        seq_dict = {"id": [], "seq": [], "percentage": []}
        seq = ""
        for line in fin:
            if line[0] == ">":
                if seq != "":
                    seq_dict["seq"] += [seq]
                    seq_dict["percentage"] += GCcontent(seq)
                    seq = ""
                    pri_dict["PriID"] += [priID]
                priID = pri_re.search(line).group(1)
            else:
                seq += line.strip("\n")
        # add last lines
        seq_dict["seq"] += [seq]
        seq_dict["percentage"] +=

    tmp = fib(int(a),int(b))
    tmp = str(tmp)
    print(tmp)

    # ff = open("out.txt","w")
    # ff.write(tmp)
    # ff.close()

#print(fib(33, 5))
