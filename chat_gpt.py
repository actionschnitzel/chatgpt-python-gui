import tkinter as tk
from tkinter import *
from tkinter import ttk
import openai
from tkinter import messagebox



class ApiPopup(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.resizable(0, 0)
        app_width = 400
        app_height = 150
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.title("")

        def write_key():

            if key_entry.get() == "Enter API Key" or key_entry.get() == "":
                messagebox.showerror(title=None, message="No API-KEY Found!")
                print("No Key Found!")
            else:
                f = open('key', 'w')
                f.write(f"api_key={key_entry.get()}")
                f.close()
                key_label.config(text=f"api_key={key_entry.get()}")
                set_key.config(state=DISABLED)

        key_entry = ttk.Entry(self)
        key_entry.pack(fill="x", padx=20, pady=20)
        key_entry.insert(0, "Enter API Key")

        set_key = ttk.Button(self, text="Set", command=write_key)
        set_key.pack()


class GptGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Chat-GPT Python GUI")
        self.geometry("900x900")
        self.resizable(0, 0)
        app_width = 900
        app_height = 900
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        def lines_that_contain(string, fp):
            return [line for line in fp if string in line]


        def key_check():
            first_child = ApiPopup(self)
            first_child.grab_set()

        def del_chet():
            chat_answer.delete("1.0", END)

        def ask_chatgtp():

            with open("key", "r") as key_file:
                for line in lines_that_contain("api_key=", key_file):
                    print(line)


            prompt = str(qeustion_entry.get())
            if qeustion_entry.get() == "":
                messagebox.showerror(title=None, message="No Input!")

            elif line == "api_key=None":
                messagebox.showerror(title=None, message="No API-Key!")

            else:

                openai.api_key = str(line[8:])
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

        global key_label
        key_label = Label(self, text="API-Key=None")
        key_label.pack(fill="x", padx=20, pady=20)

        with open("key") as key:
            api_key = key.read()
        
        if api_key == "api_key=None":
            key_label.config(text="Enter API-Key")
            print(api_key)
        else:
            key_label.config(text=api_key)
        

        #print(api_key[8:])






        key_entry = ttk.Button(self, text="Set API-Key", command=key_check)
        key_entry.pack(fill="x", padx=20, pady=10)

        anser_frame = ttk.Frame(self)
        anser_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        scroll_chat_answer = ttk.Scrollbar(anser_frame, orient='vertical')
        scroll_chat_answer.pack(side=RIGHT, fill='y')

        chat_answer = tk.Text(
            anser_frame, yscrollcommand=scroll_chat_answer.set)
        scroll_chat_answer.config(command=chat_answer.yview)
        chat_answer.pack(fill=tk.BOTH, expand=True)

        question_frame_frame = Frame(self, pady=20)
        question_frame_frame.pack(padx=20, fill="x")

        qeustion_entry = ttk.Entry(question_frame_frame)
        qeustion_entry.pack(fill="x", expand=True, side=LEFT)

        submit_btn = ttk.Button(question_frame_frame,
                                text="Submit", command=ask_chatgtp)
        submit_btn.pack()

        del_chat = ttk.Button(self, text="Clear Chat", command=del_chet)
        del_chat.pack(fill="x", padx=20, pady=10)


if __name__ == "__main__":
    app = GptGUI()
    app.mainloop()
