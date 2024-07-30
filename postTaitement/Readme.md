/!\ C'est le Code pour simplifier un peu le Post taitement, il faudrait encore une verification manuelle quand vous tracez le carto;

Ce Code est juste remplacer le partie de lancement de Rviz et enregistement, donc, nous devons lancer les autre partie suvie la commande de Post taitement : roscore, frame.launch, fusionnode,etc.
et aussi, nous devons sourcer les  ROS d'abord dans un nouveau terminal avant de lancer ce Code.

EX:
"
noetic
rosparam set use_sim_time true
"
pour bien sauvgarder le fichier pcd, veuillez modifier le répertoire de ROS1 bag et l'endroit d'enregistement dans le script; Il se trouve dans la zone suivant :


def main():
#####################################################################################################################################################

    time_s = 0
    n_bag = 10
    nm_bag = 10
    n_pcd = 1000
    n_pc = n_pcd
    duration = 5
    r_pc = "/media/milla/datalogger/YeloDeta/rosbag2_2024_05_02-14_15_37/les_nuages_de_points/testDeBag10/"
    r_rosbag = "/media/milla/datalogger/YeloDeta/rosbag2_2024_05_02-14_15_37/ROS1BAG/"


#####################################################################################################################################################



"""

time_s :    pour chaque rosbag le temps que il commence.
n_bag :     numero de premiere rosbag que vous voulez commencer
nm_bag :    nombre de rosbag
n_pcd :     numero de rosbag que vous voulez commencer
duration :  Duration de chaque enregistement (il propose de mieux superieur 3s de Rostime)
r_pc :      répertoire de fichier Pointcloud(.pcd) que vous voulez enregistrer
r_rosbag :  Répertoire où les rosbags se trouvent. 


"""

La duration de chaque rosbag est considéré au 300 seconds par défaut.
Petit conseil : À cause de la performance de PC, ne pas mettre nombre de rosbag plus de 10 une fois,(le lot de 10 chaque fois et puis pauser le PC quelque minuite et puis relancer les étapes au dessus)