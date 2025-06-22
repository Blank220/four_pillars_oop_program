from tkinter import Tk
from snake_game import Snake

class MySnake(Snake):
    def __init__(self):
        super().__init__()
        print("Customized snake behavior")

if __name__ == "__main__":
    root = Tk()
    game = Snake(root)
    root.mainloop()
