import pygame as a
a.init()
sc = a.display.set_mode((640, 480))
ft = a.font.Font(None, 36)
ts = ft.render("OK", 1, [255]*3)
ps = [(320, 100), (270, 200), (370, 200)]
a.draw.polygon(sc, (0, 0, 255), ps)
sc.blit(ts, [0]*2)
a.display.flip()
a.time.wait(10000)