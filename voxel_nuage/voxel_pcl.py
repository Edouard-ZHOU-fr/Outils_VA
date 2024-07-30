import open3d as o3d
import os
import numpy as np
from pyntcloud import PyntCloud
from pandas import DataFrame
# fonction：filtrage voxélisé
# input：
#     point_cloud：Nuage de point entree
#     leaf_size: taille de voxel 



def load_pcd(file_path):
    pointcloud = o3d.io.read_point_cloud(file_path)
    pointcloud = np.asarray(pointcloud.points)
    return pointcloud


def save_pointcloud(pointcloud_np, file_name="pointcloud.pcd"):
    point_cloud_o3d = o3d.geometry.PointCloud()
    point_cloud_o3d.points = o3d.utility.Vector3dVector(pointcloud_np[:, 0:3])
    o3d.io.write_point_cloud(file_name, point_cloud_o3d, write_ascii=False, compressed=True)


def voxel_filter(point_cloud, leaf_size, random=False):
    filtered_points = []
    # calculer les points de bords
    x_min, y_min, z_min = np.amin(point_cloud, axis=0)      #x y z maximum
    x_max, y_max, z_max = np.amax(point_cloud, axis=0)
 
    # calculer voxel grid
    Dx = (x_max - x_min)//leaf_size + 1
    Dy = (y_max - y_min)//leaf_size + 1
    Dz = (z_max - z_min)//leaf_size + 1
    print("Dx x Dy x Dz is {} x {} x {}".format(Dx, Dy, Dz))
 
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
 
def main():




####################################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####################################
    

    # charger le  fichier de nuage de points 
    pcd1 = "maps_mgrs0.pcd"
    tailleDeEchantillonage = 0.5    # 0~infini, le numéro plus grands la taille plus petite (unité mètre de chaque Cube); 


####################################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####################################






    
    nuage_de_point1 = load_pcd(pcd1)

    print(len(nuage_de_point1))
    nuage_de_point_redui1 = voxel_filter(nuage_de_point1, 0.5, random=True)
    print(len(nuage_de_point_redui1))


    save_pointcloud(nuage_de_point_redui1,("redui"+pcd1))



    # ##################### Visualisation ###################################
    # nuage_de_point_redui1 = nuage_de_point_redui1[:, :3]
    # point_cloud_o3d = o3d.geometry.PointCloud()
    # point_cloud_o3d.points = o3d.utility.Vector3dVector(nuage_de_point_redui1)
    # o3d.visualization.draw_geometries([point_cloud_o3d])



 
if __name__ == '__main__':
    main()
