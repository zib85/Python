class Stationery:
    def __init__(self, title="What is the tool to draw:"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Try to draw with a {self.title} pen!")


class Pencil(Stationery):
    def draw(self):
        print(f"Try the possibilities of the {self.title} pencil!")


class Marker(Stationery):
    def draw(self):
        print(f"Master the ability of the {self.title} marker!")


stat = Stationery()
stat.draw()
pen = Pen("Brauberg")
pen.draw()
pencil = Pencil("Derwent")
pencil.draw()
marker = Marker("COPIC")
marker.draw()
