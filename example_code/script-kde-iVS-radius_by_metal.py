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

#TMtopo data directory
tm_dir = '../data'

import numpy as np
import scipy.stats as stats

tm_metals=['Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn']
# Collect data
with open(f"{tm_dir}/tmtopo.idx",'r') as f:
    idx = f.readlines()[1:]

raw_data = {x:list() for x in tm_metals}

for line in idx:
    metal = 'UNK'
    rad = -1
    for dline in open(f"{tm_dir}/{line.split(',')[1].strip()}",'r'):
        if 'F003' in dline: metal = dline.split('::')[-1].strip()
        if 'F250' in dline: rad = float(dline.split('::')[-1])
    if rad >= 0:
        raw_data[metal].append(rad)
        
r_min = min(min(raw_data[k]) for k in raw_data.keys()) 
r_max = max(max(raw_data[k]) for k in raw_data.keys()) 
rad_range = r_max - r_min
r_min = r_min - 0.1*rad_range
r_max = r_max + 0.1*rad_range

npoints = 256
r = np.linspace(r_min, r_max, npoints)

table = dict()
for metal in tm_metals:
    table[metal] = stats.gaussian_kde(raw_data[metal]).pdf(r)

s = 'Metal'
for metal in tm_metals:
    s += f"; {metal}"
print(s)

for i in range(npoints):
    s = f"{r[i]:6.4f}"
    for metal in tm_metals:
        s += f"; {table[metal][i]:10.5e}"
    print(s)
