from Transaction import Transaction

cart = Transaction()

cart.add_item("Baju", 2, 10000)
cart.add_item("Celana", 2, 20000)
cart.add_item("Kaos Kaki", 2, 30000)
cart.add_item("Sepatu", 2, 30000)
cart.add_item("Topi", 2, 20000)

cart.check_order()
cart.total_price()
