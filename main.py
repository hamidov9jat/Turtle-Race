import turtle
from turtle import Turtle, Screen
from random import randint

screen = Screen()


def create_turtles(number: int, shape: str):
    turtles = []
    for _ in range(number):
        turtles.append(Turtle(shape=shape))
    return turtles


screen.setup(width=700, height=600)
my_bet = screen.textinput('Make your bet', 'Which turtle will win the race? Enter a colour: ')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []

if my_bet is None:
    th = Turtle('square')
    th.hideturtle()
    th.write("You didn't make bet!", align='center', font=('Times New Roman', 20, 'bold'))
else:
    # Create 6 turtles
    all_turtles = create_turtles(6, 'turtle')

    starting_x = -(screen.window_width() / 2 - 20)
    for turtle_index in range(6):
        # temp_t refers to the same object as all_turtles[turtle_index]
        temp_t = all_turtles[turtle_index]
        # print(temp_t)
        temp_t.color(colors[turtle_index])
        temp_t.penup()
        temp_t.goto(x=starting_x, y=y_positions[turtle_index])

    is_race_on = True
    while is_race_on:
        for turtle_ in all_turtles:
            if turtle_.xcor() > (screen.window_width() / 2 - turtle_.shapesize()[0] / 2):
                # print(screen.window_width() / 2)
                # print(turtle_.xcor())
                is_race_on = False
                winner_color = turtle_.pencolor()
                if my_bet == winner_color:
                    print(f"You've won! The winner is the {winner_color} turtle!")
                else:
                    print(f"You've lost! The winner is the {winner_color} turtle!")

            # Make each turtle move a random amount.
            rand_distance = randint(0, 10)
            turtle_.forward(rand_distance)

# screen.exitonclick()

turtle.done()
