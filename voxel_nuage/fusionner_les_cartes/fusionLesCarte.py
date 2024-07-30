import os,sys,shutil
import open3d as o3d
import numpy as np
from pyntcloud import PyntCloud
from pandas import DataFrame
import time
# fonction：filtrage voxélisé
# input：
#     point_cloud：Nuage de point entree
#     leaf_size: taille de voxel 



pcd_ancienne = []



def fusion_les_cartes(pointCloud1,pointCloud2):



    return (pointCloud1+pointCloud2)


def print_c(clignotant):
    clignotant = str(clignotant)
    # os.system("clear")
    print("\033[5;34;42m"+clignotant+"\033[0m", end='\r')
    pass


def print_reussi(reussi):
    reussi = str(reussi)
    # os.system("clear")
    print("\033[1;32;47m"+reussi+"\033[0m")
    pass



def recursive_listdir(path):

    files = os.listdir(path)
    # pcd_ancienne = []
    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            # print(file)
            # print(file_path)
            pcd_ancienne.append(file_path)
            pass


        elif os.path.isdir(file_path):
          recursive_listdir(file_path)


    return pcd_ancienne


os.system("clear")
path=input('Saisir le repertoire origine (avec/ à la fin): ')  



output = input("répertoire sauvgarder (avec '.pcd' à la fin): ")  

print("\n\n")



start = time.time()


if os.path.isdir(path):
    print("Entrée est une répertoire(un dossier)")
    print_c("Commencer de parcourir le dossier......")




    pcd_ancienne=recursive_listdir(path)
    # print("1111111111111")
    # print(len(pcd_ancienne))

    n=0
    pointCloudAll = o3d.io.read_point_cloud(pcd_ancienne[0])
    for i in range(len(pcd_ancienne)):
        pointCloud = o3d.io.read_point_cloud(pcd_ancienne[i])
        pointCloudAll += pointCloud


    o3d.io.write_point_cloud(output, pointCloudAll, write_ascii=False, compressed=False,print_progress=True)
    print_reussi("Terminer les fusions de nuage de points "+str(len(pcd_ancienne))+" réussi!!!")
    
else:
    print("C'est pas une répertoire, veuillez saisir une répertoire !!!")
    pass   
end = time.time()

print("Temps d'éxecusion: "+str(end-start)+" s\n")
