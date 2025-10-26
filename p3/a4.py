import pygame as a
a.init()
sc=a.display.set_mode((640,480))
ft=a.font.Font(None,36)
ts=ft.render("OK",1,[255]*3)
sc.blit(ts,[0]*2)
a.display.flip()
a.time.wait(3000)