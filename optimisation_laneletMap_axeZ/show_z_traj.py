# import matplotlib.pyplot as plt
import numpy as np
import csv
import re
import matplotlib.pyplot as plt



 

inputFileName = "test.csv"

textFile = open(inputFileName, "r")
rawLines = textFile.readlines()
textFile.close()

z = []
x = []
for rawline in rawLines:

    line = re.split(',',rawline)


    # print(float(line[2]))
    try:
        print(float(line[2]))
        z.append(float(line[2]))
    except:
        pass
for i in range(len(z)):
    x.append(i)
    pass







x = np.array(x)
plt.xlabel("ID",fontdict={'size': 16})

y = np.array(z)
plt.ylabel("Z",fontdict={'size': 16})

plt.title("hauteur_de_chaque_points",fontdict={'size': 16})

# plt.axis('off')
# plt.gca().axis('off')
plt.xticks([])
plt.yticks([])

plt.plot(x, y, color = 'r')
# plt.scatter(x, y, color = 'r')


plt.show()




