import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

vertices = np.array([
    [0, 0, 0], 
    [1, 0, 0], 
    [0.5, 0.866, 0],
    [0.5, 0.288, 0.816]
])

faces = [
    [vertices[0], vertices[1], vertices[2]],  
    [vertices[0], vertices[1], vertices[3]],  
    [vertices[1], vertices[2], vertices[3]],  
    [vertices[2], vertices[0], vertices[3]]   
]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

poly3d = Poly3DCollection(faces, alpha=0.5, edgecolor='k')
ax.add_collection3d(poly3d)

z_plane = 0.2
x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
x, y = np.meshgrid(x, y)
z = np.full_like(x, z_plane)
ax.plot_surface(x, y, z, alpha=0.3, color='red')

ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

def tetrahedron_volume(v1, v2, v3, v4):
    matrix = np.array([v2 - v1, v3 - v1, v4 - v1])
    return abs(np.linalg.det(matrix)) / 6

above = []
below = []
for vertex in vertices:
    if vertex[2] > z_plane:
        above.append(vertex)
    else:
        below.append(vertex)

if len(above) == 4:
    volume = tetrahedron_volume(*vertices)
    print(f"All vertices are above the plane. Volume above the plane: {volume}")
elif len(above) == 0:
    print("No vertices are above the plane. Volume above the plane: 0")
else:
    new_vertices = []
    for v1 in above:
        for v2 in below:
            t = (z_plane - v2[2]) / (v1[2] - v2[2])
            new_vertex = v2 + t * (v1 - v2)
            new_vertices.append(new_vertex)
    
    pyramid_base = new_vertices
    pyramid_tip = above[0]  

    pyramid_volume = 0
    for i in range(len(pyramid_base)):
        v1 = pyramid_base[i]
        v2 = pyramid_base[(i + 1) % len(pyramid_base)]
        v3 = pyramid_tip
        pyramid_volume += tetrahedron_volume(np.array([0, 0, z_plane]), v1, v2, v3)

    print(f"Volume above the plane: {pyramid_volume}")

# plt.savefig('tetrahedron_with_plane.png')
plt.show()