import sys
import sdl2
import sdl2.ext
sdl2.ext.init()
window = sdl2.ext.Window("SDL2 OK Display", size=(640, 480))
window.show()
renderer = sdl2.ext.Renderer(window)
renderer.color = sdl2.ext.Color(0, 0, 0)
renderer.clear()
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font_manager = sdl2.ext.FontManager(font_path, size=36)
factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=renderer)
text_sprite = factory.from_text("OK", fontmanager=font_manager, color=sdl2.ext.Color(255, 255, 255))
renderer.copy(text_sprite, dstrect=(10, 10, text_sprite.size[0], text_sprite.size[1]))
renderer.present()
sdl2.SDL_Delay(3000)
sdl2.ext.quit()
sys.exit()