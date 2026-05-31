from Screens import *
from tkinter import *

root = Tk()

root.title('OnlySocks')

root.geometry('550x500')
root["bg"]="#E6E6E6"

root.resizable(False, False)
#registerScreen(root)
adminDashboardScreen(root)
root.mainloop()
