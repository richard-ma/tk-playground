import random
from tkinter import *
from tkinter import ttk


class ColorGenerator:
    def __init__(self):
        pass

    def generat(self):
        pass


class RandomColorGenerator(ColorGenerator):
    def __init__(self, r_min=0, r_max=255, g_min=0, g_max=255, b_min=0, b_max=255):
        self.limit = dict()
        self.limit['r_min'] = r_min
        self.limit['r_max'] = r_max
        self.limit['g_min'] = g_min
        self.limit['g_max'] = g_max
        self.limit['b_min'] = b_min
        self.limit['b_max'] = b_max

    def generat(self):
        r = lambda s, e: random.randint(s, e)
        return "#%02X%02X%02X" % (r(self.limit['r_min'], self.limit['r_max']), r(self.limit['g_min'], self.limit['g_max']), r(self.limit['b_min'], self.limit['b_max']))


def create_rectangles(canvas, color_generator, start=[0, 0], indent=[100, 100], size=[1000, 1000], noise=0, noise_start=0):
    assert noise >= noise_start

    xs = (size[0] - start[0]) // indent[0]
    ys = (size[1] - start[1]) // indent[1]

    for x in range(xs):
        for y in range(ys):
            # coordinates unclockwise
            coords = [
                x * indent[0] + start[0] + random.randint(noise_start, noise),
                y * indent[1] + start[1] + random.randint(noise_start, noise),
                x * indent[0] + start[0] + random.randint(noise_start, noise),
                y * indent[1] + start[1] + indent[1] - random.randint(noise_start, noise),
                x * indent[0] + start[0] + indent[0] - random.randint(noise_start, noise),
                y * indent[1] + start[1] + indent[1] - random.randint(noise_start, noise),
                x * indent[0] + start[0] + indent[0] - random.randint(noise_start, noise),
                y * indent[1] + start[1] + random.randint(noise_start, noise),
            ]
            canvas.create_polygon(coords, fill=color_generator.generat())


if __name__ == "__main__":
    size = [1000, 1000]
    start = [0, 0]
    indent = [50, 50]
    noise = indent[0] // random.randint(3, indent[0] // 3)
    color_generator = RandomColorGenerator(r_max=0, g_max=0, b_min=127)

    root = Tk()
    c = Canvas(root, bg="black", height=1000, width=1000)
    c.pack()

    create_rectangles(
        c,
        color_generator,
        start=start,
        indent=indent,
        size=size,
        noise=noise,
        noise_start=noise - random.randint(2, noise)
    )
    root.mainloop()
