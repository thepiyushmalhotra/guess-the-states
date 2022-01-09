import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic(r"E:\Coding World !!\Angela Yu Python\Python Practice\US States Game\us-states-game-start\blank_states_img.gif")
data = pd.read_csv(r"US States Game\us-states-game-start\50_states.csv")
df = pd.DataFrame(data)
all_states = df.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_state)}/50 States Correct", prompt = "What's another state's name?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    

