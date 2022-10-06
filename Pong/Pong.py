# Sunny Chan
# CS-UY 1114
# Final project

import turtle
import time
import random

# This variable represents the x position
# of the player's paddle. Initially, it
# will be 0 (i.e. in the center). The y
# position of the paddles never changes,
# so we don't need a variable for it.
user1x = 0

# This variable represents the x position
# of the computer's paddle. Initially, it
# will be 0 (i.e. in the center)
user2x = 0

# These variables store the current x and y
# position of the ball. Their values will be
# updates on each frame, as the ball moves.
ballx = 0
bally = 0

# These variables store the current x and y
# velocity of the ball. Their values will be
# updates on each frame, as the ball moves.
ballvx = 0
ballvy = 0

# These variables store the current score 
# of the game.
user1points = 0
user2points = 0

def draw_frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables, draw all visual
    elements on the screen: the paddles,
    the ball, and the current score.
    Please note that this is your only function
    where drawing should happen (i.e. the only
    function where you call functions in the
    turtle module). Other functions in this
    program merely update the state of global
    variables.
    This function also should not modify any
    global variables.
    Hint: write this function first!
    """
    #ball
    turtle.penup()
    turtle.goto(ballx,bally)
    turtle.pendown()
    turtle.dot(20)
    #Paddle User 1
    turtle.penup()
    turtle.goto(user1x - 25, -turtle.window_height()/2 + 100)
    turtle.pendown()
    turtle.width(2)
    turtle.forward(50)
    #Paddle User 2
    turtle.penup()
    turtle.goto(user2x - 25, turtle.window_height()/2 - 100)
    turtle.pendown()
    turtle.forward(50)
    #Scoreboard
    msg1 = "Player 1 Score: " + str(user1points)
    msg2 = "Player 2 Score: " + str(user2points)
    msg = "\n".join([msg1, msg2])
    turtle.color("Black")
    turtle.penup()
    turtle.goto(-turtle.window_width()/2 + 10, -turtle.window_height()/2 + 50)
    turtle.pendown()
    turtle.write(msg, font=("Arial", 10, "normal"))

def key_left():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the user's paddle
    appropriately by modifying the variable
    user1x. It should not draw anything on the
    screen.
    """
    global user1x
    user1x = (user1x - 20)

