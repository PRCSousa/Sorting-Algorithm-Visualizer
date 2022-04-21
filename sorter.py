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
    BG_COLOR = WHITE

    # Paddings
    BORDER = 100
    TOP = 150

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
        self.bar_width = round((self.width - self.BORDER) / len(lst))
        self.bar_height = math.floor(
            (self.height - self.TOP) / (self.max_value - self.min_value))
        self.start_x = self.BORDER // 2


def map_range(val, in_min, in_max, out_min, out_max):
    return (val - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


def draw(drawInfo):
    draw_list(drawInfo)
    pygame.display.update()


def draw_list(drawInfo):
    lst = drawInfo.lst
    for i, val in enumerate(lst):
        x = drawInfo.start_x + i * drawInfo.bar_width
        y = drawInfo.height - (val - drawInfo.min_value) * drawInfo.bar_height

        grad = map_range(val, drawInfo.min_value,drawInfo.max_value, 230, 50)

        color = (grad, grad, grad)

        pygame.draw.rect(drawInfo.window, color,
                         (x, y, drawInfo.bar_width - 2, drawInfo.height))

def gen_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def main():
    running = True
    n = 50
    min_val = 0
    max_val = 100
    lst = gen_list(n, min_val, max_val)
    drawInfo = DrawInformation(800, 600, lst)
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)

        draw(drawInfo)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()
