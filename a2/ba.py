def aa(pa):
    import pygame
    pygame.init()
    a=pygame.display.set_mode((640,480))
    b=pygame.font.SysFont(None,36).render(pa,True,(255,255,255))
    c=True
    while c:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:c=False
        a.blit(b,(0,0))
        pygame.display.flip()
    pygame.quit()
