"""
Import Transaction Class seperti import module library

Example
------------------
import library_name as lib_alias
from library_name import library_class


How to import from file as module
-------------------------------------
from module_py_file import class_name
*Notes: This module_py_file will not include format file name

How to import
------------------
from Transaction import Transaction

"""
from Transaction import Transaction


### Call the Transaction class with variable
cart = Transaction()


### Add data
cart.add_item("Baju", 2, 10000)
cart.add_item("Celana", 2, 20000)
cart.add_item("Kaos Kaki", 2, 30000)
cart.add_item("Sepatu", 2, 30000)
cart.add_item("Topi", 2, 20000)

### Update item name data in cart
# cart.update_item_name("nama item", "nama baru item")
cart.update_item_name("Baju", "Baju Dino")

### Update quantity data with item_name in cart
cart.update_item_qty("Topi", 8)


### Update price data with item_name in cart
### You can use cart.update_item_price("nama item", 120000)

### Delete item with specific name
### You can use cart.delete_item("nama item")
cart.delete_item("Celana")


### Function for check order with table output
cart.check_order()
### Function for call total price
cart.total_price()