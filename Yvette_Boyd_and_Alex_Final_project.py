import tkinter as tk
'''Created by Alex Luu and Yvette Boyd'''






#Global variables
GUI = None
 
current_scene_index = 0

choice_buttons = []

paragraph_label = None

scenes = []

character_selected = False

buttons_to_destroy = []



class Character:
    "class for my two characters"


    def __init__(self, name, color):
        "initializes the function"
        self.name = name
        self.color = color

# Creating characters

c1 = Character("Tom", "blue")
c2 = Character("Jen", "pink")

#FOR THE WELCOME PAGE

# Incorporate Boolean function with yes or no
def make_a_choice(choice):
    "user makes a choice and if True a new window will be created and the current will be destroyed, and if False, the current window will be destroyed"
    if choice:  # TRUE
        menu.withdraw()
        character_selected = True
        question_set = "two_buttons"
        character_window = character_page(question_set)
        return character_window
    else:  # FALSE
        menu.withdraw()

# User Defined Function for yes and no buttons
def yes_click(argument=None):
    global character_selected
    "user clicks yes button"
    make_a_choice(True)
    print("WOOOOOO")

def no_click(argument=None):
    "user clicks no button"
    print("Aww, goodbye")
    make_a_choice(False)

#FOR THE ENDING PAGE

# Global variables

ending_question_label = None

current_scene_index = 0


scenes_2 = [{"question": "Thank you for staying until the end! If you haven't noticed or wanted to know, this project is a mixture of our knowlegde of tkinter, gui, and our current knowledge of python."},
          {"question": "When we first thought of our proposal idea for this project, we really wanted to incorporate pyschology. How we ending up doing that is incorporating a storyline based experience."},
          {"question": "This storyline experience is based off of a mixture of our personal experience of what social anxiety is or what it could look like to other people."},
          {"question": "The main setting was going through highschool because we personally felt that highschool provided us the most social anxiety and even introduced social anxiety to us. We also feel like that might be the case for others as well."},
          {"question": "Well we are glad that you played our game and thank you for reading our creator's note. PS. Yvette and Alex"}
]

# Function for the ending game
def create_ending_GUI():
    "the ending of the game"
    global ending_GUI, ending_question_label, current_scene_index

    current_scene_index = 0
    
    # Create a new GUI for the ending
    ending_GUI = tk.Tk()
    ending_GUI.title("Game Ending")
    ending_GUI.geometry("1000x1000")
    ending_GUI.configure(bg="white")
    ending_GUI.resizable(True, True)
    
    # Create a label to display the ending question
    global ending_question_label
    
    ending_question_label = tk.Label(ending_GUI, text="", font=("Arial", 16), wraplength=800, justify="left")
    ending_question_label.grid(row=0, column=0, padx=60, pady=20,columnspan=2)

    # Creates "Play" button
    play_button = tk.Button(ending_GUI, text="Play", command=play_button_click, width=10, height=2)
    play_button.grid(row=1, column=1, sticky="se", padx=5, pady=5)


    # Configure the last column 
    ending_GUI.columnconfigure(1, weight=1)
    
    # Create a "Next" button for further progression
    next_button_2 = tk.Button(ending_GUI, text="Next", command=next_button_2_click, width=10, height=2)
    next_button_2.grid(row=0, column=1, sticky="ne", padx=5, pady=5) 



    # Start the ending GUI loop
    ending_GUI.mainloop()

def play_button_click():
    "user clicked the play button"
    update_scene_ending(scenes_2)
        
def update_scene_ending(scenes_2):
        "updates the scene"
        global ending_question_label, current_scene_index

        if 0 <= current_scene_index < len(scenes_2):
            # Get the current scene
            current_scene = scenes_2[current_scene_index]

            # Display the question
            ending_question_label.config(text=current_scene["question"])
           
            
                    
# Function for the Next button_2 click in the ending
def next_button_2_click():
    " button_2 is clicked in the ending"
    global current_scene_index

    # Check if there are more scenes
    if 0 <= current_scene_index < len(scenes_2) - 1:
        current_scene_index += 1
        update_scene_ending(scenes_2)
        
        print(f"Current scene index after update: {current_scene_index}")
    else:
        # If no more scenes, destroy the ending GUI
        display_quit_button()
        
       
