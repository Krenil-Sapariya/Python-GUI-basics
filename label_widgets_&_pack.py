import tkinter
from tkinter import BOTH
#define window
root = tkinter.Tk()
root.title('label basics!')
root.geometry('800x800')
#root.resizable(0,0)
root.config(bg='blue')

#create widgets

label1 = tkinter.Label(root, text='hey this is label 1')
label1.pack()

label2 = tkinter.Label(root, text='this is label 2', font=('Arial', 18, 'bold'))
label2.pack()

label3 = tkinter.Label(root, text='this is label 3', font=('Calibri', 18, 'bold'))
# padx - set horizontal padding & pady - set vertical padding
label3.pack(padx=10 , pady=10)

label4 = tkinter.Label(root, text='this is label 4', bg='red' , fg='white')
label4.pack(pady=(0,10) , ipadx=5 , ipady=5 , anchor='w')

# pady=(0,10) => 0 padding on top & 10 padding on bottom
# ipadx - internal padding in x direction & ipady - internal padding in y direction
# anchor='w' - pin widget in a perticular direction of the screen i.e. here w means west (try 'e','n','s')

label5 = tkinter.Label(root, text='this is label 5', bg='black' , fg='yellow')
# fill='x' means it will be filled in x direction
label5.pack(ipadx=8 , ipady=8 , fill='x')

label6 = tkinter.Label(root, text='this is label 6', bg='black' , fg='yellow')
# # fill='y' means it will be filled in y direction upto space required by characters
# # to fill full space type expand='True'
label6.pack(ipadx=8 , ipady=8 , fill='y' , expand='True')

label7 = tkinter.Label(root, text='this is label 7', bg='yellow' , fg='blue')

label7.pack(ipadx=8 , ipady=8 , fill=BOTH , expand='True')



#main loop
root.mainloop()
