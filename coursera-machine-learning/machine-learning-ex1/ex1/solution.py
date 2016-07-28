import csv
import matplotlib.pyplot as plt

reader = csv.reader(open("ex1data1.txt"))

print(reader)

x = []
y = []
for row in reader:
	x.append(row[0])
	y.append(row[1])

plt.plot(x, y, 'o')
plt.show()
