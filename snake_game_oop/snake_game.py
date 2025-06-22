from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#FFFFFF"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

    def move(self, x, y):
        self.coordinates.insert(0, (x, y))
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        self.squares.insert(0, square)

    def remove_tail(self):
        del self.coordinates[-1]
        canvas.delete(self.squares[-1])
        del self.squares[-1]

class Food:
    def __init__(self, snake_coordinates):
        # Generate food position not overlapping snake coordinates
        while True:
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            if (x, y) not in snake_coordinates:
                break
        self.coordinates = [x, y]
        self.square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

    def draw(self):
        canvas.coords(self.square, self.coordinates[0], self.coordinates[1],
                      self.coordinates[0] + SPACE_SIZE, self.coordinates[1] + SPACE_SIZE)

def next_turn(snake):
    global food, score

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Wrap around screen edges
    x %= GAME_WIDTH
    y %= GAME_HEIGHT

    snake.move(x, y)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food(snake.coordinates)
    else:
        snake.remove_tail()

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake)

window = Tk()
window.title("Snake game")
window.resizable(False, False)

window.mainloop()