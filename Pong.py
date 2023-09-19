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

# Bola

bola = turtle.Turtle()
bola.speed()
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)

# Funções para fazer com que as barras se movam

#Barra A
def barra_a_cima():
    y = barra_a.ycor()
    y += 20
    barra_a.sety(y)

def barra_a_baixo():
    y = barra_a.ycor()
    y -= 20
    barra_a.sety(y)

#Barra B

def barra_b_cima():
    y = barra_b.ycor()
    y += 20
    barra_b.sety(y)

def barra_b_baixo():
    y = barra_b.ycor()
    y -= 20
    barra_b.sety(y)

# Definição das teclas

tela.listen()
tela.onkeypress(barra_a_cima, "w")

tela.listen()
tela.onkeypress(barra_a_baixo, "s")

tela.listen()
tela.onkeypress(barra_b_cima, "Up")

tela.listen()
tela.onkeypress(barra_b_baixo, "Down")

# Main game loop
while True:
    tela.update()