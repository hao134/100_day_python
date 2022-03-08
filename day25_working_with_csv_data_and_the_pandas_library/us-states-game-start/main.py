import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
guessed_states = []
all_states = data.state.to_list()
state_xcor = data.x.to_list()
state_ycor = data.y.to_list()

# def write_state(state_name, statex_cor, statey_cor):
#     turtle.hideturtle()
#     turtle.penup()
#     turtle.goto(statex_cor, statey_cor)
#     turtle.write(state_name, align="center", font=("Courier", 10, "normal"))


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the State {len(guessed_states)}/50",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center", font=("Courier", 10, "normal"))

