import turtle

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor('navy')

turtle.shape('square')
# Maze grid
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

# Player setup
player = turtle.Turtle()
player.shape('turtle')
player.color('yellow')
player.penup()
player.goto(-264,264)
player.speed(0)












screen.mainloop()