import open3d as o3d

if __name__ == '__main__':
    mesh_filepath = "mesh1.obj"
    pcd_filepath = "pcd2.ply"

    mesh = o3d.io.read_triangle_mesh(mesh_filepath)
    pcd = o3d.io.read_point_cloud(pcd_filepath)

    mesh.paint_uniform_color((0.7, 0.3, 0.3))
    pcd.paint_uniform_color((0.3, 0.7, 0.3))

    o3d.visualization.draw_geometries([mesh, pcd], mesh_show_wireframe=True, mesh_show_back_face=True)

