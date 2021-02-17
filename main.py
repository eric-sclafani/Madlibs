#Created by Eric Sclafani
#Please note that I did NOT create these stories. They are from: http://www.redkid.net/madlibs/
import sys
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

SMALL_FONT = ("Times New Roman", 11)
LARGE_FONT = ("Times New Roman", 16,)
STORY_FONT = ("Lucida Console", 16)
SELECTION_FONT = ("Algerian", 25)

class Madlibs(tk.Tk):
    """
    Constructs tkinter frame

    Parameters:
    -----------
    tk.Tk (class): creates instance of tkinter interpreter and root window.
    """
    def __init__(self):
        """
        Initializes frame features
        """
        tk.Tk.__init__(self)
        icon = tk.PhotoImage(file="Pictures/madlibsicon.png")
        self.iconphoto(False, icon)

        tk.Tk.wm_title(self, "Madlibs")
        tk.Tk.geometry(self, "1200x720+160+50")
        tk.Tk.resizable(self, 0,0)

        MLimage = Image.open("Pictures/madlibs.png")
        MLimage.thumbnail((490,200))#resizes and keeps aspect ratio
        MLimagePI = ImageTk.PhotoImage(MLimage)
        global picture
        picture = tk.Label(self, image=MLimagePI)
        picture.image = MLimagePI
        picture.pack()

        window = tk.Frame(self)
        window.pack(side="top", fill="both", expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (TitleScreen, StorySelect):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(TitleScreen)

    def show_frame(self, page):
        """Displays desired page

        Parameters:
        -----------
        page (class): page to be displayed
        """
        frame = self.frames[page]
        frame.tkraise()

class TitleScreen(tk.Frame):
    """Initializes the titlescreen page

    Parameters:
    -----------
    tk.Frame (class): creates subclass of "Frame" class in tkinter. Frames act like containers that hold widgets inside
    """
    def __init__(self, parent, controller):
        """
        Parameters:
        -----------
        parent: parent required by tkinter widgets 

        controller: lets different frames (classes) interact with each other

        """
        tk.Frame.__init__(self, parent)#parent = Madlibs
        button_play = tk.Button(self,
                                text="Play",
                                command=lambda: [picture.pack_forget(), controller.show_frame(StorySelect)],
                                width=25,
                                font=SMALL_FONT,
                                bg="Gold",
                                bd=5,
                                activebackground="Gold",)
        button_play.pack(expand=True)

        global button_rules
        button_rules = tk.Button(self,
                                 text="Rules",
                                 command=self.show_rules,
                                 width=25,
                                 font=SMALL_FONT,
                                 bg="Gold",
                                 bd=5,
                                 activebackground="Gold",)
        button_rules.pack(expand=True)

        global button_credits
        button_credits = tk.Button(self,
                                   text="Credits",
                                   command=self.show_credits,
                                   width=25,
                                   font=SMALL_FONT,
                                   bg="Gold",
                                   bd=5,
                                   activebackground="Gold",)
        button_credits.pack(expand=True)

        button_exit = tk.Button(self,
                                text="Exit",
                                command=lambda: sys.exit(),
                                width=25,
                                font=SMALL_FONT,
                                bg="Gold",
                                bd=5,
                                activebackground="Gold",)
        button_exit.pack(expand=True)

    def show_rules(self):
        """Rule button event handler. Displays rules when called"""
        rules = "In this game, you will be asked a series of prompts ranging from nouns and verbs to funny noises and celebrity names. \n\nProvide the funniest answers you can think of and enjoy the ridiculousness!"
        display_rules = tk.Message(self,
                                   text=rules,
                                   font=LARGE_FONT,
                                   relief="raised",
                                   bg="Gold",
                                   bd=3,
                                   justify="center")
        display_rules.place(x=5, y=50)
        button_rules.config(state="disabled", bg="Light Gray")

    def show_credits(self):
        """Credits button event handler. Displays credits when called"""
        credits = "This app was coded by \nEric Sclafani.\n\n I do not own Madlibs™. All credits go to Leonard Stern and Roger Price, the geniuses who created the game.\n\n I did not write the stories. They all come from http://www.redkid.net/madlibs/"
        dispay_credits = tk.Message(self,
                                    text=credits,
                                    font=LARGE_FONT,
                                    relief="raised",
                                    bg="Gold",
                                    bd=3,
                                    justify="center")
        dispay_credits.place(x=845, y=50)
        button_credits.config(state="disabled", bg="Light Gray")

class StorySelect(tk.Frame):
    """Initializes story select page

    Parameters:
    -----------
    tk.Frame (class): creates subclass of "Frame" class from tkinter
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.construct_titles()

    def construct_titles(self):
        """Constructs definitions and story buttons"""

        storage = {"s1":["Adjective", "Celebrity name", "Noun", "Adjective", "Verb ending in \"-ing\"", "Place", "Number", "Number", 
                         "Type of liquid", "Adjective", "Noun", "Verb (present tense)", "Adjective", "Noun", "Adjective","Verb (present tense)", "Adjective", "Adjective"],

                   "s2":["Noun", "Noun", "Food", "Noun","Adjective", "Noun", "Adjective", "Adjective", 
                         "Plural noun", "Noun", "Adjective", "Noun", "Adjective", "Type of liquid"],

                   "s3":["Body part", "Noun", "Adjective", "Female Celebrity", "Occupation", "Verb ending in \"ing\"", "Adjective", "Male Celebrity", 
                         "Adjective", "Occupation"],

                   "s4":["Noun", "Adjective", "Adjective", "Noun", "Noun", "Plural Noun", "Plural Noun", "Noun", 
                         "Body Part", "Plural Noun", "Adverb", "Plural Noun","Plural Noun", "Plural Noun", "A Letter"],

                   "s5":["Plural Noun", "Plural Noun", "Adjective", "Liquid", "Animal (plural)", "Adjective", "Funny noise #1", "Funny noise #2", 
                         "Adjective", "Plural Noun", "Animal", "Another Animal", "Body Part", "Plural Noun", "Adjective"],

                   "paths":["Pictures/airplane.png","Pictures/waitercustomer.png", "Pictures/emmy.png", "Pictures/eatdrinksick.png", "Pictures/zoo.png"],
                   } 

        defs = """
                            Definitions:

        Noun: A person, place, or thing. 
               
        Adjective: Words that describe nouns.

        Verb: A word used to describe an action.

        Adverb: A word that modifies a verb.

        Plurals: The plural version of any category.
        """

        widgets = []#storage for deletion

        display_defs = tk.Message(self, 
                                  text=defs,
                                  font=("Times New Roman", 16, "bold"),
                                  relief="raised",
                                  width=800,
                                  bg="Gold",
                                  bd=3)
        display_defs.place(x=753, y=4)
        widgets.append(display_defs)

        display_heading = tk.Message(self,
                                     text="Please select a prompt to begin:",
                                     font=("Times New Roman", 16, "bold"),
                                     width=500,
                                     bd=3,)
        display_heading.grid(sticky="W")
        widgets.append(display_heading)

        button_story1 = tk.Button(self,
                                  text="Pilot to Passengers",
                                  command=lambda: [self.construct_story(storage["s1"], storage["paths"][0], "~~~Pilot to Passengers~~~"),
                                                   self.remove_widgets(widgets, display_defs)],
                                  font=LARGE_FONT,
                                  width=25, 
                                  bg="Gold",
                                  bd=5,
                                  activebackground="Gold")
        button_story1.grid(sticky="W")
        widgets.append(button_story1)

        button_story2 = tk.Button(self,
                                  text="Waiter and Customer",
                                  command=lambda: [self.construct_story(storage["s2"], storage["paths"][1], "~~~Waiter and Customer~~~"),
                                                   self.remove_widgets(widgets, display_defs)],
                                  font=LARGE_FONT,
                                  width=25,
                                  bg="Gold",
                                  bd=5,
                                  activebackground="Gold")
        button_story2.grid(sticky="W")
        widgets.append(button_story2)

        button_story3 = tk.Button(self,
                                  text="Emmy Acceptance Speech",
                                  command=lambda: [self.construct_story(storage["s3"], storage["paths"][2], "~~~Emmy Acceptance Speech~~~"),
                                                   self.remove_widgets(widgets, display_defs)], 
                                  font=LARGE_FONT,
                                  width=25,
                                  bg="Gold",
                                  bd=5,
                                  activebackground="Gold")
        button_story3.grid(sticky="W")
        widgets.append(button_story3)

        button_story4 = tk.Button(self,
                                  text="Eat, Drink, and be Sick",
                                  command=lambda: [self.construct_story(storage["s4"], storage["paths"][3], "~~~Eat, Drink, and be Sick~~~"),
                                                   self.remove_widgets(widgets, display_defs)],
                                  font=LARGE_FONT,
                                  width=25,
                                  bg="Gold",
                                  bd=5,
                                  activebackground="Gold")
        button_story4.grid(sticky="W")
        widgets.append(button_story4)

        button_story5 = tk.Button(self,
                                  text="A Visit to the Zoo",
                                  command=lambda: [self.construct_story(storage["s5"], storage["paths"][4], "~~~A Visit to the Zoo~~~"),
                                                   self.remove_widgets(widgets, display_defs)],
                                  font=LARGE_FONT,
                                  width=25,
                                  bg="Gold",
                                  bd=5,
                                  activebackground="Gold")
        button_story5.grid(sticky="W")
        widgets.append(button_story5)

    def construct_story(self, questions, path, title):
        """Creates the story prompts, entry boxes and image.

        Parameters:
        ----------
        questions (list): list of questions for user

        path (string): directory for photo

        title (string): title of story

        """
        widgets = [] 
        self.entry_list = [ttk.Entry(self) for item in range(len(questions))]

        selection = tk.Label(self,
                             text=title,
                             font=SELECTION_FONT,
                             bd=3)
        selection.place(x=600, y=20)
        widgets.append(selection)

        IMG = Image.open(path)
        IMG.thumbnail((600,400))
        IMGPI = ImageTk.PhotoImage(IMG)
        IMGpic = tk.Label(self, image=IMGPI)
        IMGpic.image = IMGPI
        IMGpic.place(x=600, y=100)

        count = 0
        for prompt in questions:
            label = tk.Label(self, text=prompt + ":", font=LARGE_FONT)
            label.grid(column=0,row=count, pady=4, sticky="w")
            
            entry = self.entry_list[count]#set to a variable to be appended
            entry.grid(row=count, column=20)
            widgets.append(label)
            widgets.append(entry)
            count+=1

        submit = tk.Button(self, 
                           text="Submit",  
                           command=lambda: [self.submit_answers(title), self.remove_widgets(widgets, selection), IMGpic.place_forget()],
                           font=("Times New Roman", 16),
                           bg="Gold",
                           bd=5,
                           activebackground="Gold")
        submit.grid(column=20)
        widgets.append(submit)

    def remove_widgets(self, lst, place=False):
        """Removes widgets

        Parameters:
        -----------
        lst (list): Iterable to be removed.

        place (bool): When True, place_forget is used. Needed since grid_forget can only remove grid widgets, not place widgets.
        """
        for widget in lst:
            widget.grid_forget()
        if place:
            place.place_forget()

    def clear_entries(self):
        """Clears the text in the ttk entry boxes"""
        for entry in self.entry_list:
            entry.delete(0, "end")

    def submit_answers(self, title):
        """Submit button event handler. Appends answers to list and places them into each story accordingly.

        Parameters:
        -----------
        title (string): Title of story. Determines which story is displayed based on button press.
        """ 
        ans = [item.get() for item in self.entry_list]
         
        if title == "~~~Pilot to Passengers~~~":
            story1 = f"""
Pilot to Passengers

Ladies and gentlemen, welcome aboard {ans[0]} Airline's Flight 750. This is your captain and pilot, {ans[1]}.

The plane you are traveling on is the latest Strato-{ans[2]}, with four {ans[3]} engines. At present, we are {ans[4]} directly over {ans[5]}. 

Our speed is {ans[6]} miles per hour, and we are flying at an altitude of {ans[7]} feet. 

If you care for a cup of {ans[8]} or a good old-fashioned {ans[9]} sandwich, please push the {ans[10]} located over your seat, 

and our flight attendant will be glad to {ans[11]} on you. We have a {ans[12]} tailwind and will soon be flying through a heavy {ans[13]} storm.

So I'll have to ask you all to fasten your {ans[14]} belts and {ans[15]} your trays to the {ans[16]} position.

In the meantime, I hope you have a fantastic day and {ans[17]} trip.""" 
            text = story1

        if title == "~~~Waiter and Customer~~~":
            story2 = f"""
Waiter and Customer

CUSTOMER: Oh, waiter! would you please bring me a {ans[0]}? I want to see what today's specials are.

WAITER: Today's specials are cream of {ans[1]} soup and T-bone {ans[2]}. Does that sound good?

CUSTOMER: Yes, but I'll have the roast prime {ans[3]} of beef with the {ans[4]} pudding.

WAITER: We're out of that. How about a sizzling sirloin {ans[5]} and a {ans[6]} green salad?

CUSTOMER: No, thanks, I'd rather have the {ans[7]} fried chicken.

WAITER: Sorry, but we're out of that, too. How about soft-shell {ans[8]}?

CUSTOMER: No, thanks. Do you have any roast Long Island {ans[9]}?

WAITER: Sorry, no. Why don't you try our {ans[10]} goulash with homemade {ans[11]} sauce?

CUSTOMER: No, thanks. Just bring me four {ans[12]} egg sandwiches and a cup of black {ans[13]}."""
            text = story2

        if title == "~~~Emmy Acceptance Speech~~~":
            story3 = f"""
Emmy Acceptance Speech

Thank You! Thank you from the bottom of my {ans[0]}. I don't know what to say. I'm speechless. 

I truly didn't expect to win this {ans[1]}, certainly not with so many {ans[2]} actors competing in the same category. 

First and foremost, my thanks to {ans[3]}. You couldn't work with a better {ans[4]}. And I'm sure I wouldn't be {ans[5]} here tonight if it weren't for my {ans[6]} director. 

I must also thank {ans[7]}, who wrote a {ans[8]} script for me. 

Of course, none of this would be happening if it weren't for my agent, who convinced the network that I could play a 75 year-old, retired {ans[9]}."""
            text = story3

        if title == "~~~Eat, Drink, and be Sick~~~":
            story4 = f"""
Eat, Drink, and be Sick

An inspector from the Department of Health and {ans[0]} Services paid a surprise visit to  our {ans[1]} school cafeteria. 

The lunch special, prepared by our {ans[2]} dietician, was spaghetti and {ans[3]}-balls with a choice of either a {ans[4]} salad or French {ans[5]}. 

The inspector found the meat-{ans[6]} to be overcooked and discovered a live {ans[7]} in the fries, causing him to have a bad {ans[8]} ache. 

In response, he threw up all over his {ans[9]}. In his report, the inspector {ans[10]} recommended that the school cafeteria serve only nutritious {ans[11]} as well as low-calorie {ans[12]}, and that all of the saturated {ans[13]} be eliminated."""
            text = story4

        if title == "~~~A Visit to the Zoo~~~":
            story5 = f"""
A Visit to the Zoo

Zoos are places where wild {ans[0]} are kept in pens or cages so that {ans[1]} can come and look at them. 

There are two zoos in New York, one in the Bronx and one in {ans[2]} Park. The Park zoo is built around a large pond filled with clear sparkling {ans[3]}. 

You will see several {ans[4]} swimming in the pond and eating fish. When it is feeding time, all of the animals make {ans[5]} noises. 

The elephant goes {ans[6]} and the turtledoves go {ans[7]}. In one part of the zoo, there are {ans[8]} gorillas who love to eat {ans[9]}. 

In another building, there is a spotted African {ans[10]} that is so fast it can outrun a {ans[11]}. But my favorite animal is the hippopotamus.

It has a huge {ans[12]} and eats fifty pounds of {ans[13]} a day. You would never know that, technically, it's nothing but an oversized {ans[14]} pig."""
            text = story5

        show_story = tk.Label(self, text=text, wraplength=800, font=STORY_FONT)
        show_story.place(x=200,y=8)

        button_back = tk.Button(self, 
                                text="←Back", 
                                width=10, 
                                font=LARGE_FONT, 
                                bg="Gold",
                                bd=5, 
                                activebackground="Gold", 
                                command= lambda: [ 
                                ans.clear(),
                                show_story.destroy(),
                                button_back.destroy(),
                                self.clear_entries(),
                                self.construct_titles()])
        button_back.grid()

window = Madlibs()
window.mainloop()
