import turtle

def spiral():
   wn = turtle.Screen()
   wn.bgcolor("lightgreen")
   tess = turtle.Turtle()
   tess.shape("turtle")
   tess.color("blue")

   tess.penup()                # This is new
   size = 20
   for i in range(30):
      tess.stamp()             # Leave an impression on the canvas
      size = size + 3          # Increase the size on every iteration
      tess.forward(size)       # Move tess along
      tess.right(24)           #  ...  and turn her
   turtle.done()

def square():
   silly = turtle.Turtle()

   silly.forward(50)
   silly.right(90)     # Rotate clockwise by 90 degrees

   silly.forward(50)
   silly.right(90)

   silly.forward(50)
   silly.right(90)

   silly.forward(50)
   silly.right(90)

   turtle.done()

def spiralStar():
   spiral = turtle.Turtle()

   for i in range(20):
       spiral.forward(i * 10)
       spiral.right(144)
    
   turtle.done()

def colorCircles():
   painter = turtle.Turtle()

   painter.pencolor("blue")

   for i in range(50):
       painter.forward(50)
       painter.left(123) # Let's go counterclockwise this time 
       
   painter.pencolor("red")
   for i in range(50):
       painter.forward(100)
       painter.left(123)
       
   turtle.done()

def lineCircle():
   ninja = turtle.Turtle()

   ninja.speed(10)

   for i in range(180):
       ninja.forward(100)
       ninja.right(30)
       ninja.forward(20)
       ninja.left(60)
       ninja.forward(50)
       ninja.right(30)
       
       ninja.penup()
       ninja.setposition(0, 0)
       ninja.pendown()
       
       ninja.right(2)
       
   turtle.done()

lineCircle()
