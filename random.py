import turtle

my_wn = turtle.Screen()
my_wn.bgcolor("light blue") #screen background color
my_wn.title("Turtle")
my_pen = turtle.Turtle()
my_pen.speed(0) 
size = 0
while True: #iterate loop
    for i in range(4):
        my_pen.fd(size + 2)
        my_pen.left(90)
    size = size + 3
