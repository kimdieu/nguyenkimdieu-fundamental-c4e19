import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

# 1. Prepare data
labels = ["iOs", "Android", "Web", "React Native"]
values = [15, 15, 40, 30]
colors = ['coral', 'red', 'pink', 'gold']
explode = [0, 0, 0, 0.2]


# 2. Plot
pyplot.pie(values, labels= labels, 
                    colors= colors,
                    explode=explode)
pyplot.axis("equal")

# 3. Show
pyplot.show()
