
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()
'''rect1 = Rectangle((0.2, 0.2), width=1, height=1, edgecolor='blue', facecolor='lightblue')
rect2 = Rectangle((1.2, 1.2), width=0.4, height=0.4, edgecolor='red', facecolor='red')
rect4 = Rectangle((1.6, 1.6), width=0.01, height=0.01, edgecolor='orange', facecolor='orange')
rect5 = Rectangle((0.2, 0.2), width=1.41, height=1.41, edgecolor='blue', facecolor='none')
rect3 = Rectangle((0.2, 0.2), width=1.4, height=1.4, edgecolor='green',facecolor='none')
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)
ax.add_patch(rect4)
ax.add_patch(rect5)
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)'''
rect1 = Rectangle((0, 0), width=400, height=400, edgecolor='blue', facecolor='lightblue')
plt.text(350, 190, '}', fontsize=115, verticalalignment='center')
plt.text(350+200+10, 200, '400', fontsize=60, verticalalignment='center')
rect2 = Rectangle((400, 400), width=80, height=80, edgecolor='red', facecolor='red')
plt.text(480, 440, '}80', fontsize=21, verticalalignment='center')
'''rect4 = Rectangle((480, 480), width=30, height=30, edgecolor='orange', facecolor='orange')
ax.add_patch(rect4)'''
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)
ax.set_aspect('equal')
plt.grid(True)
plt.title('Rectangle')
plt.show()