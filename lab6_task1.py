import matplotlib.pyplot as plt

x = [1, 5, 5, 1, 1] 
y = [1, 1, 5, 5, 1]

plt.plot(x, y, color = 'y', label = 'Graf task 1', marker = 'o', ms = 5)
plt.savefig('fig_task1.png')