from tkinter import *
from my_db import Database
from tkinter import messagebox
from my_api import *

class NLPApp:

    bg_color = 'black'

    def __init__(self):

        self.dbo = Database()

        self.apio = API()

        # login ka gui load
        self.root = Tk() # Tk is main class of tkinter
        self.root.title('NLP App')
        self.root.iconbitmap('images/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg=NLPApp.bg_color)

        self.login_gui()
        self.root.mainloop() # gui ko hold karta hai screen me

    def login_gui(self):
        # self.clear_screen()

        heading = Label(self.root, text='NLP App', bg=NLPApp.bg_color, fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))

        email = Label(self.root, text = 'Enter email')
        email.pack(pady=(10,10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5,10), ipady=5)

        password = Label(self.root, text = 'Enter password')
        password.pack(pady=(10,10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5,10), ipady=5)
    
        login_button = Button(self.root, text='Login', width=30, height=2, command=self.perform_login)
        login_button.pack(pady=(10,10))

        nam = Label(self.root, text='Not a member?')
        nam.pack(pady=(20,10))

        redirect_button = Button(self.root, text='Register now', command=self.register_gui)
        redirect_button.pack(pady=(10,10))

    def register_gui(self):
        self.clear_screen()

        heading = Label(self.root, text='NLP App', bg=NLPApp.bg_color, fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))

        name = Label(self.root, text = 'Enter name')
        name.pack(pady=(10,10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5,10), ipady=5)

        email = Label(self.root, text = 'Enter email')
        email.pack(pady=(10,10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5,10), ipady=5)

        password = Label(self.root, text = 'Enter password')
        password.pack(pady=(10,10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5,10), ipady=5)
    
        register_button = Button(self.root, text='Register', width=30, height=2, command=self.perform_registration)
        register_button.pack(pady=(10,10))

        aam = Label(self.root, text='Already a member?')
        aam.pack(pady=(20,10))

        redirect_button = Button(self.root, text='Login now', command=self.login_gui)
        redirect_button.pack(pady=(10,10))

    def clear_screen(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
    
        response = self.dbo.add_data(name.strip(), email.strip(), password.strip())

        if response:
            messagebox.showinfo('Success', 'Registration successful...Login?')
        else:
            messagebox.showerror('error', 'Email exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('Success', 'Login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Wrong info, Try again')

    # def home_gui(self):

    #     self.clear_screen()

    #     heading = Label(self.root, text='NLP App', bg=NLPApp.bg_color, fg='white')
    #     heading.pack(pady=(30,30))
    #     heading.configure(font=('verdana', 24, 'bold'))

    #     button1 = Button(self.root, text='Sentiment / Emotion Analysis', width=30, height=5, command=self.sentiment_gui)
    #     button1.pack(pady=(10,10))

    #     button2 = Button(self.root, text='NER (entity extraction)', width=30, height=5, command=self.NER_gui)
    #     button2.pack(pady=(10,10))

    #     button3 = Button(self.root, text='Language Detection', width=30, height=5, command=self.Language_Detection_gui)
    #     button3.pack(pady=(10,10))

    #     logout_button = Button(self.root, text='Logout', width=30, height=2, command=self.login_gui)
    #     logout_button.pack(pady=(10,10))

    # def sentiment_gui(self):

    #     self.clear_screen()

    #     heading1 = Label(self.root, text='NLP App', bg=NLPApp.bg_color, fg='white')
    #     heading1.pack(pady=(30,30))
    #     heading1.configure(font=('verdana', 24, 'bold'))

    #     heading2 = Label(self.root, text='Sentiment / Emotion Analysis', bg=NLPApp.bg_color, fg='white')    
    #     heading2.pack(pady=(10,10))
    #     heading2.configure(font=('verdana', 15))

    #     self.text = Label(self.root, text='Enter the text', bg=NLPApp.bg_color, fg='white')
    #     self.text.pack(pady=(10,30))
    #     self.text.configure(font=('verdana', 15))

    #     self.sentiment_input = Entry(self.root, width=50)
    #     self.sentiment_input.pack(pady=(5,10), ipady=20)

    #     analyse_button = Button(self.root, text='Analyse', width=20, height=1, command=self.do_sentiment_analysis)
    #     analyse_button.pack(pady=(10,10))

    #     self.sentiment_result = Label(self.root, text='', bg=NLPApp.bg_color, fg='white')
    #     self.sentiment_result.pack(pady=(10,30))
    #     self.sentiment_result.configure(font=('verdana', 15))

    #     go_back_button = Button(self.root, text='Go Back', width=20, height=1, command=self.home_gui)
    #     go_back_button.pack(pady=(10,10))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        print(text)

        result = self.apio.Sentiment_Analysis(text)
        print(result)

        self.sentiment_result['text'] = result

    def NER_gui(self):
        self.clear_screen()

        heading1 = Label(self.root, text='NLP App', bg=NLPApp.bg_color, fg='white')
        heading1.pack(pady=(30,30))
        heading1.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment / Emotion Analysis', bg=NLPApp.bg_color, fg='white')    
        heading2.pack(pady=(10,30))
        heading2.configure(font=('verdana', 15))

        text = Entry(self.root, width=50)
        text.pack(pady=(5,10), ipady=5)

        analyse_button = Button(self.root, text='Analyse', width=30, height=2)
        analyse_button.pack(pady=(10,10))

    def Language_Detection_gui(self):
        
        self.clear_screen()

        heading1 = Label(self.root, text='NLP App', bg=NLPApp.bg_color, fg='white')
        heading1.pack(pady=(30,30))
        heading1.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment / Emotion Analysis', bg=NLPApp.bg_color, fg='white')    
        heading2.pack(pady=(10,30))
        heading2.configure(font=('verdana', 15))

        text = Entry(self.root, width=50)
        text.pack(pady=(5,10), ipady=5)

        analyse_button = Button(self.root, text='Analyse', width=30, height=2)
        analyse_button.pack(pady=(10,10))
        

nlp = NLPApp()
