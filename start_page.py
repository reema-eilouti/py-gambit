from tkinter import *
import gui


root = Tk()
root.geometry('350x200')

f1 = Frame(root)
f2 = Frame(root)

Label(f1, text='FRAME 1').pack()

def open_main():
    clicked_2()

f1.grid(row=0, column=0, sticky='news')
def clicked():
    f2.tkraise()
    btn_2 = Button(root, text="bt-2", command=clicked_2)
    btn_2.grid(column=1, row=0)





Label(f2, text='FRAME 2').pack()
f2.grid(row=0, column=0, sticky='news')
def clicked_2():
    f1.tkraise()
    btn = Button(root, text="bt-1", command=clicked)
    btn.grid(column=1, row=0)



open_main()
root.mainloop()


# from tkinter import *  
# from PIL import ImageTk,Image  
# root = Tk()  
# canvas = Canvas(root, width = 600, height = 600)  
# canvas.pack()  
# img = ImageTk.PhotoImage(Image.open("img1.jpg"))  
# canvas.create_image(0, 0, anchor=NW, image=img) 
# root.mainloop() 


