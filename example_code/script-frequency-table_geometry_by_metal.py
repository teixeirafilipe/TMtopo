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

# This variable must point to the directory containing TMtopo data
tm_dir = '../data'

tm_metals=['Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn']
ox_states=[1,2,3,4,5,6]

with open(f"{tm_dir}/tmtopo.idx",'r') as f:
    data=f.readlines()

# collect geometries:
geo_lst = list()
for line in data[1:]:
    l = [x.strip() for x in line.split(',')]
    if l[-1] not in geo_lst: geo_lst.append(l[-1])

geo_lst.sort(key=lambda x: x.upper())

# collect Table of frequencies from the index file

table = dict()
for m in tm_metals:
    for g in geo_lst:
        table[f"{m} {g}"]=0

for line in data[1:]:
    l = [x.strip() for x in line.split(',')]
    table[f"{l[4]} {l[-1]}"] += 1

s="Geometry "
for m in tm_metals:
    s += f"; {m}"
print(s)

for g in geo_lst:
    s=f"{g.title()}"
    for m in tm_metals:
        k=f"{m} {g}"
        s += f"; {table[k]}"
    print(s)
