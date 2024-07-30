À cause de la taille de nuage de point est très large, le pointCloud ne peut pas bien chargé quand nous avons lancé le simulateur(c'est égalment pas efficase de chercher notre carton car le bouton ZERO ne fonnction pas dans cette situation ), ce script est donc crée pour reduire la taille de nuage de points;



Comment utiliser?

assurer tu as bien installée open3d:
pip install open3d

changer le  répertoire de nuage de point que t'as besoin, et puis exécute le script, il peut génerer un fichier de PointCloud automatiquement qui s'appelle "redui_<nom de ton fichier>.pcd"

au fait la visualisation par python ralentie beaucoup le temp d'éxecution, tu peut commenter cette partie qui est à la fin du programme.
