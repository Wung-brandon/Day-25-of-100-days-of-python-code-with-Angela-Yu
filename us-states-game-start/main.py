import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S States Game")
#loading an image into the turtle screen 
image = "us-states-game-start/blank_states_img.gif"
screen.addshape(image)
t.shape(image)

df = pd.read_csv("us-states-game-start/50_states.csv")
all_state = df["state"].to_list()
#print(all_state)
#print(df)
guessed_state = []
while len(guessed_state) < 50: 
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 state.", prompt="What's another state's name?").title()
    #for states in state:
    if answer_state in all_state:
        guessed_state.append(answer_state)
        tr = t.Turtle()
        tr.hideturtle()
        tr.penup()
        #fetch out the row for which the user_answer corresponds to the coordinates of the states in the csv file 
        state_data = df[df["state"] == answer_state]
        tr.goto(int(state_data.x), int(state_data.y))
        #tr.write(state_data.state.item())
        tr.write(answer_state)
        
        #print("Correct answer")
    if answer_state == "Exit":
        #using the List Comprehension way for the code to be shorter
        missing_states = [state for state in all_state if state not in guessed_state]
        #missing_states = []
        #for state in all_state:
            #if state not in guessed_state:
                #missing_states.append(state)
        states_csv = pd.DataFrame(missing_states)
        states_csv.to_csv("States_to_learn.csv")
        print(missing_states)
        break
        
#print(answer_state)

screen.mainloop()