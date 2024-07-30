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

def load_pcd(file_path):
    pointcloud = o3d.io.read_point_cloud(file_path)
    pointcloud = np.asarray(pointcloud.points)
    return pointcloud


def save_pointcloud(pointcloud_np, file_name="pointcloud.pcd"):
    point_cloud_o3d = o3d.geometry.PointCloud()
    point_cloud_o3d.points = o3d.utility.Vector3dVector(pointcloud_np[:, 0:3])
    o3d.io.write_point_cloud(file_name, point_cloud_o3d, write_ascii=False, compressed=True)

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


def voxel_filter(point_cloud, leaf_size, random=False):
    filtered_points = []
    # calculer les points de bords
    x_min, y_min, z_min = np.amin(point_cloud, axis=0)      #x y z maximum
    x_max, y_max, z_max = np.amax(point_cloud, axis=0)
 
    # calculer voxel grid
    Dx = (x_max - x_min)//leaf_size + 1
    Dy = (y_max - y_min)//leaf_size + 1
    Dz = (z_max - z_min)//leaf_size + 1
    # print("Dx x Dy x Dz is {} x {} x {}".format(Dx, Dy, Dz))


    print_c("--En train de sous échantilloner le nuage de points...")


 
    # calculer l'ordre de chaque point 3D 
    h = list()  #h creation une liste pour chaque l'ordre de point 3D
    for i in range(len(point_cloud)):
        hx = (point_cloud[i][0] - x_min)//leaf_size
        hy = (point_cloud[i][1] - y_min)//leaf_size
        hz = (point_cloud[i][2] - z_min)//leaf_size
        h.append(hx + hy*Dx + hz*Dx*Dy)
    h = np.array(h)
 
    # sélectionner les points 3D
    h_indice = np.argsort(h) # mise en ordre les points 3D de mode croissant
    h_sorted = h[h_indice]
    begin = 0
    for i in range(len(h_sorted)-1):   # 0~9999
        if h_sorted[i] == h_sorted[i + 1]:
            continue
        else:
            point_idx = h_indice[begin: i + 1]
            filtered_points.append(np.mean(point_cloud[point_idx], axis=0))
            begin = i+1
 
    # type: nuage de point 2 array
    filtered_points = np.array(filtered_points, dtype=np.float64)

    
    return filtered_points


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



    nuage_de_point1 = load_pcd(pcd1)
    # print(len(nuage_de_point1))
    nuage_de_point_redui1 = voxel_filter(nuage_de_point1, leaf_size, random=True)
    # print(len(nuage_de_point_redui1))

    save_pointcloud(nuage_de_point_redui1,(output+"redui.pcd"))

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


        nuage_de_point1 = load_pcd(pcd_ancienne[i])  
        nuage_de_point_redui1 = voxel_filter(nuage_de_point1, leaf_size, random=True) 
        save_pointcloud(nuage_de_point_redui1,(output+"redui"+str(i)+".pcd"))

        print("*********** Reussi le "+str(i+1)+"ème nuage de points ***********\n")
    os.system("clear")
    print_reussi("Terminer tous les traitements de nuage de points "+str(len(pcd_ancienne))+" réussi!!!")
    
    
end = time.time()

print("Temps d'éxecusion: "+str(end-start)+" s\n")
