import subprocess, signal
import os
import time



def main():

    time_s = 1
    n_bag = 30
    nm_bag = 5
    n_pcd = 3000
    n_pc = n_pcd
    duration = 5
    rviz = "roslaunch hdl_graph_slam hdl_graph_slam_floam.launch enable_gps:=true gnss_topic:=/fixposition/converter/gpsfix"


    drapeau = True

    r_pc = "/media/milla/datalogger/YeloDeta/rosbag2_2024_05_02-14_15_37/les_nuages_de_points/testDeBag30/"
    r_rosbag = "/media/milla/datalogger/YeloDeta/rosbag2_2024_05_02-14_15_37/ROS1BAG/"





    rosbag = f"rosbag play "+r_rosbag+f"output_ros{n_bag}.bag -s {time_s} --clock -r 0.1 /tf:=/tf_old"



    enregistement2 = f"rosservice call /hdl_graph_slam/save_map \"utm: false \nresolution: 0.0 \ndestination: \'"+r_pc+f"maps{n_pc}.pcd\'\" "
    conertissement2 = f"roslaunch utils pcd_utm2mgrs.launch map_name:=\"maps{n_pc}\" map_path:=\""+r_pc+"\" zone:=\"30TXS\" utm_file_path:=\""+r_pc+f"maps{n_pc}.pcd.utm\""
    clear1 = f"rm "+r_pc+f"maps{n_pc}.pcd"
    clear2 = f"rm "+r_pc+f"maps{n_pc}.pcd.utm"



    string = "iteration= 0	 chi2= 0.167263	 time= 0.000213582	 cumTime= 0.000213582	 edges= 10	 schur= 0	 lambda= 0.000218	 levenbergIter= 1"
    print(string[int(string.find("="))+2])
    
    # print(rosbag)
    # print(conertissement2)


    status = os.stat("/home/hongyu/python_ws/postTaitement/subprocesse.py")
    print(type(status.st_size))



    # domTree.write("out.osm",encoding="utf8")
 
if __name__=="__main__":
    main()
    pass
