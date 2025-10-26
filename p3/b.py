import pygame as a
a.init()
scre=a.display.set_mode((640,480))
font=a.font.Font(None,36)
txsf=font.render("OK",1,[255]*3)
scre.blit(txsf,[0]*2)
a.display.flip()
a.time.wait(3000)