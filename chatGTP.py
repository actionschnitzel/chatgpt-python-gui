import tkinter as tk
from tkinter import *
from tkinter import ttk
import os


# Using the python library openai
import openai











class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root selfdow
        self.title("Chat-GTP Python GUI")
        self.geometry("900x900")

        
        def ask_chatgtp():
            openai.api_key = str(key_entry.get())
            # Now let's call the API
            prompt = str(qeustion_entry.get())

            completions = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )

            # Print the message
            message = completions.choices[0].text
            chat_answer.insert(END, f"You:\n\n{prompt}\n\n")
            chat_answer.insert(END, f"Chat:{message}\n\n")
            print(message)

        key_entry = Entry(self)
        key_entry.pack(fill="x",padx=20,pady=20)
        key_entry.insert(0,"Enter API Key")

        anser_frame = Frame(self)
        anser_frame.pack(padx=20,pady=20,fill=tk.BOTH,expand=True)

        v=Scrollbar(anser_frame, orient='vertical')
        v.pack(side=RIGHT, fill='y')


        chat_answer = Text(anser_frame, yscrollcommand=v.set)
        v.config(command=chat_answer.yview)
        chat_answer.pack(fill=tk.BOTH,expand=True)

        question_frame_frame = Frame(self,pady=20)
        question_frame_frame.pack(padx=20,fill="x")        

        qeustion_entry = Entry(question_frame_frame)
        qeustion_entry.pack(fill="x",expand=True,side=LEFT)

        submit_btn = Button(question_frame_frame,text="Submit",command=ask_chatgtp)
        submit_btn.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()



