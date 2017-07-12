import random
from random import randint
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

num_friend = [random.randint(0, 100) for _ in range(50000)]

friend_counts = Counter(num_friend)

xs = np.linspace(10, 100, num = 91)
ys = [friend_counts[x]/50000 for x in xs]
plt.bar(xs, ys, align = 'center')
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()