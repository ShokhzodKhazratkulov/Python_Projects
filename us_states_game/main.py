import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        with open("states_to_learn.csv", mode="w") as data_file:
            for state in all_states:
                if state not in guessed_states:
                    data_file.write(f"{state}\n")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = states_data[states_data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)





