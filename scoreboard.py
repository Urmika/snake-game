from turtle import Turtle
ALIGN = "center"
FONT = ("Courier",24,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.score = 0
        self.goto(0,260)
        #self.high_score = 0
        with open(r"..\..\Desktop\data.txt") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"..\..\Desktop\data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER",align=ALIGN,font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def decrease_score(self):
        self.score -= 1
        self.clear()
        self.update_scoreboard()
