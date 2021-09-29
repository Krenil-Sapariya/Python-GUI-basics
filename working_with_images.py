import tkinter
from PIL import ImageTk, Image

#define window
root = tkinter.Tk()
root.title('Image basics')
root.geometry('700x700')

# PNG image
my_img = tkinter.PhotoImage(file='a.png')

my_label = tkinter.Label(root, image=my_img)
my_label.pack()

my_btn = tkinter.Button(root, image=my_img)
my_btn.pack()

# JPEG image
img = ImageTk.PhotoImage(Image.open('b.jpg'))
label = tkinter.Label(root, image = img)
label.pack()

#run root in main looop
root.mainloop()