import pygame
try:
    from libs.pygameMenu.all_fonts import *
except:
    from all_fonts import *
try:
    from libs.pygameMenu.Text_input import TextInput
except:
    from Text_input import TextInput

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# Font_Comic_Sans_MS = 'Comic Sans MS'
class Field(object):
    def __init__(self, screen=None, rect=(0,0,1,1),
                 text="",
                 size_text=25, font=FONT_comicsansms,
                 color_text=BLACK, bg_rect=WHITE,
                 color_bord=BLACK, image=None,
                 bord=3, color_key=GREEN,
                 text_align="c",
                 real_offset_xy=(0, 0),):
        self.screen = screen
        self.rect = rect
        self.x, self.y, self.size_x, self.size_y = rect
        self.image = image
        self.nr_image = image
        self.real_offset_xy = real_offset_xy
        if image != None:
            self.set_image(image)
        else:
            self.text = text
            self.color_text = color_text
            self.bg_rect = bg_rect
            self.color_bord = color_bord
            self.bord = bord
            self.my_font = pygame.font.SysFont(font, size_text)
            self.text_surface = self.my_font.render(text, True, color_text)
            self.text_align = text_align

    def update(self, event=None):
        self.render()

    def render(self):
        if self.image:
            self.screen.blit(self.image, self.rect)
        else:
            center = self.xy_for_align_text(self.text_align, self.text_surface)
            pygame.draw.rect(self.screen, self.bg_rect, self.rect)
            pygame.draw.rect(self.screen, self.color_bord, self.rect, self.bord)
            text_rect = self.text_surface.get_rect(center=center)
            self.screen.blit(self.text_surface, text_rect)

    def xy_for_align_text(self, aligns, text):
        width, height, = text.get_size()
        x = self.x + self.size_x // 2
        y = self.y + self.size_y // 2
        for align in aligns:
            if align=="c":
                pass
            elif align=="n":
                y = self.y + height // 2
            elif align=="s":
                y = self.y + self.size_y - height // 2
            elif align=="w":
                x = self.x + width // 2 + self.bord + 1
            elif align=="e":
                x = self.x + self.size_x - width // 2 - self.bord - 1
        rect = (x, y)
        #print("====rect====", rect, (width, height), align)
        return rect

    def set_rect(self, rect):
        self.x, self.y, self.size_x, self.size_y = rect
        self.set_xy(rect[:2])
        self.set_height_width(rect[2:])

    def set_xy(self, xy):
        self.x, self.y = xy
        self.rect = xy + self.rect[2:]

    def set_height_width(self, height_width):
        self.size_x, self.size_y = height_width
        self.rect = self.rect[:2] + height_width
        if self.image:
            self.set_image(self.nr_image)

    def set_image(self, image):
        image = pygame.transform.scale(image, (self.size_x, self.size_y))#
        self.image = image

    def set_surface(self, surface):
        self.screen = surface

    def set_real_offset_xy(self, xy):
        self.real_offset_xy = xy

    def mouse_in_me(self):
        mx, my = pygame.mouse.get_pos()
        x1, y1, sx, sy = self.rect
        x2, y2 = x1 + sx, y1 + sy
        ox, oy = self.real_offset_xy
        mx, my = mx - ox, my - oy
        return (x1 <= mx <= x2 and y1 <= my <= y2)

    def mouse_click_me(self):
        mouse_pressed = pygame.mouse.get_pressed()[0]
        return (self.mouse_in_me() and mouse_pressed)


