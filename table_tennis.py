import turtle

def screen_setup ():
    
    pg = turtle.Screen()
    
    pg.title("Paddle Prodigy")
    pg.bigcolor("white")
    pg.setup(width=800, height=600)
    pg.tracer(0)
    
    return pg

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
    
    pong_ball = turtle.Turtle()
    
    pong_ball.speed(10)
    pong_ball.shape("square")
    pong_ball.color("black")
    
    pong_ball.penup()
    pong_ball.goto(0, 0)
    
    pong_ball.dx = 2
    pong_ball.dy = -2
    
    return pong_ball

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
    pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Georgia", 24, "italic"))

