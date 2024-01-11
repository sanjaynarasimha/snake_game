from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_squares = []
        self.create_snake()
        self.head = self.all_squares[0]

    def create_snake(self):

        for positions in STARTING_POSITIONS:
            self.add_square(positions)

    def add_square(self, positions):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(positions)
        self.all_squares.append(new_turtle)

    def extend(self):
        self.add_square(self.all_squares[-1].position())

    def move(self):
        for squares in range(len(self.all_squares) - 1, 0, -1):
            new_x = self.all_squares[squares - 1].xcor()
            new_y = self.all_squares[squares - 1].ycor()
            self.all_squares[squares].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
