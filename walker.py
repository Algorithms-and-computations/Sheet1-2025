import numpy as np
import random as rand

tasks = ["Mark student's problem sheets",
         "Solve the problem sheet",
         "Get locked out of my office",
         "Supervisor meeting"]

weights = [5,
           3,
           20,
           2.5]

# Normalise the weights
weights = np.array(weights)
weights = weights / np.sum(weights) * len(weights)
print("Initial weights:")
print(weights)

shorts = {}
talls = {}

# Sort the originals into shorts/talls
# ID counts 0, 1, 2, ...
for ID, weight in enumerate(weights):
    if weight < 1:
        shorts[ID] = weight
    else:
        talls[ID] = weight


# List of tuples. Each tuple is:
# (ID of first, weight of first, then ID of second)
table = []

while len(shorts) >= 1 and len(talls) >= 1:
    # Grab a short and a long
    short_ID, short_weight = shorts.popitem()
    tall_ID = next(iter(talls))

    table.append((short_ID, short_weight, tall_ID))

    new_tall_height = talls[tall_ID] - (1 - short_weight)

    if new_tall_height > 1:
        # Modify old height
        talls[tall_ID] = new_tall_height
    else:
        # It became small. Remove it from talls, put in shorts.
        talls.pop(tall_ID)

        # You never have to worry about tall_ID already being in small.
        shorts[tall_ID] = new_tall_height

# The last one is either in shorts or talls... just place it
# (Might want to use np.isclose if we have multiple sticks close to the average line)
while len(shorts) >= 1:
    ID, height = shorts.popitem()
    table.append((ID, height, -1))
while len(talls) >= 1:
    ID, height = talls.popitem()
    table.append((ID, height, -1))

print("Table:")
print(table)




def get_sample():
    n = rand.randint(0, len(table)-1)

    short_ID, short_height, tall_ID = table[n]

    # zero to one
    r = rand.random()

    if r < short_height:
        return tasks[short_ID]

    return tasks[tall_ID]


for _ in range(10):
    print(f"Sampled '{get_sample()}'")
