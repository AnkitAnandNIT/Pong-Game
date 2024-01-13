import turtle

score_a=0
score_b=0

#window
window=turtle.Screen()
window.title("Pong Game By Venom")
window.setup(width=800,height=600)
window.bgcolor("purple")
window.tracer(0)

#score
score=turtle.Turtle()
score.speed(0)
score.penup()
score.goto(0,260)
score.hideturtle
score.write("Player A: 0   Player B: 0" , align="center",font=("Courier",25,"normal"))

#boards
board1=turtle.Turtle()
board1.shape("square")
board1.color("white")
board1.shapesize(stretch_len=1,stretch_wid=5)
board1.penup()
board1.goto(-350,0)
board1.speed(0)

board2=turtle.Turtle()
board2.shape("square")
board2.color("white")
board2.shapesize(stretch_len=1,stretch_wid=5)
board2.penup()
board2.goto(350,0)
board2.speed(0)

#ball
ball=turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_len=1,stretch_wid=1)
ball.penup()
ball.goto(0,0)
ball.speed(0)
ball.dx=0.15
ball.dy=0.15

#board function
def b1_go_up():
    y1=board1.ycor()
    y1+=25
    board1.sety(y1)

def b1_go_down():
    y1=board1.ycor()
    y1-=25
    board1.sety(y1)

def b2_go_up():
    y1=board2.ycor()
    y1+=25
    board2.sety(y1)

def b2_go_down():
    y1=board2.ycor()
    y1-=25
    board2.sety(y1)

#keyboard
window.listen()
window.onkeypress(b1_go_up, "w")
window.onkeypress(b1_go_down, "s")
window.onkeypress(b2_go_up, "Up")
window.onkeypress(b2_go_down, "Down")

#main
while True:
    window.update()

    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #boder
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy=-1*ball.dy

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy=-1*ball.dy
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx=-1*ball.dx
        score_a+=1
        score.clear()
        score.write("Player A:  {}  Player B:  {}".format(score_a,score_b), align="center",font=("Courier",25,"normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx=-1*ball.dx
        score_b+=1
        score.clear()
        score.write("Player A:  {}  Player B:  {}".format(score_a,score_b), align="center",font=("Courier",25,"normal"))

    if board1.ycor()>250:
        board1.sety(250)
    
    if board1.ycor()<-250:
        board1.sety(-250)
    
    if board2.ycor()>250:
        board2.sety(250)
    
    if board2.ycor()<-250:
        board2.sety(-250)

    #hit
    if (ball.xcor()<-335 and ball.xcor()>-345) and (ball.ycor()<board1.ycor()+45 and ball.ycor()>board1.ycor()-45):
        ball.goto(-335,board1.ycor())
        ball.dx=-1*ball.dx

    if (ball.xcor()>335 and ball.xcor()<345) and (ball.ycor()<board2.ycor()+45 and ball.ycor()>board2.ycor()-45):
        ball.goto(335,board2.ycor())
        ball.dx=-1*ball.dx