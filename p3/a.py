import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

# 黄金比
phi = (1 + np.sqrt(5)) / 2

# 頂点定義（正規化）
vertices = np.array([
    [-1,  phi, 0], [1,  phi, 0], [-1, -phi, 0], [1, -phi, 0],
    [0, -1,  phi], [0, 1,  phi], [0, -1, -phi], [0, 1, -phi],
    [ phi, 0, -1], [ phi, 0, 1], [-phi, 0, -1], [-phi, 0, 1]
])
vertices /= np.linalg.norm(vertices[0])  # 単位球に正規化

# 面定義（頂点インデックス）
faces = [
    [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
    [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
    [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
    [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1]
]

# 描画設定
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, 1])

# アニメーション更新関数
def update(frame):
    ax.cla()
    ax.set_box_aspect([1, 1, 1])
    ax.view_init(elev=30, azim=frame)
    poly3d = [[vertices[i] for i in face] for face in faces]
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors='skyblue', edgecolors='k', linewidths=1, alpha=0.9))
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])
    ax.axis('off')

# アニメーション作成
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)

# GIFとして保存（必要なら）
ani.save("icosahedron_rotation.gif", writer="pillow")

plt.show()