class Button(Field):
    def __init__(self, screen, rect=(0,0,1,1),
                 fun_pressed=None, text="Button",
                 size_text=25, font=FONT_comicsansms,
                 color_text=BLACK, bg_rect=WHITE,
                 color_bord=BLACK, image=None,
                 pressed_text=None,
                 pressed_color_text=WHITE, pressed_bg_rect=BLACK,
                 pressed_color_bord=WHITE, pressed_image=None,
                 bord=3, color_key=GREEN,
                 text_align="c", pressed_text_align="c",
                 real_offset_xy=(0, 0),):
        super().__init__(screen, rect, text=text,
                        size_text=size_text, font=font,
                        color_text=color_text, bg_rect=bg_rect,
                        color_bord=color_bord, image=image,
                        bord=bord, color_key=color_key,
                        text_align=text_align,
                        real_offset_xy=real_offset_xy,)
        self.fun_pressed = fun_pressed
        self.nr_image, self.pressed_nr_image = image, pressed_image
        if image != None:
            self.set_images(image, pressed_image)
        else:
            if pressed_text == None:
                pressed_text = text
            self.pressed_text = pressed_text
            self.pressed_color_text = pressed_color_text
            self.pressed_bg_rect = pressed_bg_rect
            self.pressed_color_bord = pressed_color_bord
            self.pressed_text_surface = self.my_font.render(pressed_text, True, pressed_color_text)
            self.pressed_text_align = pressed_text_align
        self.press = False

    def pressed_render(self):
        if self.image:
            self.screen.blit(self.pressed_image, self.rect)
        else:
            center = self.xy_for_align_text(self.pressed_text_align, self.text_surface)
            pygame.draw.rect(self.screen, self.pressed_bg_rect, self.rect)
            pygame.draw.rect(self.screen, self.pressed_color_bord, self.rect, self.bord)
            text_rect = self.pressed_text_surface.get_rect(center=center)
            self.screen.blit(self.pressed_text_surface, text_rect)

    def update(self, event=None):
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if mouse_pressed:
            if not self.old_mouse_pressed and self.mouse_in_me():
                self.press = True
        else:
            if self.press == True:
                if self.mouse_in_me():
                    if self.fun_pressed:
                        self.fun_pressed()
            self.press = False
        self.old_mouse_pressed = mouse_pressed
        if self.press:
            self.pressed_render()
        else:
            self.render()

        """    def mouse_in_me(self):
        mx, my = pygame.mouse.get_pos()
        x1, y1, sx, sy = self.rect
        x2, y2 = x1 + sx, y1 + sy
        wx, wy = self.start_xy_in_window

        offset_x, offset_y = wx - self.x, wy - self.y
        mx, my = mx - offset_x, my - offset_y
        return (x1 <= mx <= x2 and y1 <= my <= y2)
        """

    def set_height_width(self, height_width):
        self.size_x, self.size_y = height_width
        self.rect = self.rect[:2] + height_width
        if self.image:
            self.set_images(self.nr_image, self.pressed_nr_image)

    def set_images(self, image, pressed_image=None):
        image = pygame.transform.scale(image, (self.size_x, self.size_y))#
        self.image = image
        if pressed_image == None:
            self.pressed_image = image
        else:
            pressed_image = pygame.transform.scale(pressed_image, (self.size_x, self.size_y))#
            self.pressed_image = pressed_image


class Entery_box(Field):
    def __init__(self, screen, rect=(0,0,1,1),
                 preface_text="input", entery_func=None,
                 size_text=25, font=FONT_comicsansms,
                 color_text=BLACK, bg_rect=WHITE,
                 color_bord=BLACK, color_cursor=BLACK,
                 bord=3, max_string_length=-1,
                 #text_align="e",
                 fps=30):
        text_align="e"
        super().__init__(screen, rect, text="",
                        size_text=size_text, font=font,
                        color_text=color_text, bg_rect=bg_rect,
                        color_bord=color_bord,
                        bord=bord,
                        text_align=text_align)
        self.text_input = TextInput(initial_string=preface_text, font_family=font,
                                    font_size=size_text, antialias=True,
                                    text_color=color_text, cursor_color=color_cursor,
                                    repeat_keys_interval_ms=35,
                                    repeat_keys_initial_ms=400,
                                    max_string_length=max_string_length,)
        self.preface_text = preface_text
        self.entery_func = entery_func
        self.text = None

    def update(self, events=None):
        get = self.text_input.update(events)

        self.render()
        if get:
            self.text = self.text_input.get_text()
            if self.entery_func:
                self.entery_func(self.text)
            return self.text
        else:
            return None

    def get_text_enter(self):
        return self.text

    def get_text(self):
        return self.text_input.get_text()

    def set_text(self, text=""):
        self.text_input.set_text(text)

    def render(self):
        size_text = self.text_input.font_size
        pygame.draw.rect(self.screen, self.bg_rect, self.rect)
        pygame.draw.rect(self.screen, self.color_bord, self.rect, self.bord)
        x_text, y_text = self.x + self.bord + 1, self.y + self.size_y // 2 - size_text // 2 - 5
        #print(x_text, y_text )
        self.screen.blit(self.text_input.get_surface(), (x_text, y_text))


