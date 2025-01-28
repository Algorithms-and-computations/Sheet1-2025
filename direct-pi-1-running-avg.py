import random
from matplotlib.lines import lineStyles
import numpy as np
import matplotlib.pyplot as plt

N = 1000


def calculate_pi(N):
    hits = 0

    running_avg = 0
    running_avgs = []

    for i in range(N):
        x = random.random()  # Between 0.0 and 1.0
        y = random.random()  # Between 0.0 and 1.0

        throw = 0
        if x**2 + y**2 < 1:
            hits += 4
            throw = 4

        running_sum = running_avg * i + throw
        running_avg = running_sum / (i + 1)
        running_avgs.append(running_avg)

    return hits / N, running_avgs


pi, running_avgs = calculate_pi(N)
print(pi)
print(running_avgs)

plt.plot(running_avgs)
plt.axhline(y=np.pi, color='black', linestyle='--')
plt.xlabel("Number of throws")
plt.ylabel("Estimate of pi")
plt.show()
