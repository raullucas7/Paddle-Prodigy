import turtle

def screen_setup ():
    
    pg = turtle.Screen()
    
    pg.title("Paddle Prodigy")
    pg.bigcolor("white")
    pg.setup(width=800, height=600)
    pg.tracer(0)
    
    return pg

def create_paddle(x, y):
    
    paddle = turtle.Turtle()
    
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("black")
    paddle.shapesize(stretch_wid = 5, stretch_len = 1)
    
    paddle.penup()
    paddle.goto(x, y)
    
    return paddle

