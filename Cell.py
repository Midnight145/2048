import pygame


pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 64)


class Cell(pygame.sprite.Sprite):
    def __init__(self, group, color, x, y, width, height, value, img=None):
        super().__init__(group)
        if img is not None:
            self.image = img
        else:
            self.image = pygame.Surface([width, height]); self.image.fill(color)
        self.value = value
        val_text = font.render(str(self.value), False, (0, 0, 0))
        rect = val_text.get_rect()
        print(rect.x, rect.y)
        self.image.blit(val_text, (80 - rect.width // 2, 80 - rect.height // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_right(self):
        if len(self.groups()) == 0: return
        while True:
            for i in self.groups()[0]:
                i: Cell
                if i.rect.collidepoint(self.rect.x + self.rect.width + 80, self.rect.y) and i is not self:
                    if i.value == self.value:
                        self.rect.x += 160
                        self.create_cell(i)
                        return
                    return
            if self.rect.x + self.rect.width + 160 > 640:
                return
            self.rect.x += 160

    def move_left(self):
        if len(self.groups()) == 0: return
        while True:

            for i in self.groups()[0]:
                i: Cell
                if i.rect.collidepoint(self.rect.x - 80, self.rect.y) and i is not self:
                    if i.value == self.value:
                        self.rect.x -= 160
                        self.create_cell(i)
                        return

                    return
            if self.rect.x - 160 < 0:
                return
            self.rect.x -= 160

    def move_up(self):
        if len(self.groups()) == 0: return
        while True:
            for i in self.groups()[0]:
                i: Cell
                if i.rect.collidepoint(self.rect.x, self.rect.y - 80) and i is not self:
                    if i.value == self.value:
                        self.rect.y -= 160
                        self.create_cell(i)
                        return

                    return
            if self.rect.y - 160 < 0:
                return
            self.rect.y -= 160

    def move_down(self):
        if len(self.groups()) == 0: return
        while True:
            for i in self.groups()[0]:
                i: Cell

                if i.rect.collidepoint(self.rect.x, self.rect.y + self.rect.height + 80) and i is not self:
                    if i.value == self.value:
                        self.rect.y += 160
                        self.create_cell(i)
                        return
                    return
            if self.rect.y + self.rect.height + 160 > 640:
                return
            self.rect.y += 160

    def create_cell(self, destroy):
        Cell(self.groups()[0], (0, 0, 255), self.rect.x, self.rect.y, self.rect.width,
             self.rect.height, self.value * 2)

        self.kill()
        destroy.kill()
        del self, destroy
        pygame.display.update()
