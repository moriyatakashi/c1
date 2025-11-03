from vpython import *

# 地球のテクスチャ画像（例: NASA Blue Marbleの画像URL）
earth_texture = "https://eoimages.gsfc.nasa.gov/images/imagerecords/57000/57730/land_ocean_ice_2048.jpg"

# 地球儀の描画
earth = sphere(radius=1, texture=earth_texture)