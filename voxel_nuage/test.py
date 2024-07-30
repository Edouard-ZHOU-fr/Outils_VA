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

leaf_size = float(input("Saisir le leaf size échantillonnage"))

output = input("répertoire sauvgarder (avec/ à la fin): ")  

print("\n\n")



start = time.time()

if os.path.isfile(path):
    print("Entrée est un fichier")
    pcd1 = path


    nuage_de_point = o3d.io.read_point_cloud(pcd1)
    print_c("--En train de sous échantilloner le nuage de points...")

    nuage_de_point_reduit = nuage_de_point.voxel_down_sample(voxel_size=leaf_size)
    o3d.io.write_point_cloud((output+"redui.pcd"), nuage_de_point_reduit, write_ascii=False, compressed=False)



    os.system("clear")

    print("Réussi de reduire la nuage de points!!!\n")



if os.path.isdir(path):
    print("Entrée est une répertoire(un dossier)")
    print("Commencer de parcourir le dossier......")




    pcd_ancienne=recursive_listdir(path)
    # print("1111111111111")
    # print(len(pcd_ancienne))

    n=0

    for i in range(len(pcd_ancienne)):


        print_c("--En train de sous échantilloner le nuage de points...")
        
        pointCloud = o3d.io.read_point_cloud(pcd_ancienne[i])
        pointCloud_reduit = pointCloud.voxel_down_sample(voxel_size=leaf_size)
        o3d.io.write_point_cloud((output+"redui"+str(i)+".pcd"), pointCloud_reduit, write_ascii=False, compressed=False)

        print("*********** Reussi le "+str(i+1)+"ème nuage de points ***********\n")

    os.system("clear")
    print_reussi("Terminer tous les traitements de nuage de points "+str(len(pcd_ancienne))+" réussi!!!")
    
    
end = time.time()

print("Temps d'éxecusion: "+str(end-start)+" s\n")