class Menu(object):
    def __init__(self, screen, rect, bg_color=None, bg_image=None,
                 distance_between=10, height_field=40, width_field=100, vertical=True,
                 set_count_fields=0, real_offset_xy=(0, 0)):
        self.fields = [None] * set_count_fields
        self.close = False
        print(screen)
        self.screen = screen
        self.bg_color = bg_color
        self.bg_image = bg_image
        self.distance_between = distance_between
        self.x, self.y, self.width, self.height = rect
        self.y_last_field = self.y
        self.x_last_field = self.x

        if vertical:
            self.height_field = height_field
            self.width_field = self.width
        else:
            self.height_field = self.height
            self.width_field = width_field
        self.vertical = vertical
        self.real_offset_xy = real_offset_xy

    def set_field(self, field, index=-1, is_update=True):
        if self.vertical:
            field_x, field_y = self.x, self.y_last_field
            width_field, height_field = self.width_field, self.height_field
            self.y_last_field += self.distance_between + height_field
        else:
            field_x, field_y = self.x_last_field, self.y
            width_field, height_field = self.width_field, self.height_field
            self.x_last_field += self.distance_between + width_field
        field_rect = (field_x, field_y, width_field, height_field)
        field.set_rect(field_rect)
        #print(self.fields, index)
        field.set_surface(self.screen)
        field.set_real_offset_xy(self.real_offset_xy)
        self.fields[index] = [field, is_update]

    def get_field(self, i=-1):
        return self.fields[i]

    def update(self):
        for field in self.fields:
            if field[1]:
                field[0].update()

    def add(self, field, is_update=True):
        self.fields.append(None)
        self.set_field(field, is_update=is_update)

    def set_close(self, close=True):
        self.close = close

if __name__ == "__main__":
    width, height = 310, 400
    scr = pygame.display.set_mode((width, height))
    screen = pygame.Surface((width, height - 10))


    pygame.font.init() # you have to call this at the start,
                       # if you want to use this module.
    img_but = pygame.image.load("but.png")
    press_img_but = pygame.image.load("but2.png")
    but = Button(screen, #(100, 120, 100, 40),
                 image=img_but, pressed_image=press_img_but,
                 fun_pressed=lambda: print("KU KU"))
    but_2 = Button(screen, (100, 170, 100, 40),
                 text="Gasha", pressed_text="Gasha",
                 fun_pressed=lambda: print("Hello"),
                 pressed_text_align="s")
    entery = Entery_box(screen, rect=(100, 170, 100, 40),
                 preface_text="Gasha",
                entery_func=lambda x: print(x),
                max_string_length=5,)
    menu = Menu(screen,
                (100, 120, 100, 40), distance_between=10,
                 height_field=40, vertical=True,
                 real_offset_xy=(0, 5))
    menu.add(but)
    menu.add(but_2)
    menu.add(entery, is_update=False)

    while 1:
        pygame.time.delay(50)
        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT: exit()
        screen.fill(RED)
        entery.update(events)
        menu.update()
        #but.update()
        #but_2.update()
        scr.blit(screen, (0, 5))
        pygame.display.update()
        mx, my = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        print(mx, my, pressed)