# Function to display quit button
def display_quit_button():
    "displays the quit button"
    global ending_GUI
    
    # Creates "Quit" button
    quit_button = tk.Button(ending_GUI, text="Quit", command=ending_GUI.destroy, width=10, height=2)
    quit_button.grid(row=1, column=1, sticky="se", padx=5, pady=5)        



current_scene_index = 0

choice_buttons = []

buttons_to_destroy = []

#create_ending_GUI()

#THE MAIN GAME
def main_game():
    "this is the visual of the game"
    global GUI, scenes, current_scene_index, choice_buttons


    GUI = tk.Tk()
    GUI.title("Returning Home")
    GUI.geometry("1000x1000")
    GUI.configure(bg="skyblue")
    GUI.resizable(True, True)

    # Where the main screen is
    GUI.columnconfigure(0, weight=2)
    GUI.rowconfigure(0, weight=10)

    # Function to handle button clicks
    def button_click(choice):
        global current_scene_index
      
        # Process the choice here if needed
        print(f"Choice selected: {choice}")

        # Move to the next scene or perform other actions
        if current_scene_index < len(scenes):
            current_scene_index += 1
            update_scene()


 # Function to update the scene
    def update_scene():
       # global choice_buttons
        global  choice_buttons, buttons_to_destroy, GUI

        # Clear existing buttons
        for button in choice_buttons:
            button.destroy()

        # Clear the list of buttons to destroy
        buttons_to_destroy = []

        # Get the current scene
        current_scene = scenes[current_scene_index]

        # Display the question
        question_label.config(text=current_scene["question"])

        # Determine the number of choices and create the corresponding buttons
        num_choices = len(current_scene["choices"])


        if num_choices == 2:
            two_buttons(GUI, current_scene["choices"], button_click)
        elif num_choices == 4:
            four_buttons(GUI, current_scene["choices"], button_click)
    
            # Create a "Next" button
           
            next_button = tk.Button(GUI, text="Next", command=next_button_click, width=10, height=2)
            next_button.grid(row=0, column=1, sticky="ne", padx=5, pady=5)

            #Adding the button to the list for destruction
            buttons_to_destroy.append(next_button)




#function for the Next button click
    def next_button_click():
        "progress the game with a click of a button"
        global current_scene_index, GUI

        #Check is there are any more scenes
        if current_scene_index < len(scenes) - 1:
            current_scene_index += 1
            update_scene()
        else:
             # If no more scenes, destroy the main GUI and show the ending GUI
            GUI.destroy()
            create_ending_GUI()

    

    # Create a label to display the question
    question_label = tk.Label(GUI, text="", font=("Arial", 16), wraplength=800, justify="left")
    question_label.grid(row=0, column=0, padx=60, pady=20,columnspan=2)

    # Create buttons based on the current scene
    update_scene()

    # Start the main event loop
    GUI.mainloop()


#STORYLINE BEING PUT INTO PLACE

