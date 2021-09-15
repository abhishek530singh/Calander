import calendar
from tkinter import * 

def showCalender(event):
    gui=Tk()
    gui.config(background="grey")
    gui.title("Calender of the year ")
    gui.geometry("550x600")
    year=int(year_field.get())
    gui_contents= calendar.calendar(year)
    calyear=Label(gui,text=gui_contents,font="Consolas 10 bold")
    calyear.grid(row=5,column=1,padx=20)
    gui.bind("<Escape>" ,lambda y: gui.destroy())
    gui.mainloop()
    

#driver code

if __name__=="__main__":
    new=Tk()
    #yearVar=StringVar()
    new.config(background="#c6d9f7")
    new.title("Calender")
    new.geometry("550x600")
    cal=Label(new,text="Calender", bg="#d1cbcb",font=('times',28,'bold'))
    year =Label(new,text="Enter year you want to look a calender for" , bg='dark grey')

    #text box for input
    year_field=Entry(new)

    #button that on clicked or on enter we show user the calender
    button=Button(new,text='Show Calender',bg='#ff7300',fg='black',command=showCalender)
    #as 
    new.bind("<Return>",showCalender)

    #adjusting widget in position
    cal.grid(row=1,column=1)
    year.grid(row=2,column=1)
    year_field.grid(row=3,column=1)
    button.grid(row=4,column=1)
    new.bind("<Escape>",lambda x: new.destroy())
    new.mainloop()