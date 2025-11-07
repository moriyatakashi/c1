import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# 正二十面体の頂点
phi = (1 + math.sqrt(5)) / 2
vertices = [
    [-1,  phi, 0], [1,  phi, 0], [-1, -phi, 0], [1, -phi, 0],
    [0, -1,  phi], [0, 1,  phi], [0, -1, -phi], [0, 1, -phi],
    [ phi, 0, -1], [ phi, 0, 1], [-phi, 0, -1], [-phi, 0, 1]
]
norm = math.sqrt(1 + phi**2)
vertices = [[x / norm, y / norm, z / norm] for x, y, z in vertices]

faces = [
    [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
    [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
    [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
    [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1]
]

# エッジ（辺）を定義
edges = set()
for face in faces:
    for i in range(len(face)):
        edge = tuple(sorted((face[i], face[(i + 1) % len(face)])))
        edges.add(edge)

def drawIcosahedron():
    # 面を描画
    glBegin(GL_TRIANGLES)
    for face in faces:
        for idx in face:
            glVertex3fv(vertices[idx])
    glEnd()

    # エッジを描画
    glColor3f(0.0, 0.0, 0.0)  # 黒い線
    glBegin(GL_LINES)
    for edge in edges:
        for idx in edge:
            glVertex3fv(vertices[idx])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glEnable(GL_DEPTH_TEST)

    angle = 0
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(angle, 1, 1, 0)
        glColor3f(0.4, 0.7, 1.0)  # 面の色
        drawIcosahedron()
        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)
        angle += 1

    pygame.quit()

if __name__ == "__main__":
    main()