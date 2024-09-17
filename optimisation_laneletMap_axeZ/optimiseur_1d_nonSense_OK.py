import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np



def MedianAverage(inputs,per):
	if np.shape(inputs)[0] % per != 0:
		lengh = np.shape(inputs)[0] / per
		for x in range(int(np.shape(inputs)[0]),int(lengh + 1)*per):
			inputs = np.append(inputs,inputs[np.shape(inputs)[0]-1])
	inputs = inputs.reshape((-1,per))
	mean = []
	for tmp in inputs:
		tmp = np.delete(tmp,np.where(tmp==tmp.max())[0],axis = 0)
		tmp = np.delete(tmp,np.where(tmp==tmp.min())[0],axis = 0)
		mean.append(tmp.mean())
	return mean

def SlidingAverage(inputs,per):
	if np.shape(inputs)[0] % per != 0:
		lengh = np.shape(inputs)[0] / per
		for x in range(int(np.shape(inputs)[0]),int(lengh + 1)*per):
			inputs = np.append(inputs,inputs[np.shape(inputs)[0]-1])
	inputs = inputs.reshape((-1,per))
	tmpmean = inputs[0].mean()
	mean = []
	for tmp in inputs:
		mean.append((tmpmean+tmp.mean())/2)
		tmpmean = tmp.mean()
	return mean


def AmplitudeLimitingShakeOff(inputs,Amplitude,N):
	#print(inputs)
	tmpnum = inputs[0]
	for index,newtmp in enumerate(inputs):
		if np.abs(tmpnum-newtmp) > Amplitude:
			inputs[index] = tmpnum
		tmpnum = newtmp
	#print(inputs)
	usenum = inputs[0]
	i = 0
	for index2,tmp2 in enumerate(inputs):
		if tmp2 != usenum:
			i = i + 1
			if i >= N:
				i = 0
				inputs[index2] = usenum
	#print(inputs)
	return inputs

def convolution_1d_padding(input,kernel=20,mode="full"):
    entree = input[:]
    print("entree",len(input))

    filtre,_  = filtre_1d(kernel)
    for i in range(kernel):
        entree.insert(0,entree[0])
        entree.append(entree[-1])
    sortie = np.convolve(entree,filtre,mode)
    # sortie = sortie[:(-(kernel-1))]
    sortie = sortie[(kernel):-((2*kernel-1))]
    # sortie = sortie[(kernel//2):(-(kernel//2-1))]

    print("sortie",len(sortie))
    return sortie

def convolution_1d_s(input,kernel=20,mode="same"):
    entree = input[:]
    print("entree",len(input))
    filtre,_  = filtre_1d(kernel)
    sortie = np.convolve(entree,filtre,mode)
	
    print("sortie",len(sortie))
    return sortie
	
	


def filtre_1d(n):
    return np.ones(n)*(1/n) , n
	


# 读取文件
domTree = ET.parse("mobauto_lanelet2_maps_v0.18.5.osm")
# domTree = ET.parse("lanelet2_maps_la_post_V21.osm")


# 获得所有节点的内容
root = domTree.getroot()


iDlist = []
zlist = []

# 逐个检查node
nodes = root.findall("node")
# tags = root.findall("tag")

for node in nodes:
    iD = node.get("id")
    iD = int(iD)
    iDlist.append(iD)

    axeZ = node[3].get("v")
    axeZ = float(axeZ)
    zlist.append(axeZ)

    # print(axeZ)


print(len(iDlist))
print(len(zlist))
print(iDlist[-1])
print(zlist[-1])





print("####################")
z_list = []
# z_list = AmplitudeLimitingShakeOff(zlist,150,20)

z_list = convolution_1d_padding(zlist,kernel=50)
# z_list = convolution_1d_s(zlist,kernel=10)

x_x = range(1,len(z_list)+1)
print(iDlist[-1])
print(z_list[-1])


print("####################")

dico_id_z = {}
for i in range(len(iDlist)):
    dico_id_z[iDlist[i]] = z_list[i]
# print(dico_id_z)    



for node in nodes:
    iD_r = node.get("id")
    iD_r = int(iD_r)

    node[2].set("v", str(dico_id_z[iD_r])  )
    
domTree.write("out.osm",encoding="utf8")



# x = np.array(id_list)
x = np.array(iDlist)
x1 = np.array(iDlist)


plt.xlabel("ID",fontdict={'size': 16})

y = np.array( zlist )
y1 = np.array( z_list )


plt.ylabel("Z",fontdict={'size': 16})

plt.title("hauteur_de_chaque_points",fontdict={'size': 16})

# plt.axis('off')
# plt.gca().axis('off')
plt.xticks([])
plt.yticks([])
plt.subplot(2,1,1)
plt.plot(x, y, color = 'r')


plt.subplot(2,1,2)
plt.plot(x1, y1, color = 'g')


plt.show()






 
