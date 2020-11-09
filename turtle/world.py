print ('Module Turtle loaded')
import turtle
import random

v = turtle.Turtle()
v.color('red','black')
def rect_side():
    for x in range(2):
        v.right(90)
        v.fd(201)

# v.up()

# v.fd(101)
# v.down()
# rect_side()
# v.right(90)
# v.fd(401)
# rect_side()

v.up()
# v.goto(random.randrange(-99,99),random.randrange(-199,199))
v.setheading(90)
rand_list = []

def randomspot():

    global rand_list
    rand_list = []
   

    for i in range(random.randrange(0,10),10):
        x1 = random.randrange(-99,99)
        y1 = random.randrange(-199,199)

        rand_list.append((x1,y1))
    return rand_list

def print_obstacles():
    global rand_list
    pos_list = []
    index_list = []
    rand_list = randomspot()
    v.speed(0)
    g = -200
    t = 0
    y = 0
    for o in range(20):
        u = -100   
        for z in range(10):
            pos_list.append((u,g))
            index_list.append((t,y))
            v.goto(u,g)
            v.down()
            v.fd(20)
            v.right(90)
            v.fd(20)
            v.right(90)
            v.fd(20)
            v.right(90)
            v.fd(20)
            v.right(90)
            v.fd(20)
            v.up()

            u += 20
            y += 1
            
        g += 20
        t += 1
    print(pos_list)
    print('---------------index--------------')
    print(index_list)
    return pos_list

pos_list = print_obstacles()

v.home()

# def up():
#     --

# def down():
#     --

# def left():
#     --

# def right():
#     --
# for an in range(8):
#     v.right(90)
#     for p in range(40):
#         pos = random.choice(pos_list)
        
#         v.color('white')
#         v.goto(pos)
#         v.down()
#         v.fd(20)
#         v.goto(pos)
#         v.fd(20)
#         v.up()
    
# for p in pos_list:
#     v.color('white')
#     v.goto(p)
#     if p[1] == -200 and p[1] == -100 or p[1] == -200 or p[1] == -100:
#         v.forward(20)
#         v.right(90)
#         v.down()
#         v.fd(20)
#         v.goto(p)
#         v.fd(20)
#         v.up()



v.setheading(90)  



# def is_position_blocked(x,y):
    
#     rand_list = randomspot() 

#     for v in rand_list:
         
#         if x in range(v[0],v[0]+5) and y in range(v[1],v[1]+5):
#             print('game over')
#             return True
#         else:
#             return False 
#print(rand_list)
x = int(input('Enter x position '))
y = int(input('Enter y position '))

v.goto(x,y)
re = is_position_blocked(x,y)

name = input("enter your name")
