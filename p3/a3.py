import pygame
import math
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Define 3D points of a tetrahedron (triangular pyramid)
vertices = [
    [0, 1, 0],     # Top vertex
    [-1, -1, -1],  # Base vertex 1
    [1, -1, -1],   # Base vertex 2
    [0, -1, 1]     # Base vertex 3
]

# Define faces using indices into the vertices list
faces = [
    (0, 1, 2),
    (0, 2, 3),
    (0, 3, 1),
    (1, 2, 3)
]

# Light direction for shading
light_dir = [0, 0, -1]

# Function to rotate a point around Y-axis
def rotate_y(point, angle):
    x, y, z = point
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    x_new = x * cos_theta - z * sin_theta
    z_new = x * sin_theta + z * cos_theta
    return [x_new, y, z_new]

# Function to project 3D point to 2D
def project(point):
    scale = 200
    x, y, z = point
    factor = scale / (z + 5)
    x_proj = int(320 + x * factor)
    y_proj = int(240 - y * factor)
    return (x_proj, y_proj)

# Function to compute normal vector of a face
def compute_normal(v0, v1, v2):
    ux, uy, uz = [v1[i] - v0[i] for i in range(3)]
    vx, vy, vz = [v2[i] - v0[i] for i in range(3)]
    nx = uy * vz - uz * vy
    ny = uz * vx - ux * vz
    nz = ux * vy - uy * vx
    length = math.sqrt(nx**2 + ny**2 + nz**2)
    return [nx / length, ny / length, nz / length]

# Function to compute dot product
def dot(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Rotate and project vertices
    rotated_vertices = [rotate_y(v, angle) for v in vertices]
    projected = [project(v) for v in rotated_vertices]

    # Draw faces with shading
    for face in faces:
        v0, v1, v2 = [rotated_vertices[i] for i in face]
        normal = compute_normal(v0, v1, v2)
        brightness = max(0, dot(normal, light_dir))
        color = [int(255 * brightness)] * 3
        points = [projected[i] for i in face]
        pygame.draw.polygon(screen, color, points)

    pygame.display.flip()
    angle += 0.02
    clock.tick(30)

pygame.quit()
sys.exit()