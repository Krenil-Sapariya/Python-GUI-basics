import tkinter
from tkinter import END
# define window
root = tkinter.Tk()
root.title('entry basics')
root.geometry('500x500')
root.resizable(0,0)

# define functions
def print_data():
    # print('hello!!')  - print hello in terminal
    text = tkinter.Label(output_frame, text=text_entry.get())
    text.pack()

    # after entry completion when click on btn clear the input box starting from index-0 till the end
    text_entry.delete(0,END)

def capital(string):
    text = tkinter.Label(output_frame, text=string.upper())
    text.pack()
    text_entry.delete(0,END)


#define frames
input_frame = tkinter.Frame(root , bg='blue' , width=500 , height=100)
output_frame = tkinter.Frame(root , bg='yellow' , width=500 , height=400)
input_frame.pack(padx=8 , pady=8)
output_frame.pack(padx=8 , pady=(0,8))

# define entry
text_entry = tkinter.Entry(input_frame , width=40)
text_entry.grid(row=0 , column=0 , padx=5 , pady=5)
# to prevent the frame to get resize according to the widget size use propagate
input_frame.grid_propagate(0)

print_btn = tkinter.Button(input_frame , text='Print' , command=print_data)
print_btn.grid(row = 0 , column=1 , padx=5 , pady=5 , ipadx=4 , ipady=2)

# propagete output_frame
output_frame.pack_propagate(0)



# new parameter function using lambda function
caps_btn = tkinter.Button(input_frame , text='Capital' , command=lambda:capital(text_entry.get()))
caps_btn.grid(row=1 , column=0 , columnspan=2 , padx=5, pady=5 , sticky='WE')

#main loop
root.mainloop()