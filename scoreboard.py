from turtle import Turtle

SCREEN_SIZE = 300
ALIGNMENT = "center"
FONT_SIZE = SCREEN_SIZE // 12
FONT_STYLE = "Courier"
FONT = (FONT_STYLE, FONT_SIZE, "normal")


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.penup()
		self.color("white")
		self.hideturtle()
		self.speed("fastest")
		self.goto(0, 8.7*SCREEN_SIZE//10)
		self.refresh()

	def increase_score(self):
		self.score += 1
		self.refresh()

	def game_over(self):
		self.goto(0, -20)
		self.write("GAME OVER", False, ALIGNMENT, (FONT_STYLE, SCREEN_SIZE // 8, "normal"))

	def refresh(self):
		self.clear()
		self.write(f"Score - {self.score}", False, ALIGNMENT, FONT)
