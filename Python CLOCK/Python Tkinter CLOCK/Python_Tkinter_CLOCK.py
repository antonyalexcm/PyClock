
# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to 
# retrieve system's time
from time import strftime

# creating Tkinter window
root = Tk()
root.title('Python Clock')

# this function is used to 
# display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

#Styling the label widget so that the 
#clock will look more attractive
lbl = Label(root, font= ('calibri', 40, 'bold'),
            background= 'purple',
            foreground= 'white')

#Placing the clock at the 
#centre of the Tkinter Window
lbl.pack(anchor = 'center')
time()

mainloop()