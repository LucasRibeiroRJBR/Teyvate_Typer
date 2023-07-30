import customtkinter

app = customtkinter.CTk()
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

def slider_event(value):
    print(value)

slider = customtkinter.CTkSlider(app, from_=0, to=100, command=slider_event)
slider.pack()

app.mainloop()