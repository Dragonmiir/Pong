import turtle

tela = turtle.Screen()
tela.title("Pong Estudo")
tela.bgcolor("black")
tela.setup(width=800, height=600)
tela.tracer(0)

# Barra A

barra_a = turtle.Turtle()
barra_a.speed(0)
barra_a.shape("square")
barra_a.color("white")
barra_a.shapesize(stretch_wid=5, stretch_len=1)
barra_a.penup()
barra_a.goto(-350, 0)

# Barra B

barra_b = turtle.Turtle()
barra_b.speed(0)
barra_b.shape("square")
barra_b.color("white")
barra_b.shapesize(stretch_wid=5, stretch_len=1)
barra_b.penup()
barra_b.goto(350, 0)

# Mina game loop
while True:
    tela.update()