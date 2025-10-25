import pygame as p
p.init()
s = p.display.set_mode(p.Rect(0, 0, 640, 480).size)
s.fill((0, 0, 0))
s.blit(p.font.Font(None, 36).render("OK", True, (255, 255, 255)), (10, 10))
p.display.flip()
p.time.wait(3000)
p.quit()
