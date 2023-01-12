import tkinter as tk
from tkinter import *
from tkinter import ttk
import openai
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Chat-GPT Python GUI")
        self.geometry("900x900")
        
        
        
        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        
        def ask_chatgtp():
            
            
            # Now let's call the API
            prompt = str(qeustion_entry.get())
            if qeustion_entry.get() == "":
                messagebox.showerror(title=None, message="No Input!")

            elif key_entry.get() == "Enter API Key" or key_entry.get() == "":
                messagebox.showerror(title=None, message="No API-KEY Found!")
                qeustion_entry.delete(0, 'end')
                print("No Key Found!")
            else:
                openai.api_key = str(key_entry.get())
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
                chat_answer.yview(END)
                qeustion_entry.delete(0, 'end')
                print(message)



        key_entry = ttk.Entry(self)
        key_entry.pack(fill="x",padx=20,pady=20)
        key_entry.insert(0,"Enter API Key")

        anser_frame = ttk.Frame(self)
        anser_frame.pack(padx=20,pady=20,fill=tk.BOTH,expand=True)

        scroll_chat_answer=ttk.Scrollbar(anser_frame, orient='vertical')
        scroll_chat_answer.pack(side=RIGHT, fill='y')


        chat_answer = tk.Text(anser_frame, yscrollcommand=scroll_chat_answer.set)
        scroll_chat_answer.config(command=chat_answer.yview)
        chat_answer.pack(fill=tk.BOTH,expand=True)

        question_frame_frame = Frame(self,pady=20)
        question_frame_frame.pack(padx=20,fill="x")        

        qeustion_entry = ttk.Entry(question_frame_frame)
        qeustion_entry.pack(fill="x",expand=True,side=LEFT)

        submit_btn = ttk.Button(question_frame_frame,text="Submit",command=ask_chatgtp)
        submit_btn.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()



