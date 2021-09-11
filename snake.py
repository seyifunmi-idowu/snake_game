from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:


    def __init__(self, ):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):

        for index in range(3):
            self.add_segment(index)


    def add_segment(self, index):
        x_axis = 0
        y_axis = 0
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.shapesize(1, 1)
        snake.goto(x=x_axis, y=y_axis)
        x_axis -= 20
        self.segment.append(snake)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]


    def move(self):
        for seg_num in range(len(self.segment)-1, 0, -1):   #this range takes (start=-1, stop=0, step=-1)
            new_x = self.segment[seg_num -1].xcor()
            new_y = self.segment[seg_num -1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(20)

    def move_up(self):
        if self.head.heading() != DOWN:
            # This is replaced in the __innit__. you will find how we came about the .head
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)