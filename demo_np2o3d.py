import open3d as o3d
import numpy as np

if __name__ == '__main__':
    points = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
    colors = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.colors = o3d.utility.Vector3dVector(colors)

    o3d.visualization.draw_geometries([pcd])

