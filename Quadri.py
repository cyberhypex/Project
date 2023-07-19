import turtle as t

t.pensize(10)
t.pencolor("Black")
t.shape("turtle")

t.color("Blue")

t.screensize(600,600)
#rectangle
t.fillcolor("Violet")
t.begin_fill()
t.forward(150)
t.right(90)
t.forward(50)
t.right(90)
t.forward(150)
t.right(90)
t.forward(50)
t.end_fill()
#parallelogram
t.fillcolor("Indigo")
t.begin_fill()
t.penup()
t.forward(50)
t.pendown()
t.right(60)
t.forward(60)
t.right(60)
t.forward(30)
t.right(120)
t.forward(60)
t.right(60)
t.forward(30)
t.penup()
t.end_fill()

t.fillcolor("cyan")
t.forward(110)
t.pendown()
t.begin_fill()


#Square
for i in range(4):
    t.forward(60)
    t.right(90)
t.end_fill()
#rhombus

t.fillcolor("Green")
t.penup()
t.forward(110)
t.pendown()
t.begin_fill()
t.forward(30)
t.right(60)
t.forward(30)
t.right(120)
t.forward(30)
t.right(60)
t.forward(30)
t.end_fill()


t.fillcolor("Yellow")
t.penup()
t.forward(110)
t.pendown()



t.begin_fill()
# Draw the kite
t.right(60)
t.forward(80)
t.left(120)
t.forward(80)
t.left(70)
t.forward(60)
t.right(260)

t.forward(60)
t.end_fill()

#trapezium
t.fillcolor("Red")
t.penup()
t.backward(250)
t.pendown()
t.begin_fill()
t.right(60)
t.forward(50)
t.left(240)
t.forward(80)
t.right(120)
t.forward(50)
t.right(60)
t.forward(25)
t.end_fill()



t.penup()
t.backward(110)
t.pendown()
t.write("Quadrilaterals \n Serial number of drawing \n  1.Rectangle \n 2.parallelogram \n 3.Square \n 4.Rhombus \n 5.Kite \n 6.Trapezium")


t.done()