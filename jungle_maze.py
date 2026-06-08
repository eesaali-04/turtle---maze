import turtle

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor('blue')

turtle.shape('square')
maze = [
    "XXXXXXXXXXXXXXX",
    "X             X",
    "X XXXXX XXXXX X",
    "X X     X     X",
    "X X XXX X XXX X",
    "X X   X X X   X",
    "X XXX X X X XXX",
    "X     X X X   X",
    "XXXXX X X X XXX",
    "X     X   X   X",
    "X XXXXX XXXXX X",
    "X             X",
    "XXXXXXXXXXXXX F"
]

player = turtle.Turtle()
player.shape('turtle')
player.color('pink')
player.penup()
player.goto(-264,264)
player.speed(0)

score = 0
pen = turtle.Turtle()
pen.color('white')
pen.penup()
pen.goto(210,264)
pen.write(f'score : {score}',font = ('Arial',16,'bold'))
pen.hideturtle()







screen.mainloop()