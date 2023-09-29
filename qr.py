import qrcode
import tkinter.messagebox
import tkinter as tk

def makeqr():
    try :
        data=text_input.get()
        img = qrcode.make(data)
        type(img)
        img.save("myqr.png")
        tkinter.messagebox.showinfo('Done','Qr Succesfully downloaded in this folder :D')
    except:
        tkinter.messagebox.showinfo('something worng :(')
            

myapp=tk.Tk()
myapp.title('qrcodemaker')
myapp.minsize(width=150,height=100)
title_label =tk.Label(text="Your Data", fg='red', font=20)
title_label.pack()

text_input=tk.Entry()
text_input.pack()

ok_button=tk.Button(text='Generate QRcode',command=makeqr, fg='green')
ok_button.pack()


myapp.mainloop()