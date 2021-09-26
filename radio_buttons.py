import tkinter
from tkinter import IntVar
from tkinter import END

#define window
root = tkinter.Tk()
root.title('Radio button basics')
root.geometry('500x500')
root.resizable(0,0)

# define functions
def print_answer(num):
    # we have set number's value=1 for radio button-1 and 2 for radio button-2
    if number.get()==1:
        text = tkinter.Label(output_frame, text=str(int(num)+10))
    else:
        text = tkinter.Label(output_frame, text=str(int(num)*10))

    text.pack()
    

# define frames
input_frame = tkinter.LabelFrame(root, text='this is input frame', width=500 , height=100)
output_frame = tkinter.Frame(root, width=500 , height=450 , bg='green')
input_frame.pack(padx=10 , pady=10)
output_frame.pack(padx=10 , pady = (0,10))


# input box
num = tkinter.Entry(input_frame, width=30)
num.grid(row=0, column=0, padx=8, pady=8)
num.grid_propagate(0)


# buttons
number = IntVar()   #common variable to link radio buttons
number.set(1)       #default value of the button is set to 1 means btn having value 1 will be default selected

radio1 = tkinter.Radiobutton(input_frame , text='+10' , variable=number , value=1)
radio2 = tkinter.Radiobutton(input_frame , text='*10' , variable=number , value=2)
print_btn = tkinter.Button(input_frame , text='Print', bg='black', fg='yellow' , command=lambda:print_answer(num.get()))

output_frame.pack_propagate(0)

radio1.grid(row=1 , column=0 , padx=8, pady=8)
radio2.grid(row=1 , column=1 , padx=8, pady=8)
print_btn.grid(row=2 , column=0 ,columnspan=2, sticky='WE', padx=8, pady=8)

# main loop
root.mainloop()