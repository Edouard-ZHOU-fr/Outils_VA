import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
 
def main():
    # 读取文件
    domTree = ET.parse("mobauto_lanelet2_maps_v0.18.5.osm")
 
    # 获得所有节点的内容
    root = domTree.getroot()

 
    # 存储不在所选区域内的node ID
    iDlist = []
    zlist = []

 
    # 逐个检查node
    nodes = root.findall("node")
    # tags = root.findall("tag")

    for node in nodes:
        iD = node.get("id")
        iDlist.append(iD)

        axeZ = node[3].get("v")
        zlist.append(axeZ)
        # print(axeZ)
    


    # iDlist = iDlist[:500]
    # zlist = zlist[:500]


    print(len(iDlist))
    print(len(zlist))

    x_x = range(1,len(zlist)+1)
    print(len(x_x))


    print(zlist[2])


    print("####################")
    for i in range(0,len(iDlist)):
        print ( [i])
        pass
    print("####################")



    x = np.array(iDlist)
    plt.xlabel("ID",fontdict={'size': 16})

    y = np.array(zlist)
    plt.ylabel("Z",fontdict={'size': 16})

    plt.title("hauteur_de_chaque_points",fontdict={'size': 16})

    # plt.axis('off')
    # plt.gca().axis('off')
    plt.xticks([])
    plt.yticks([])

    plt.plot(x, y, color = 'r')
    # plt.scatter(x, y, color = 'r')

    
    plt.show()






    # domTree.write("out.osm",encoding="utf8")
 
if __name__=="__main__":
    main()