import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# define a list of markevery cases to plot
cases = [None,
         8,
         (30, 8),
         [16, 24, 30], [0, -1],
         slice(100, 200, 3),
         0.1, 0.3, 1.5,
         (0.0, 0.1), (0.45, 0.1)]

# define the figure size and grid layout properties
figsize = (10, 8)
cols = 3
rows = len(cases) // cols + 1
# define the data for cartesian plots
delta = 0.11
x = np.linspace(0, 10 - 2 * delta, 200) + delta
y = np.sin(x) + 1.0 + delta

fig = plt.figure()
def trim_axs(axs, N):
    """
    Reduce *axs* to *N* Axes. All further Axes are removed from the figure.
    """
    axs = axs.flat
    for ax in axs[N:]:
        ax.remove()
    return axs[:N]

axs = plt.figure(figsize=figsize, constrained_layout=True).subplots(rows, cols)
axs = trim_axs(axs, len(cases))
for ax, case in zip(axs, cases):
    ax.set_title('markevery=%s' % str(case))
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=case)



plt.savefig('joke.png')