import turtle
import random
import time
import music_handler

def screen_setup ():
    
    pg = turtle.Screen()
    
    pg.title("Paddle Prodigy")
    pg.bgcolor("white")
    pg.setup(width=1920, height=1080)
    #pg.bgpic(".png")
    pg.tracer(0)
    draw_border(pg)
    
    return pg


def draw_border(pg):
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("black")
    border_pen.penup()
    border_pen.goto(-400, 300)
    border_pen.pendown()
    
    for side in range(4):
        if side % 2 == 0:
            border_pen.forward(800)
        else:
            border_pen.forward(600)
        border_pen.right(90)
    border_pen.hideturtle()

def make_paddles(x, y):
    
    paddle = turtle.Turtle()
    
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("black")
    paddle.shapesize(stretch_wid = 5, stretch_len = 1)
    
    paddle.penup()
    paddle.goto(x, y)
    
    return paddle

def make_ball():
    
    ball = turtle.Turtle()
    
    ball.speed(0)
    ball.shape("square")
    ball.color("black")
    
    ball.penup()
    ball.goto(0, 0)
    
    ball.dx = 1
    ball.dy = -1
    
    return ball

# displays score on screen
def make_pen():
    
    pen = turtle.Turtle()
    
    pen.speed(0)
    pen.color("black")
    pen.penup()
    
    pen.hideturtle()
    pen.goto(0, 260)
    
    return pen

def score_update(pen, score_a, score_b):
    pen.clear()
    pen.write(f"Player: {score_a}  Bot: {score_b}", align="center", font=("Georgia", 24, "italic"))


# Paddle mechanics
def player_paddle_up(paddle):
    
    y = paddle_a.ycor()
    
    if  y < 250:
        y += 70
    
    paddle_a.sety(y)
    
def player_paddle_down(paddle):
    
    y = paddle_a.ycor()
    
    if  y > -240:
        y -= 70
    
    paddle_a.sety(y)


def vs_robot(ball, paddle_b):
    
    if random.random() < 0.3:
        return
    
    bot_speed = 4
    speed_nerf = 50         # done to decrease bot difficulty
    miss_chance = 0.5          
    
    if random.random() < miss_chance:
        return
    
    if ball.ycor() > paddle_b.ycor() + speed_nerf:
        new_y = paddle_b.ycor() + bot_speed
        if new_y < 250:
            paddle_b.sety(new_y)
    
    elif ball.ycor() < paddle_b.ycor() - speed_nerf:
        new_y = paddle_b.ycor() - bot_speed
        if new_y > -240:
            paddle_b.sety(new_y)


def keybinds(pg, paddle_a):
    
    pg.listen()
    
    pg.onkeypress(lambda: player_paddle_up(paddle_a), "Up")
    pg.onkeypress(lambda: player_paddle_down(paddle_a), "Down")
    pg.onkeypress(lambda: player_paddle_up(paddle_a), "w")
    pg.onkeypress(lambda: player_paddle_down(paddle_a), "s")
    
    
def maingame_loop(pg, ball, paddle_a, paddle_b, pen):
    
    score_a = 0
    score_b = 0
    base_speed = 4
    speed_increase = 0.02
    max_speed = 1
    
    while True:
        
        pg.update()
        
        # ball movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
        # speed ceiling
        if abs(ball.dx) > max_speed:
            ball.dx = max_speed * (1 if ball.dx > 0 else -1)
        if abs(ball.dy) > max_speed:
            ball.dy = max_speed * (1 if ball.dy > 0 else -1)
        
        # checking arena borders
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.dy *= -1
        
        if ball.xcor() > 390:
            score_a += 1
            ball.goto(0, 0)
            ball.dx = -(abs(ball.dx) + score_a * speed_increase) * (1 if ball.dx < 0 else -1)
            ball.dy = -(abs(ball.dy) + score_a * speed_increase) * (1 if ball.dy < 0 else -1)
            score_update(pen, score_a, score_b)
            paddle_a.goto(-350, 0)
            paddle_b.goto(350, 0)
        
        if ball.xcor() < -390:
            score_b += 1
            ball.goto(0, 0)
            ball.dx = abs(ball.dx) + score_a * speed_increase * (1 if ball.dx < 0 else -1)
            ball.dy = abs(ball.dy) + score_a * speed_increase * (1 if ball.dy < 0 else -1)
            score_update(pen, score_a, score_b)
            paddle_a.goto(-350, 0)
            paddle_b.goto(350, 0)
        
        # Paddle / Ball Collision Mechanics
        if (ball.dx > 0 and 340 < ball.xcor() < 350 and paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 40) or \
           (ball.dx < 0 and -350 < ball.xcor() < -340 and paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 40):
               ball.dx *= -1
            
        
        # Robot Movement
        vs_robot(ball, paddle_b)


if __name__ == "__main__":
    
    pg = screen_setup()
    
    paddle_a = make_paddles(-350, 0)
    paddle_b = make_paddles(350, 0)
    
    ball = make_ball()
    pen = make_pen()
    
    soundtrack_paths = ["Blue_sky.wav", "Reflection_2021.wav"]
    music_handler.initialize_soundtrack(soundtrack_paths)
    
    score_update(pen, 0, 0)
    keybinds(pg, paddle_a)
    maingame_loop(pg, ball, paddle_a, paddle_b, pen)