# List of scenes
scenes = [
    {"question": " Your eyes are numb, your body feels heavy, and you can’t help but feel sleepy. You don’t want to wake up to start your day of school. You don’t want to grow up and be somebody new. You want to stay as little as you can and enjoy your life as much as you can. There’s so much work to do, yet you procrastinate what you need to do. What will you do?",
     "choices": ["1) Wake up and start your day.", "2) Sleep in and be late for school."]},

  
    {"question": "You hesitantly move the blanket covering your body from the cold, moving your feet to touch the floor, and sitting up on your bed looking around. You don’t really want to go to school, but you just want to finish high school as quickly as you can and get it done with. As you’re sitting up, you feel your body slowly waking up. You look at the clock to see that it’s 6:45 AM. How will you start your day?",
     "choices": ["1) Brush your teeth.", "3) Skip breakfast.", "2) Eat breakfast.", "4) Change your clothes."]},

  
    {"question": "You walk towards your bathroom that’s connected to your room. You first wash the tiredness off your eyes. You feel more awake now. You first wash your toothbrush, then squeeze some toothpaste on your toothbrush, and then pour some water onto your toothbrush again. You manually brush your teeth, making sure you get every crevice. What will you do now?",
     "choices": ["1) Eat breakfast.", "3) Change your clothes.", "2) Skip breakfast.", "4) Go to school."]},

  
    {"question": "You’re very hungry. You walk toward your kitchen in a desperate manner to fill the emptiness in your stomach. You walk into the kitchen to see it empty, your parents probably left for work already. You look around for food, like a raccoon scavenging for food in a trashcan. What will you eat?",
     "choices": ["1) Cereal with milk.", "3) A pop tart.", "2) A croissant.", "4) A PBJ sandwich."]},

  
    {"question": "You’ve decided you’re not very hungry this morning, so you won’t be eating breakfast. What will you do next?",
     "choices": ["1) Brush your teeth.", "3) Change your clothes.", "2) Eat breakfast.", "4) Go to school."]},

  
    {"question": "You decided to get out of your PJs and change into a new set of clothes. What will you do now?",
     "choices": ["1) Brush your teeth.", "3) Skip breakfast.", "2) Eat breakfast.", "4) Go to school."]},

    # This scene has no choices

    {"question": "You don’t feel like waking up, you let the cold embrace you and you continue to sleep. How long you slept in? You don’t know. You just know that this is the best sleep you’ve had in a long while. When you wake up, you find yourself submerged in black liquid. You’re sinking slowly and when you attempt to move, you sink ever faster. You don’t know what to do, but to let the black liquid embrace you. You wake up in a cold sweat. You don’t know what just happened. You look at your clock and see that it’s 9:23 AM and school starts at 8:00 AM. You missed the first period which ends at 9:30 AM and the second period starts at 9:40 AM. You didn’t even get the chance to brush your teeth, eat breakfast, or change clothes. You quickly get into your car and rush to school before the second period starts.",
     "choices": ["No choices for this one","No choices for this one","No choices for this one","No choices for this one"]},  

    # This scene has no choices

    {"question": "You’re now going to head to school. The bus already left and walking to school with take an hour. Classes start at 8:00 AM and it’s 7:45 AM and it takes you about 10 minutes to drive to school. You get in your car to start heading to school. You park your car in the parking lot, and you look at the dashboard to see that it’s 7:57. You quickly get out of your car to head to class. Your first period is Pre-Calculus. You walk into class and instantly sit in the front row of the class because all the seats in the back were taken.",
     "choices": ["No choices for this one","No choices for this one","No choices for this one","No choices for this one"] } ,  

  
    {"question": "Today in Pre-Calculus, you have a test. You have 1 hour and ten minutes to take your test. Scavenging your backpack you realize that you left your calculator at home. Even though you are sitting in the front of the class, you are self-conscious about getting up and asking for a spare calculator. Will you?",
     "choices": ["A) Take the test without a calculator.", "B) Ask for a calculator.", "C) Get up and take a calculator.", "D) Leave the test blank."]},

  
    {"question": "After your Pre-Calculus class, you look at your daily planner and see that you have a Study Hall at 10:35. As you approach the Classroom, you walk inside and head to the back because that is where your assigned seat resides. As you approach your seat, realize that a football player takes your assigned seat. What will you do?",
     "choices": ["A) Tell him to get up.", "B) Ask him nicely if he could give you your seat back.", "C) Pick another person's seat.", "D) Tell the teacher about him."]},

  
    {"question": "You ended up leaving your previous class a little later than expected due to chatting with the teacher about the next test. You realize that your next class, biology starts in 3 minutes and the hallways are packed with students. It is as if there is no room to move through the halls. What will you do?",
     "choices": ["A) Push through the crowds of students.", "B) Ask nicely if people could move.", "N/A", "N/A"]},

  
    {"question": "You finally reached your biology class; however, you are late. The teacher is not impressed with your delay and in front of the class asks you why are you late. You explain how the hallways were full of late students, making it hard to get around. The teacher then asks you to solve a question on the board. You have social anxiety and hate being in front of people let alone solving a problem. What do you do?",
     "choices": ["A) Tell your teacher that you don't know the answer.", "B) Tell your teacher that you don't want to do it.", "N/A", "N/A"]},

  
    {"question": "Finally, you arrive at your favorite class of the day, History. You have been told to find a group of 4 people and discuss why you think democracy is better than communism and who the United States represents as a democracy. You see a girl sitting alone at the back of the class. Wondering if you should ask her to be in your group, intrusive thoughts consume your head. These thoughts consist of, what if she doesn't want to be in my group? what if she doesn't like how I dress? If she says no? Will I be in a group alone? As these thoughts come across your mind, you stop in your tracks and need to decide. Will you ask her to be in your group?",
     "choices": ["A) Yes", "B) No", "N/A", "N/A"]},

  
    {"question": "Unfortunately, it is time for Physics; however, you have a friend in the class. You walk into the classroom keeping an eye out for your friend and realize that your prompt for the class time is to get into groups and recreate one of Newton's Laws of Motion. To get into groups, the teacher asks who would like to volunteer to be in the first group. None raise their hand, therefore the teacher decides that he will pick out sticks, and that will decide the group if no one volunteers. It is silent in the room and you are worried that you won't get into a group with your friend. What will you do?",
     "choices": ["A) Raise your hand.", "B) Let your name be picked out by sticks.", "N/A", "N/A"]},

  
    {"question": "The bell rang; it is time for lunch. You get up from your seat and quickly pack up. Looking around you notice that everyone else is rushing and practically speed-walking to the lunchroom. As you leave the classroom you see some people running. You think to yourself, The lines are probably going to be long today if people are running. What will you do?",
     "choices": ["A) Run to the lunchroom and get your food faster", "B) Walk to the lunchroom and be stuck in the line", "N/A", "N/A"]},

  
    {"question": "After you get your food, you meet up with your friends. You all decide that you want to sit outside and eat your food. Walking over to a large table outside, you place your food down first and then your backpack. While you are getting ready to sit down and eat your food, another person walks up to you and says, Hey, this is our usual Table so you need to get up and eat your food somewhere else. What do you do?",
     "choices": ["A) Argue with them and stay", "B) Pick up your food and go", "N/A", "N/A"]},

  
    {"question": "Finally, it is time to go home. After a long stressful day of school and people, you cannot wait for that bus ride. The bus can sometimes provide a little bit of anxiety. Personally, you want to sit in the seats closest to the front of the bus because the seats are bigger versus the back. The bell rang. It is time to head to the bus loop. Knowing this what will you do?",
     "choices": ["A) Rush to the bus", "B) Slowly walk to the bus", "N/A", "N/A"]},

  
    {"question": "You made it on the bus and you managed to score a seat in the front of the bus. After a long day of conversing with people, you decided that on this bus ride, you want to just relax and not have to interact with anyone. That means that you're hoping that someone does not sit next to you. A bunch of students enter the bus and soon the bus starts to fill up, but there are spaces in the back open. A student asks you if they can sit next to you. What will you say?",
     "choices": ["A) Sure", "B) Sorry, can you find another seat?", "N/A", "N/A"]},

  
    {"question": "You finally made it home after a tiring day of school. You want to wind down and just be in your room because your social battery is spent. You decide to go to your room and start up your personal computer. You start to play GTA, and your someone keeps burning your cars. What will you do?",
     "choices": ["A) Get them back.", "B) Run away and keep playing GTA.", "N/A", "N/A"]}
]

