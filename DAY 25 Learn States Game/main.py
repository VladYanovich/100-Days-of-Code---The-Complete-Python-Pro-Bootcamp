import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
game_is_on = True
score = 0
states = pd.read_csv("50_states.csv")

print(states[states["state"] == "Arizona"]["x"].values[0])

guessed_states: list[str] = []
all_states = states.state.to_list()
def write_state(state: str) -> None:
    new_state = turtle.Turtle()
    new_state.hideturtle()
    new_state.penup()
    new_state.goto(
        states[states["state"] == str(state).title()]["x"].values[0],
        states[states["state"] == str(state).title()]["y"].values[0]
    )
    new_state.write(arg=str(state).capitalize(), align="center", font=("Calibre", 12, "bold"))

while game_is_on:
    answer_state = screen.textinput(title = f"{score}/50 States correct", prompt = "What's another state's name?")
    if str(answer_state).lower() == "exit":
        missing_states = pd.DataFrame([state for state in all_states if state not in guessed_states])
        missing_states.to_csv("states_to_learn.csv")
        break
    if str(answer_state).title() in states["state"].values and str(answer_state).title() not in guessed_states:
        print("correct", answer_state)
        score += 1
        write_state(answer_state)
        guessed_states.append(str(answer_state).title())
    else:
        print("wrong", answer_state, str(answer_state).title())
    if score == 50:
        game_is_on = False



turtle.exitonclick()
