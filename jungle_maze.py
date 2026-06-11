import turtle

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor('blue')

turtle.shape('square')
maze = [
    "XXXXXXXXXXXXXXX",
    "X             X",
    "X XXXXX XXXXXOX",
    "X X     X     X",
    "X X XXXOX XXX X",
    "X X   X X X   X",
    "X XXX X XOX XXX",
    "X     X X X   X",
    "XXXXX XOX X XXX",
    "X     X   X   X",
    "XOXXXXX XXXXX X",
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

obstacles = []
bonuses = []
def create_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            chr = maze[row][col]
            x = -288 + (col * 24)
            y = 288 - (row * 24)

            if chr == 'X':
                obs = turtle.Turtle()
                obs.shape('square')
                obs.speed(100)
                obs.color('white')
                obs.penup()
                obs.goto(x,y)
                obstacles.append(obs)
            
            if chr == 'O':
                bonus = turtle.Turtle()
                bonus.shape('circle')
                bonus.speed(100)
                bonus.color('yellow')
                bonus.penup()
                bonus.goto(x,y)
                bonuses.append(bonus)
                

            elif chr == 'F':
                food = turtle.Turtle()
                food.shape('triangle')
                food.color('pink')
                food.penup()
                food.goto(x,y)
                return food


def is_valid_move(x,y):
    for obs in obstacles:
        if obs.xcor() == x and obs.ycor() == y:
            return False
    return True

def is_touch_bonus(x,y):
    for bonus in bonuses:
        if bonus.xcor() == x and bonus.ycor() == y:
            return True
            score += 10
            pen.clear()
            pen.write(f'score : {score}',font = ('Arial',16,'bold'))
    return False

def move_up():
    x = player.xcor()
    y = player.ycor() + 24
    if is_valid_move(x,y):
        player.goto(x,y)

def move_down():
    x = player.xcor()
    y = player.ycor() - 24
    if is_valid_move(x,y):
        player.goto(x,y)

def move_left():
    x = player.xcor() - 24
    y = player.ycor()
    if is_valid_move(x,y):
        player.goto(x,y)

def move_right():
    x = player.xcor() + 24
    y = player.ycor()
    if is_valid_move(x,y):
        player.goto(x,y)

screen.listen()
screen.onkey(move_up,'Up')
screen.onkey(move_down,'Down')
screen.onkey(move_left,'Left')
screen.onkey(move_right,'Right')






screen.mainloop()