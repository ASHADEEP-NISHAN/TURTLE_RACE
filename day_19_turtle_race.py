from turtle import Turtle, Screen
screen = Screen()
screen.setup(height=400,width=500)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race")

position=[-70,-40,-10,20,50,80]
color=["Green","Purple","Yellow","Orange","Blue","Red"]
all_turtle=[]
import random
speed=[10,20,30,40]
for index in range(0,6):
    tim = Turtle("turtle")
    tim.color(color[index])
    tim.penup()
    tim.setposition(x=-230,y=position[index])
    all_turtle.append(tim)
is_race_on=False
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtle:
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color=turtle.pencolor()
            if user_bet.lower() != winning_color.lower():
                print(f"you lose! {winning_color} won the race")
            else:
                print(f"You Won! {winning_color} won the race")

screen.exitonclick()