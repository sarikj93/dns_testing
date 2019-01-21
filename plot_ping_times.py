#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from glob import glob

ping_files = sorted(glob('pingtest*.txt'))

plt.figure()

for file in ping_files:
    label = file.strip('pingtest').strip('.txt')
    info = np.genfromtxt(file, skip_header=1, usecols=(6,), dtype=str)
    times = []
    for i in range(len(info)):
        times.append(float(info[i].split('=')[-1]))
    plt.plot(range(1, len(times)+1), times, label=label)

plt.title('DNS Server Ping Times')
plt.xlabel('Data Point')
plt.ylabel('Ping Time (ms)')
plt.legend()
plt.show()
