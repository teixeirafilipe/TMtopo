#! /usr/bin/env python3

# MIT License
#
#Copyright 2021 Filipe Teixeira
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# directory containing TMtopo data
tm_dir = '../data'

import numpy as np

tm_metals=['Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn']
# Collect data

with open(f"{tm_dir}/tmtopo.idx",'r') as f:
    idx = f.readlines()

for metal in tm_metals:
    for line in idx:
        l=line.split(',')
        if  l[4].strip()==metal:
            qm = np.nan
            dipole = np.nan
            oxst = -1
            g1 = -1
            g2 = -1
            i_count = -1
            data = open(f"{tm_dir}/{l[1].strip()}").readlines()
            for i,dline in enumerate(data):
                if dline[:4]=='F019': dipole = float(dline.split('::')[-1])
                if dline[:4]=='F100': qm = float(data[i+1].split()[-1])
                if dline[:4]=='F004': oxst = int(dline.split('::')[-1])
                if dline[:4]=='F251': i_count = int(dline.split('::')[-1])
                if dline[:4]=='F253': g1 = float(dline.split('::')[-1])
                if dline[:4]=='F254': g2 = float(dline.split('::')[-1])
                # ivscc radius is F250
            if all([g1 >= 0, g2 >=0, oxst>=0, not np.isnan(qm), not np.isnan(dipole)]):
                if i_count < 10:
                    print(qm, dipole, oxst,i_count, g1, g2, metal, sep=' ;')
    #print('')
    #print('')