#HERE ARE THE START OF OUR BUTTONS FOR OUR GAME

#defining the buttons
def two_buttons(gui, choices, button_click=None):
    global GUI

    # Creates 2 buttons
    x = "normal"
    button1 = tk.Button(gui, text=choices[0], bg="#6288a6", fg="white", state=x, width=5, height=10,
                        command=lambda: button_click(choices[0]) )#if button_click else None)
    button2 = tk.Button(gui, text=choices[1], bg="#6288a6", fg="white", state=x, width=5, height=10,
                        command=lambda: button_click(choices[1])) #if button_click else None)

    # Place the two buttons in the row below the question label
    button1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    button2.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    # Configure the grid
    gui.columnconfigure(0, weight=1)
    gui.columnconfigure(1, weight=1)
    gui.rowconfigure(1, weight=1)


def four_buttons(gui, choices, button_click=None):
    global GUI

    # Makes 4 buttons
    x = "normal"
    button1 = tk.Button(gui, text=choices[0], bg="#6288a6", fg="white", state=x, width=5, height=10,
                        command=lambda: button_click(choices[0]) )
    button2 = tk.Button(gui, text=choices[1], bg="#6288a6", fg="white", state=x, width=5, height=10,
                        command=lambda: button_click(choices[1])) #if button_click else None
    button3 = tk.Button(gui, text=choices[2], bg="#6288a6", fg="white", state=x, width=5, height=10,
                        command=lambda: button_click(choices[2])) #if button_click else None
    button4 = tk.Button(gui, text=choices[3], bg="#6288a6", fg="white", state=x, width=5, height=10,
                        command=lambda: button_click(choices[3])) #if button_click else None

    # Places the 4 buttons in the row below the question label
    button1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    button2.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
    button3.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
    button4.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

  
    # Configure the grid
    gui.columnconfigure(0, weight=1)
    gui.columnconfigure(1, weight=1)
    gui.rowconfigure(1, weight=1)
    gui.rowconfigure(2, weight=1)



