import pygame as a
a.init()
a.display.set_mode((640,480)).blit(a.font.Font(None,36).render("OK",1,[255]*3),[10]*2)
a.display.flip()
a.time.wait(3000)