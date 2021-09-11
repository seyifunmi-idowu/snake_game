from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 285)
        self.update_score()

    def update_score(self):
        self.goto(0, 285)
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=True, align="center")

    def store_high_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.store_high_score()
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()