def select_character(character_window, question_set):
    "when clicking either Tom or Jen, it will close and open the main game"
    global GUI
    character_window.withdraw()
    main_game()


def clicked_tom(character_window):
    "user clicks on the Tom button"
    select_character(character_window)


def clicked_Jen(character_window):
    "user clicks on the Jen button"
    select_character(character_window)


def character_page(question_set):
    "Visual for picking your characters"
    global character_selected
  
    if not character_selected:
        character = tk.Tk()
        character.minsize(900, 750)
        character.title("Pick a Character")

    # Blue box above Tom Button
    canvas = tk.Canvas(character, width=200, height=100, bg="blue")
    canvas.place(relx=0.3, rely=0.35, anchor=tk.CENTER)

    # Pink box above Jen button
    canvas_jen = tk.Canvas(character, width=200, height=100, bg="pink")
    canvas_jen.place(relx=0.7, rely=0.35, anchor=tk.CENTER)

# Create Buttons for characters
    "below are the two buttons for Tom and Jen"

   # BUTTON FOR TOM
    button_Tom = tk.Button(character, text="Tom", command=lambda: select_character(character, question_set),
                               width=15, height=3, font=10)
    button_Tom.bind("<Button-1>", lambda event, q_set=question_set: select_character(character, q_set))
    button_Tom.place(relx=0.3, rely=0.6, anchor=tk.CENTER)

    # BUTTON FOR JEN
    button_Jen = tk.Button(character, text="Jen", command=lambda: select_character(character, question_set),
                               width=15, height=3, font=10)
    button_Jen.bind("<Button-1>", lambda event, q_set=question_set: select_character(character, q_set))
    button_Jen.place(relx=0.7, rely=0.6, anchor=tk.CENTER)

    return character



# Welcome screen
menu = tk.Tk()
menu.minsize(900, 750)
menu.title("Main Menu")

label = tk.Label(menu, text="Would You Like To Play Our Game? :>", font=("Arial", 28))
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button_yes = tk.Button(menu, text="Yes", command=yes_click, width=15, height=3, font=10)
button_yes.bind("<Button-1>", yes_click)
button_yes.place(relx=0.4, rely=0.6, anchor=tk.CENTER)

button_no = tk.Button(menu, text="No", command=no_click, width=15, height=3, font=10)
button_no.bind("<Button-1>", no_click)
button_no.place(relx=0.6, rely=0.6, anchor=tk.CENTER)

menu.mainloop()


