from epidemic import *
import matplotlib.pyplot as plt

for v in [1, 0.7, 0.5, 0.3]:

    time, sick, healthy, recovered, deads = \
        calculate_epidemic(3, v, 200)
    plt.figure(1)
    p1 = plt.plot(time, sick, label=r"$v = $"+str(v))
    plt.figure(2)
    p2 = plt.plot(time, deads, label=r"$v = $"+str(v))
    plt.figure(3)
    plt.plot(time, recovered, label=r"$v = $"+str(v))
plt.figure(1)
plt.xlabel("Time")
plt.ylabel("Number of sick people")
plt.xticks([])
plt.yticks([])
plt.legend(loc='upper right')
plt.figure(2)
plt.yticks([])
plt.xticks([])
plt.xlabel("Time")
plt.ylabel("Number of dead people")
plt.legend()
plt.figure(3)
plt.yticks([])
plt.xticks([])
plt.xlabel("Time")
plt.ylabel("Number of recovered people")
plt.legend()
plt.show()
