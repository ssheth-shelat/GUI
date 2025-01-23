# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.geometry("400x500")
root.configure(bg = "#cbd7f7")

def OnClick_Submit():
    money = money_textbox.get()
    messagebox.showinfo("Captured data", money)
'''Sector, Industry, Goal (income or growth), Age range/point in career, Risk tolerance, How long to keep the stock, 
How much money the client is willing to invest to produce an optimal stock listed on Yahoo finance'''

root.title("Client Inquiries")
money_label = tkinter.Label(root, text = "Enter the amount of money you are willing to invest")
money_label.pack(anchor = tkinter.W, padx= 10)
money_textbox = tkinter.Entry(root)
money_textbox.pack(anchor = tkinter.W, padx= 10)

submit_button = tkinter.Button(root, text = "Submit", command = OnClick_Submit)
submit_button.pack(anchor = tkinter.W, padx= 10)






root.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/