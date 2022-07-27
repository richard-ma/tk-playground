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


class ShapeCreator:
    def __init__(self):
        pass

    def create(self):
        pass


class NoiseRectShapeCreator(ShapeCreator):
    def __init__(self, canvas, color_generator, start=[0, 0], indent=[100, 100], size=[1000, 1000], noise=0, noise_start=0):
        assert noise >= noise_start

        self.canvas = canvas
        self.color_generator = color_generator
        self.start = start
        self.indent = indent
        self.size = size
        self.noise = noise
        self.noise_start = noise_start

    def create(self):
        xs = (self.size[0] - self.start[0]) // self.indent[0]
        ys = (self.size[1] - self.start[1]) // self.indent[1]

        for x in range(xs):
            for y in range(ys):
                # coordinates unclockwise
                coords = [
                    x * self.indent[0] + self.start[0] + random.randint(self.noise_start, self.noise),
                    y * self.indent[1] + self.start[1] + random.randint(self.noise_start, self.noise),
                    x * self.indent[0] + self.start[0] + random.randint(self.noise_start, self.noise),
                    y * self.indent[1] + self.start[1] + self.indent[1] - random.randint(self.noise_start, self.noise),
                    x * self.indent[0] + self.start[0] + self.indent[0] - random.randint(self.noise_start, self.noise),
                    y * self.indent[1] + self.start[1] + self.indent[1] - random.randint(self.noise_start, self.noise),
                    x * self.indent[0] + self.start[0] + self.indent[0] - random.randint(self.noise_start, self.noise),
                    y * self.indent[1] + self.start[1] + random.randint(self.noise_start, self.noise),
                ]
                self.canvas.create_polygon(coords, fill=self.color_generator.generat())


if __name__ == "__main__":
    size = [1000, 1000]
    start = [0, 0]
    indent = [50, 50]
    noise = indent[0] // random.randint(3, indent[0] // 3)
    color_generator = RandomColorGenerator(r_max=0, g_max=0, b_min=127)

    root = Tk()
    c = Canvas(root, bg="black", height=1000, width=1000)
    c.pack()

    sc = NoiseRectShapeCreator(
        c,
        color_generator,
        start=start,
        indent=indent,
        size=size,
        noise=noise,
        noise_start=noise - random.randint(2, noise))
    sc.create()

    root.mainloop()