def key_right():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the user's paddle
    appropriately by modifying the variable
    user1x. It should not draw anything on the
    screen.
    """
    global user1x
    user1x = (user1x + 20)

def reset():
    """
    signature: () -> NoneType
    Reset the global variables representing
    the position and velocity of the ball and
    the position of the paddles to their initial
    state, effectively restarting the game. The
    initial velocity of the ball should be random
    (but there there must be nonzero vertical
    velocity), but the speed of the ball should
    be the same in every game.
    """
    global user1x, user2x
    global ballvx, ballvy
    global ballx, bally
    gameover = False
    user1x = 0
    user2x = 0
    ballx = 0
    bally = 0
    ballvy = 0
    ballvx = 0
    while ballvy == 0:
        #speed = 5
        ballvy = random.randint(-8,8)
        ballvx = random.choice([((64 - (ballvy ** 2)) ** 0.5), -((64 - (ballvy ** 2)) ** 0.5)])


def ai():
    """
    signature: () -> NoneType
    Perform the 'artificial intelligence' of
    the game, by moving the computer's paddle
    to an appropriate location by updating
    the user2x variable. The computer
    paddle should move towards the ball in an
    attempt to get under it. THis function
    should not draw anything on the screen.
    """
    global user2x
    if ballx < user2x:
        user2x = (user2x - 6)
    elif ballx > user2x:
        user2x = (user2x + 6)

def physics():
    """
    signature: () -> NoneType
    This function handles the physics of the game
    by updating the position and velocity of the
    ball depending on its current location. This
    function should detect if the ball has collided
    with a paddle or a wall, and if so, adjust the
    direction of the ball (as stored in the ballvx
    and ballvy variables) appropriately. If the ball
    has not collided with anything, the position of the
    ball should be updated according to its current
    velocity.
    This function should also detect if one of
    the two players has missed the ball. If so, it
    should award a point to the other player, and
    then call the reset() function to start a new
    round.
    This function should not draw anything on the
    screen.
    """
    global ballx, bally
    global ballvx, ballvy
    global user1points, user2points
    ballx += ballvx
    bally += ballvy
    #Collides with walls
    if ((-turtle.window_width()/2 + 10) > ballx) or  (ballx > (turtle.window_width()/2 - 10)):
        ballvx = -ballvx
    #Ball hits paddle user 1
    if (bally <= -turtle.window_height()/2 + 110):
        if (user1x - 25 <= ballx) and (ballx < user1x): #Hit left side of paddle, ball moves 30 degrees left
            ballvy = 8 * 0.5
            ballvx = -(8 * ((3 ** 0.5)/2))
        elif (user1x < ballx) and (ballx <= user1x + 25): #Hit right side of paddle, ball moves 30 degrees right
            ballvy = 8 * 0.5
            ballvx = 8 * ((3 ** 0.5)/2)
        elif bally == user1x: #Hit middle of paddle, ball moves perpendicular of paddle
            ballvy = 8
            ballvx = 0
        else:               #Miss paddle, reset and score of user 2 increase by 1
            reset()
            user2points += 1
    if (bally >= turtle.window_height()/2 - 110):
        if (user2x - 25 <= ballx) and (ballx < user2x): #Hit left side of paddle, ball moves 30 degrees left
            ballvy = -(8 * 0.5)
            ballvx = -(8 * ((3 ** 0.5)/2))
        elif (user2x < ballx) and (ballx <= user2x + 25): #Hit right side of paddle, ball moves 30 degrees right
            ballvy = -(8 * 0.5)
            ballvx = 8 * ((3 ** 0.5)/2)
        elif bally == user2x: #Hit middle of paddle, ball moves perpendicular of paddle
            ballvy = -8
            ballvx = 0
        else:               #Miss paddle, reset and score of user 1 increase by 1
            reset()
            user1points += 1

def is_game_over():
    """
    signature: () -> bool
    Returns true when the game is over, according
    to the rules specified in the assignment.
    """
    if user2points == 5:
        return True

def read_high_scores():
    """
    signature: () -> list(tuple(int, str))
    Reads the current contents of the high score
    file. It returns a list of tuples, where
    each tuple contains a score and a player's
    name. The scores should be returned in
    decreasing order, with the best score
    first. If the high score file does not
    exist, the function should return an
    empty list.
    """
    high_scores_list = []
    high_scores_file = open("Highscores.txt", "r")
    for line in high_scores_file:
        score = line.strip().split(",")
        score[0] = int(score[0])
        high_scores_list.append(score)
    high_scores_file.close()
    high_scores_list.sort()
    high_scores_list.reverse()
    return high_scores_list

def update_high_scores():
    """
    signature: () -> bool

    position on the high score table. If so,
    prompt the user for their name and update
    the table.
    This function should call read_high_scores
    to get the current high score values.
    """
    high_scores_list = read_high_scores()
    update = False
    while not update:
        if high_scores_list == []:
            print(high_scores_list)
            myfile = open("Highscores.txt", "w")
            Name = input("Enter Your Name: ")
            str_lst = ", ".join([str(user1points),Name])
            myfile.write(str_lst)
            lst = [user1points, Name]
            high_scores_list.append(tuple(lst))
            print(high_scores_list)
            myfile.close()
            update = True
            return update
        else:
            for i in range(len(high_scores_list)):
                myfile = open("Highscores.txt", "a")
                score_counter = high_scores_list[i][0]
                print(user1points)
                print(score_counter)
                if user1points >= score_counter:
                    Name = input("Enter Your Name:")
                    lst = [user1points, Name]
                    str_lst = ", ".join([str(user1points),Name])
                    myfile.write(str_lst+ "\n")
                    high_scores_list.insert(i,(tuple(lst)))
                    myfile.close()
                    update = True
                    return update
                elif len(high_scores_list) <= 10:
                    Name = input("Enter Your Name:")
                    lst = [user1points, Name]
                    str_lst = ", ".join([str(user1points),Name])
                    myfile.write(str_lst + "\n")
                    high_scores_list.append(lst)
                    myfile.close()
                    update = True
                    return update
            update = True
            return update
    

def display_high_scores():
    """
    signature: () -> bool
    Get the current content of the high score
    table from a file and display it in the
    turtle window.
    This function should call read_high_scores
    to get the current high score values.
    """
    high_scores_list = read_high_scores()
    for i in range(len(high_scores_list)):
        turtle.penup()
        turtle.goto(0,turtle.window_height()/4 - 10(i))
        turtle.pendown()
        turtle.write(str(high_scores_list[i]), font=("Arial", 10, "normal"))
    

def main():
    """
    signature: () -> NoneType
    Run the pong game. You shouldn't need to
    modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onkey(key_left, "Left")
    turtle.onkey(key_right, "Right")
    turtle.listen()
    reset()
    while not is_game_over():
        physics()
        ai()
        turtle.clear()
        draw_frame()
        turtle.update()
        time.sleep(0.05)
    update_high_scores()
    display_high_scores()
    
main()
