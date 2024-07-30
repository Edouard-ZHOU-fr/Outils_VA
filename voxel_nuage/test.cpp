#include<iostream>
#include<pcl/io/pcd_io.h>
#include<pcl/point_types.h>

#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/filters/voxel_grid.h>		
using namespace std;
 



int main (int argc, char** argv){
	// typedef pcl::PointXYZRGBA PointT;
	typedef pcl::PCLPointCloud2 PoinT;
	/////////////////// 	typedef pcl::PointCloud2 PoinT;		//////////
	pcl::PointCloud<PointT>::Ptr cloud1 (new pcl::PointCloud<PointT>);
	pcl::PointCloud<PointT>::Ptr cloud2 (new pcl::PointCloud<PointT>);
	pcl::PointCloud<PointT>::Ptr cloud3 (new pcl::PointCloud<PointT>);



	pcl::PCLPointCloud2::Ptr cloud(new pcl::PCLPointCloud2());
    pcl::PCLPointCloud2::Ptr cloud_filtered(new pcl::PCLPointCloud2());




                        

	
	std::string dir = "/home/wgb/Desktop/wgb_save_pic/color/";
	std::string filename1 = "0010_cloud.pcd";
	std::string filename2 = "0010_cloud.pcd";



	cloud1 = pcl::io::loadPCDFile<PointT> ((dir+filename1);
	cloud2 = pcl::io::loadPCDFile<PointT> ((dir+filename2);
    // pcl::PCDReader reader;	
    // // Replacer le racroucci de ce fichier pcd par la tiennes 
    // reader.read("./pcd/table_scene_lms400.pcd", *cloud); 



	cloud3 = cloud1;
	cloud3 +=cloud2;

	pcl::VoxelGrid<pcl::PCLPointCloud2> sor;	//creation VoxelGrid
    sor.setInputCloud(cloud3);					
    sor.setLeafSize(0.01f, 0.01f, 0.01f);		//taille de voxel，unité (m)，ex: 1cm cube
    sor.filter(*cloud_filtered);	



	pcl::visualization::PCLVisualizer viewer("Cloud viewer");
	viewer.setCameraPosition(0,0,-2,0,-1,0);
	//viewer.setCameraPosition(0,0,-3.0,0,-1,0);
	viewer.addCoordinateSystem(0.3);


	viewer.addPointCloud(cloud3);
	while(!viewer.wasStopped())
	viewer.spinOnce(100);



// enregistrer dans un nouveau fichgier.pcd
    pcl::PCDWriter writer;
    writer.write("table_scene_lms400_downsampled.pcd", *cloud_filtered,
        Eigen::Vector4f::Zero(), Eigen::Quaternionf::Identity(), false);

                        
}




