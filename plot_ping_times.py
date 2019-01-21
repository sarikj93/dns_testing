#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from glob import glob

ping_files = sorted(glob('pingtest*.txt'))  # Get file names

plt.figure()

for file in ping_files:
    label = file.strip('pingtest').strip('.txt')  # Get labels for the data sets
    info = np.genfromtxt(file, skip_header=1, usecols=(6,), dtype=str)  # Extract the ping times from the text files
    times = np.array([], float)
    for i in range(len(info)):
        times = np.append(times, float(info[i].split('=')[-1]))
    times = times[times < 100]
    plt.bar(range(1, len(times)+1), times, label=label)
    print('Mean ping time for %s: %d +/- %d ms' % (label, np.mean(times), np.std(times)))

plt.title('DNS Server Ping Times')
plt.xlabel('Data Point')
plt.ylabel('Ping Time (ms)')
plt.legend()
plt.show()
