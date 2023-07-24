import customtkinter as ctk
import tkinter.font as tkfont

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.mondstadt = ("Teyvat Neue",30)
        self.genshin = ("HYWenHei-85W",36,'bold')
        self.small_font = ('HYWenHei-85W', 30,'bold')
        self.teyvat = ("Teyvat Neue", 30)
        self.inazuma = ("Inazuma Neue", 30)
        self.sumeru = ("Sumeru Neue", 30)
        self.deshret = ("Deshret Neue", 30)
        self.khaenriah = ("Khaenriah Neue", 30)
        self.khaenriah_charm = ("Khaenriah Neue Chasm", 30)

        self.w = 800
        self.h = 600
        self.geometry(f"{self.w}x{self.h}+{int(self.winfo_screenwidth())/2}+{int(self.winfo_screenheight())/2}")
        
        
        self.vText = ctk.StringVar()

        self.lb_title = ctk.CTkLabel(master=self,text='Type your text below',font=self.genshin)
        
        self.frame_text = ctk.CTkFrame(master=self,border_width=3,width=180,height=500)
        self.lb_letreiro = ctk.CTkLabel(master=self.frame_text,text='',font=self.small_font)
        
        # ButtonRadios
        self.radio_var = ctk.IntVar(value=0)
        self.rb_mondstadt = ctk.CTkRadioButton(master=self, text="Mondstadt", command=self.idiom, variable= self.radio_var, value=0)
        self.rb_inazuma = ctk.CTkRadioButton(master=self, text="Inazuma", command=self.idiom, variable= self.radio_var, value=1)
        self.rb_sumeru = ctk.CTkRadioButton(master=self, text="Sumeru", command=self.idiom, variable= self.radio_var, value=2)
        self.rb_deshret = ctk.CTkRadioButton(master=self, text="Deshret", command=self.idiom, variable= self.radio_var, value=3)
        self.rb_khaenriah = ctk.CTkRadioButton(master=self, text="Khaenriah", command=self.idiom, variable= self.radio_var, value=4)
        self.rb_khaenriah_charm = ctk.CTkRadioButton(master=self, text="Khaenriah Charm", command=self.idiom, variable= self.radio_var, value=5)
        
        
        self.input_text = ctk.CTkEntry(master=self,textvariable=self.vText,width=750,font=self.small_font)
        self.bt_limpar = ctk.CTkButton(master=self,text='Limpar',command=lambda:self.limpar)
        self.input_text.bind('<KeyRelease>',self.fill_frame)

        # GRIDs
        self.grid_rowconfigure((0,1,2,3,4),weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5),weight=1)
        self.lb_title.grid(row=0,column=0,columnspan=6,padx=15,pady=15)
        self.frame_text.grid(row=1,column=0,columnspan=6,padx=15,pady=15,sticky='nsew')
        self.rb_mondstadt.grid(row=2,column=0)
        self.rb_inazuma.grid(row=2,column=1)
        self.rb_sumeru.grid(row=2,column=2)
        self.rb_deshret.grid(row=2,column=3)
        self.rb_khaenriah.grid(row=2,column=4)
        self.rb_khaenriah_charm.grid(row=2,column=5)
        self.input_text.grid(row=3,column=0,columnspan=6,pady=(0,15))
        self.bt_limpar.grid(row=4,column=0,columnspan=6)

        self.frame_text.grid_rowconfigure(0,weight=1)
        self.frame_text.grid_columnconfigure(0,weight=1)
        self.lb_letreiro.grid(row=0,column=0,padx=5,pady=5)



    def limpar(self):
        self.vText=''

    def fill_frame(self,event):
        t = self.input_text.get()
        self.lb_letreiro.configure(text=t)

    def idiom(self):
        match self.radio_var.get():
            case 0: self.lb_letreiro.configure(font=self.mondstadt)
            case 1: self.lb_letreiro.configure(font=self.inazuma)
            case 2: self.lb_letreiro.configure(font=self.sumeru)
            case 3: self.lb_letreiro.configure(font=self.deshret)
            case 4: self.lb_letreiro.configure(font=self.khaenriah)
            case 5: self.lb_letreiro.configure(font=self.khaenriah_charm)



if __name__ == '__main__':
    App().mainloop()


