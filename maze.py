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

# Obstacle setup
obstacles = []

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

            elif chr == 'F':
                food = turtle.Turtle()
                food.shape('triangle')
                food.color('pink')
                food.penup()
                food.goto(x,y)
                return food

# Check if the move is valid
def is_valid_move(x,y):
    for obs in obstacles:
        if obs.xcor() == x and obs.ycor() == y:
            return False
    return True

# Add movement to the player
def move_up():
    x = player.xcor()
    y = player.ycor() + 24
    if is_valid_move(x,y):
        player.goto(x,y)
    check_winner()

def move_down():
    x = player.xcor()
    y = player.ycor() - 24
    if is_valid_move(x,y):
        player.goto(x,y)
    check_winner()

def move_left():
    x = player.xcor() - 24
    y = player.ycor()
    if is_valid_move(x,y):
        player.goto(x,y)
    check_winner()

def move_right():
    x = player.xcor() + 24
    y = player.ycor()
    if is_valid_move(x,y):
        player.goto(x,y)
    check_winner()

screen.listen()
screen.onkey(move_up,'Up')
screen.onkey(move_down,'Down')
screen.onkey(move_left,'Left')
screen.onkey(move_right,'Right')

def check_winner():
    if player.distance(food) < 12:
        player.hideturtle()
        food.hideturtle()
        screen.bye()
        print('Congratulations! You completed the maze.')

food = create_maze()        


screen.mainloop()