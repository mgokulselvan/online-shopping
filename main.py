from loginScreen import loginScreen
from registerScreen import registerScreen
from homeScreen import homeScreen
from shoppingCart import shoppingCart
from paymentScreen import paymentScreen
from ordersScreen import ordersScreen
from inventoryScreen import inventoryScreen
from addProductScreen import addProductScreen
from adminOrdersScreen import adminOrdersScreen
from adminDashboardScreen import adminDashboardScreen
from tkinter import *

root = Tk()

root.title('OnlySocks')

root.geometry('550x500')
root["bg"]="#E6E6E6"

root.resizable(False, False)
#loginScreen(root)
#registerScreen(root)
#homeScreen(root)
adminDashboardScreen(root)
#shoppingCart(root)
#paymentScreen(root)
#ordersScreen(root)
#inventoryScreen(root)
#addProductScreen(root)
#adminOrdersScreen(root)
root.mainloop()
