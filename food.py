from turtle import Turtle
from scoreboard import SCREEN_SIZE
import random


class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("blue")
		self.speed("fastest")
		self.shapesize(0.5, 0.5)
		self.penup()
		self.refresh()

	def refresh(self):
		self.goto(random.randint(-SCREEN_SIZE + 20, SCREEN_SIZE - 20), random.randint(-SCREEN_SIZE + 20, SCREEN_SIZE - 20))
