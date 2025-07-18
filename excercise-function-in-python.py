# Traffic Light Simulator with User Prompt
# Uses a while loop and asks the user: "What color is the light?"

# --- Functions for Each Light State ---

def red_light():
    print("Stop! The light is red.")

def yellow_light():
    print("Caution! The light is yellow.")

def green_light():
    print("Go! The light is green.")

# --- Function to Handle State Selection ---

def traffic_light(state):
    """
    Calls the correct function based on the input traffic light state.
    
    Parameters:
    - state (str): The color of the traffic light
    """
    state = state.lower()
    if state == "red":
        red_light()
    elif state == "yellow":
        yellow_light()
    elif state == "green":
        green_light()
    else:
        print(" Invalid light color. Please enter 'red', 'yellow', or 'green'.")

# --- User Interaction with a While Loop ---

print("===Traffic Light Control System===")
print("Type 'quit' to exit.")

while True:
    user_input = input("What color is the light? (red/yellow/green): ")
    
    if user_input.lower() == "quit":
        print("Exiting traffic light system. Goodbye!")
        break
    
    traffic_light(user_input)

# --- Optional: Add Your Own Creative Functions Below ---

def blink_light(color, times):
    """Blink the specified light a given number of times."""
    for _ in range(times):
        traffic_light(color)

# Example usage of the custom function after exiting the loop:
# blink_light("yellow", 3)
