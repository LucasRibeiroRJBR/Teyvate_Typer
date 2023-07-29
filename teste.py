import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('300x300')

        self.lb = ctk.CTkLabel(master=self,text='Metninizi aşağıya yazın')
        self.lb.grid(row=0,column=0)

if __name__ == '__main__':
    App().mainloop()