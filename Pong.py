# Código feito com a biblioteca de turtle

import turtle

# Tela do jogo

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
bola.dx = 0.2
bola.dy = 0.2

# Placar

placar_a = 0

placar_b = 0

# Visual do placar

placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Jogador A = 0  Jogador B = 0", align="center", font=("Arial", 24, "normal"))

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

    # Movimentação da bola

    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Limite das bordas de cima e de baixo

    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    # bordas da direta e da esquerda
    
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        placar_a += 1
        placar.clear()
        placar.write("Jogador A = {}  Jogador B = {}".format(placar_a, placar_b), align="center", font=("Arial", 24, "normal"))


    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        placar_b += 1
        placar.clear()
        placar.write("Jogador A = {}  Jogador B = {}".format(placar_a, placar_b), align="center", font=("Arial", 24, "normal"))

    # Colisão das barras com a bola
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < barra_b.ycor() + 40 and bola.ycor() > barra_b.ycor() -40):
        bola.setx(340)
        bola.dx *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < barra_a.ycor() + 40 and bola.ycor() > barra_a.ycor() -40):
        bola.setx(-340)
        bola.dx *= -1
