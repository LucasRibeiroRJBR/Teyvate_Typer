#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import customtkinter as ctk
from utils import lang_flags as lf
from utils import window_fonts as f


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.w_width, self.w_height = 1200, 900

        self.screen_width, self.screen_height = self.winfo_screenwidth(), self.winfo_screenheight()

        x = (self.screen_width / 2) - (self.w_width / 2)
        y = (self.screen_height / 2 ) - (self.w_height / 2)

        self.geometry(f'{self.w_width}x{self.w_height}+{int(x)}+{int(y)}')

        self.vText = ctk.StringVar()

        self.lb_title = ctk.CTkLabel(master=self,text='Type your text below',font=f.genshin)

        self.lb_flag = ctk.CTkLabel(master=self,text='',image=lf.img_en_flag,width=50,height=50)
        self.cbx_lang = ctk.CTkComboBox(master=self,
                                        values=['English','French','German','Indonesian','Italian','Japanese','Korean','Mandarin','Portuguese','Russian','Spanish','Taiwanese','Thai','Turkish','Vietnamese'],
                                        font=f.genshin_dropdown,
                                        dropdown_font=f.genshin_dropdown,
                                        command=self.lang)
        self.cbx_lang.set('English')
        
        # Frame
        self.frame_text = ctk.CTkFrame(master=self,border_width=3,width=180,height=400)
        self.lb_letreiro = ctk.CTkLabel(master=self.frame_text,text='',font=f.mondstadt,justify='center',width=180,height=400,wraplength=700)
        self.vSliderTextSize = ctk.IntVar()
        self.slider_text_size = ctk.CTkSlider(master=self.frame_text,from_=0,to=100,number_of_steps=100,command=self.font_size,orientation='vertical',variable=self.vSliderTextSize)
        self.slider_text_size.set(18)
        self.lb_TextFont = ctk.CTkLabel(master=self.frame_text,text=self.vSliderTextSize.get())
        
        
        # ButtonRadios
        self.radio_var = ctk.IntVar(value=0)
        self.rb_mondstadt = ctk.CTkRadioButton(master=self, text="Mondstadt", font = f.genshin_small, command=self.idiom, variable= self.radio_var, value=0)
        self.rb_inazuma = ctk.CTkRadioButton(master=self, text="Inazuma", font = f.genshin_small, command=self.idiom, variable= self.radio_var, value=1)
        self.rb_sumeru = ctk.CTkRadioButton(master=self, text="Sumeru", font = f.genshin_small, command=self.idiom, variable= self.radio_var, value=2)
        self.rb_deshret = ctk.CTkRadioButton(master=self, text="Deshret", font = f.genshin_small, command=self.idiom, variable= self.radio_var, value=3)
        self.rb_khaenriah = ctk.CTkRadioButton(master=self, text="Khaenriah", font = f.genshin_small, command=self.idiom, variable= self.radio_var, value=4)
        self.rb_khaenriah_charm = ctk.CTkRadioButton(master=self, text="Khaenriah Charm", font = f.genshin_small, command=self.idiom, variable= self.radio_var, value=5)        
        
        self.input_text = ctk.CTkEntry(master=self,textvariable=self.vText,width=750,font=f.small_font)
        self.bt_limpar = ctk.CTkButton(master=self,text='Limpar',command=lambda:self.limpar)
        self.input_text.bind('<KeyRelease>',self.fill_frame)

        # GRIDs
        self.grid_rowconfigure((0,1,2,3,4),weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5),weight=1)
        self.lb_title.grid(row=0,column=0,columnspan=5,padx=15,pady=15)
        self.lb_flag.grid(row=0,column=4,sticky='e')
        self.cbx_lang.grid(row=0,column=5,sticky='e',padx=(0,15))
        self.frame_text.grid(row=1,column=0,columnspan=6,padx=15,pady=15,sticky='nsew')
        self.rb_mondstadt.grid(row=2,column=0)
        self.rb_inazuma.grid(row=2,column=1)
        self.rb_sumeru.grid(row=2,column=2)
        self.rb_deshret.grid(row=2,column=3)
        self.rb_khaenriah.grid(row=2,column=4)
        self.rb_khaenriah_charm.grid(row=2,column=5)
        self.input_text.grid(row=3,column=0,columnspan=6,pady=(0,15))
        self.bt_limpar.grid(row=4,column=0,columnspan=6)

        # Frame GRIDs
        self.frame_text.grid_rowconfigure((0,1),weight=1)
        self.frame_text.grid_columnconfigure(0,weight=2)
        self.frame_text.grid_columnconfigure(1,weight=1)
        self.lb_letreiro.grid(row=0,column=0,padx=5,pady=5)
        self.slider_text_size.grid(row=0,column=1,sticky='se',padx=15)
        self.lb_TextFont.grid(row=2,column=1,sticky='w',pady=15)

    def limpar(self):
        self.vText=''

    def fill_frame(self,event):
        t = self.input_text.get()
        self.lb_letreiro.configure(text=t)

    def font_size(self,v):
        self.lb_TextFont.configure(text=self.vSliderTextSize.get())
    def send_size(self):
        return self.vSliderTextSize.get()

    def idiom(self):
        match self.radio_var.get():
            case 0: self.lb_letreiro.configure(font=f.mondstadt)
            case 1: self.lb_letreiro.configure(font=f.inazuma)
            case 2: self.lb_letreiro.configure(font=f.sumeru)
            case 3: self.lb_letreiro.configure(font=f.deshret)
            case 4: self.lb_letreiro.configure(font=f.khaenriah)
            case 5: self.lb_letreiro.configure(font=f.khaenriah_charm)

    def lang(self,c):
        match c:
            case 'English':
                self.lb_title.configure(image='',text='Type your text below')
                self.lb_flag.configure(image=lf.img_en_flag)
                self.bt_limpar.configure(text='Clear')
            case 'French':
                self.lb_title.configure(image='',text='Tapez votre texte ci-dessous')
                self.lb_flag.configure(image=lf.img_fr_flag)
                self.bt_limpar.configure(text='Effacer')
            case 'German':
                self.lb_title.configure(image='',text='Geben Sie unten Ihren Text ein')
                self.lb_flag.configure(image=lf.img_de_flag)
                self.bt_limpar.configure(text='L�chen')
            case 'Indonesian':
                self.lb_title.configure(image='',text='Ketik teks Anda di bawah ini')
                self.lb_flag.configure(image=lf.img_id_flag)
            case 'Italian':
                self.lb_title.configure(image='',text='Digita il testo qui sotto')
                self.lb_flag.configure(image=lf.img_it_flag)
                self.bt_limpar.configure(text='Chiarire')
            case 'Japanese':
                self.lb_title.configure(image=lf.img_jp_lang,text='')
                self.lb_flag.configure(image=lf.img_jp_flag)
                self.bt_limpar.configure(text='????')
            case 'Korean':
                self.lb_title.configure(image=lf.img_kr_lang,text='')
                self.lb_flag.configure(image=lf.img_kr_flag)
            case 'Mandarin':
                self.lb_title.configure(image=lf.img_ch_lang,text='')
                self.lb_flag.configure(image=lf.img_cn_flag)
            case 'Portuguese':
                self.lb_title.configure(image='',text='Escreva seu texto abaixo')
                self.lb_flag.configure(image=lf.img_pt_flag)
                self.bt_limpar.configure(text='Limpar')
            case 'Russian':
                self.lb_title.configure(image=lf.img_ru_lang,text='')
                self.lb_flag.configure(image=lf.img_ru_flag)
            case 'Spanish':
                self.lb_title.configure(image='',text='Escribe tu texto abajo')
                self.lb_flag.configure(image=lf.img_sp_flag)
                self.bt_limpar.configure(text='Limpiar')
            case 'Taiwanese':
                self.lb_title.configure(image=lf.img_tw_lang,text='')
                self.lb_flag.configure(image=lf.img_tw_flag)
            case 'Thai':
                self.lb_title.configure(image=lf.img_th_lang,text='')
                self.lb_flag.configure(image=lf.img_th_flag)
            case 'Turkish':
                self.lb_title.configure(image='',text='Metninizi aşağıya yazın')
                self.lb_flag.configure(image=lf.img_tr_flag)
            case 'Vietnamese':
                self.lb_title.configure(image='',text='Nhập văn bản của bạn dưới đây')
                self.lb_flag.configure(image=lf.img_vt_flag)

if __name__ == '__main__':
    App().mainloop()


