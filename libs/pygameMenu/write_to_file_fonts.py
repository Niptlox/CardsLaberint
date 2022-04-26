import pygame
ar = pygame.font.get_fonts()
f = open("all_fonts.py", "w")
for font in ar:
    st = f"FONT_{font} = '{font}'\n"
    f.write(st)
f.close()
