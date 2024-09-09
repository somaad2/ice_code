from tkinter import *
from tkinter import messagebox
import base64
import os


def decrypt():
    password = code.get()

    if password == "kasper":
        screen_dec = Toplevel(screen)
        screen_dec.geometry("400x200")
        screen_dec.title("Encryption")
        screen_dec.configure(bg = "#00BD56")

        message = text_place.get(1.0, END)
        encrypt_message = message.encode("ascii")
        message_bytes = base64.b64decode(encrypt_message)
        decrypt = message_bytes.decode("ascii")

        Label(screen_dec , text= "DECRYPTION :" , font ="Arial"  , fg = "#FFF" , bg = "#00BD56").place(x = 10 , y = 0)
        text2 = Text(screen_dec ,font ="Roboto 12" , bg = "#FFF" , highlightthickness=0 , bd = 0 , relief= GROOVE , wrap = WORD)
        text2.place(x = 10, y = 50 , width= 380, height= 150)
        text2.insert(END, decrypt)

    elif password =="":
        messagebox.showerror("Error" , "Input Password")

    elif password != "Kasper":
        messagebox.showerror("Error" , "Invalid Password")


def encrypt():
    password = code.get()

    if password =="kasper":
        screen_enc = Toplevel(screen)
        screen_enc.geometry("400x200")
        screen_enc.title("Encryption")
        screen_enc.configure(bg = "#ED3833")

        message = text_place.get(1.0, END)
        encrypt_message = message.encode("ascii")
        message_bytes = base64.b64encode(encrypt_message)
        encrypt = message_bytes.decode("ascii")

        Label(screen_enc , text= "ENCRYPTION :" , font ="Arial"  , fg = "#FFF" , bg = "#ED3833").place(x = 10 , y = 0)
        text2 = Text(screen_enc ,font ="Roboto 12" , bg = "#FFF" , highlightthickness=0 , bd = 0 , relief= GROOVE , wrap = WORD)
        text2.place(x = 10, y = 50 , width=380, height=150)
        text2.insert(END, encrypt)

    elif password =="":
        messagebox.showerror("Error" , "Input Password")

    elif password != "Kasper":
        messagebox.showerror("Error" , "Invalid Password")

        
def main_screen():
   global screen , code , text_place
   screen = Tk()
   screen.title("تطبيق تشفير الرسائل")
   screen.geometry("375x375")

   def reset():
       code.set("")
       text_place.delete(1.0 , END)

   Label(screen , text ="أدخل النص الخاص بك للتشفير " , fg ="#000" ,
        font=("calbri" , 11)).place(x = 10 , y = 10)
   text_place = Text(screen , bg = "#FFF" , highlightthickness = 0 , bd = 0 , relief = GROOVE , font = "Roboto 15")
   text_place.place(x = 10 , y = 40 , width = 355 , height = 100)

   Label(screen , text ="أدخل كلمة المرور لفك التشفير " ,
          fg ="#000" , font=("calbri" , 11)).place(x = 10 , y = 170)
   
   code = StringVar()
   Entry(screen, textvariable = code ,width= 32, fg="#000" , bg = "#FFF",
         highlightthickness = 0 , bd = 0 , relief = GROOVE , font=("arial" , 15) , show = "*").place(x = 10 , y = 200)
   
   Button(screen , text = "تشفير" , width = 15 , height =2 , fg = "#FFF", bg = "#ED3833" , command =encrypt , highlightthickness = 0 , bd = 0 , relief = GROOVE , cursor="hand2").place(x = 10 , y = 240)
   Button(screen , text = "فك التشفير" , width = 15 ,height =2 , fg = "#FFF", bg = "#00BD56" , command=decrypt, highlightthickness = 0 , bd = 0 , relief = GROOVE , cursor="hand2").place(x = 235 , y = 240)
   Button(screen , text = "إعادة ضبط" , width = 47 , height =2 , font = ("arial" , 9), fg = "#FFF",
           bg = "#2196F3", highlightthickness = 0 , bd = 0 , relief = GROOVE , cursor="hand2" , command= reset).place(x = 10 , y = 300)
   screen.mainloop()



main_screen()