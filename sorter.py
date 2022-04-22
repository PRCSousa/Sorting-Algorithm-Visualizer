import pygame
import random
import math

pygame.init()


class DrawInformation:

    # Colors
    BLACK = 0, 0, 0,
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    MAX_GRAD = 160
    MIN_GRAD = 30
    BG_COLOR = BLACK

    # Paddings
    BORDER = 60
    TOP = 100

    # Text
    FONT = pygame.font.SysFont('hack', 15)

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        self.window.fill(self.BG_COLOR)
        pygame.display.set_caption("Sorting Algorithm Vizualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)
        self.spacing = 2
        self.bar_width = round((self.width - self.BORDER) / len(lst))
        self.bar_height = math.floor(
            (self.height - self.TOP) / (self.max_value - self.min_value))
        self.start_x = 10



def map_range(val, in_min, in_max, out_min, out_max):
    return (val - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


def draw(drawInfo, asc):
    drawInfo.window.fill(drawInfo.BG_COLOR)
    text = drawInfo.FONT.render(f"Sorting Algorithm: INSERIR AQUI | Order: {'Ascending' if asc else 'Descending'}", 1, drawInfo.WHITE)
    drawInfo.window.blit(text, (6, 5))
    draw_list(drawInfo)
    pygame.display.update()


def draw_list(drawInfo):
    lst = drawInfo.lst
    for i, val in enumerate(lst):
        x = drawInfo.start_x + i * drawInfo.bar_width
        y = drawInfo.height - (val - drawInfo.min_value) * drawInfo.bar_height

        grad = map_range(val, drawInfo.min_value,drawInfo.max_value, drawInfo.MIN_GRAD, drawInfo.MAX_GRAD)

        color = (grad, grad, grad)

        pygame.draw.rect(drawInfo.window, color,
                         (x, y, drawInfo.bar_width, drawInfo.height))

def gen_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def main():
    running = True
    n = 100
    min_val = 10
    max_val = 100
    sorting = False
    ascending = True
    lst = gen_list(n, min_val, max_val)
    drawInfo = DrawInformation(800, 600, lst)
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)

        draw(drawInfo, ascending)
        pygame.display.update()

        for event in pygame.event.get():
            keys=pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False

            if event.type != pygame.KEYDOWN:
                continue
            
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed() 
                if key[pygame.K_r]:
                    lst = gen_list(n, min_val, max_val)
                    drawInfo.set_list(lst)
                    sorting = False
                if key[pygame.K_RETURN] and not sorting:
                    sorting = True
                if key[pygame.K_UP] and not sorting:
                    ascending = True
                if key[pygame.K_DOWN] and not sorting:
                    ascending = False
                    

    pygame.quit()


if __name__ == "__main__":
    main()
