# Par Khalil Nait Bahloul avec l`aide de Maxime
# TP4

# import arcade and random
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COULEURS = [arcade.color.ALABAMA_CRIMSON, arcade.color.AMBER, arcade.color.AO, arcade.color.AZURE, arcade.color.CADMIUM_ORANGE, arcade.color.BYZANTIUM]
#definir la forme balle
class Balle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = random.uniform(-5, 5)
        self.change_y = random.uniform(-5, 5)
        self.rayon = random.randint(10, 30)
        self.couleur = random.choice(COULEURS)
    #code pour le mouvement des formes
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        # code pour que la balle ne sorte pas de l'écran
        if self.x < 0 + self.rayon:
            self.x = 0 + self.rayon
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.rayon:
            self.x = SCREEN_WIDTH - self.rayon
            self.change_x *= -1
        if self.y < 0 + self.rayon:
            self.y = 0 + self.rayon
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.rayon:
            self.y = SCREEN_HEIGHT - self.rayon
            self.change_y *= -1
    #dessin de chaque "frame"
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.couleur)
#definir la forme rectangle
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = random.uniform(-5, 5)
        self.change_y = random.uniform(-5, 5)
        self.width = random.randint(20, 50)
        self.height = random.randint(20, 50)
        self.couleur = random.choice(COULEURS)
        self.angle = random.uniform(0, 360)

    # code pour le mouvement des formes
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        # code pour que le rectangle ne sorte pas de l'écran
        if self.x < 0 + self.width / 2:
            self.x = 0 + self.width / 2
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.width / 2:
            self.x = SCREEN_WIDTH - self.width / 2
            self.change_x *= -1
        if self.y < 0 + self.height / 2:
            self.y = 0 + self.height / 2
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.height / 2:
            self.y = SCREEN_HEIGHT - self.height / 2
            self.change_y *= -1

    # dessin de chaque "frame"
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.couleur, self.angle)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "essai #1")
        self.balles = []
        self.rectangles = []

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

        for balle in self.balles:
            balle.draw()

        for rectangle in self.rectangles:
            rectangle.draw()

    #Clique gauche et clique droit de la souris pour générer les cercles et rectangles
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.balles.append(Balle(x, y))

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            self.rectangles.append(Rectangle(x, y))

    #Faire bouger les formes
    def update(self, delta_time):
        for balle in self.balles:
            balle.update()

        for rectangle in self.rectangles:
            rectangle.update()
#lancer le jeu
def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()

main()