import sdl2
import sdl2.ext
sdl2.ext.init()
w = sdl2.ext.Window("", size=(640, 480))
w.show()
r = sdl2.ext.Renderer(w)
r.color = sdl2.ext.Color(0, 0, 0)
r.clear()
t = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE,renderer=r).from_text("OK", fontmanager = sdl2.ext.FontManager(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size=36), color=sdl2.ext.Color(255, 255, 255))
r.copy(t, dstrect=(10, 10, t.size[0], t.size[1]))
r.present()
sdl2.SDL_Delay(3000)
sdl2.ext.quit()
