from tabulate import tabulate

class Transaction:

    def __init__(self):
        self.items = []

    """
    ### Add item untuk menambahkan item ke keranjang

    ### Parameter
    ----------------------
    nama_item       : str
    jumlah_item     : int
    harga_per_item  : int

    ### Function
    ---------------------
    .append()
    """
    def add_item(self, nama_item, jumlah_item, harga_per_item):
        jumlah_harga = jumlah_item * harga_per_item
        item = [nama_item, jumlah_item, harga_per_item, jumlah_harga]
        self.items.append(item)
    """
    ### End of add function
    """
    ### End of add_item()



    """
    ### Membuat fungsi Update untuk merubah salah satu nama item di dalam keranjang

    ### Parameter
    ----------------------
    nama_item       : str
    new_nama        : str

    ### Function
    ---------------------
    .pop()
    """
    def update_item_name(self, nama_item, new_nama):
        for item in self.items:
            if item[0] == nama_item:
                item.pop(0)
                item.insert(0, new_nama)
    
    def update_item_qty(self, nama_item, jumlah_item):
        for item in self.items:
            if item[0] == nama_item:
                item.pop(3)
                item.pop(1)
                item.insert(1, jumlah_item)
                jumlah_harga = jumlah_item * item[2]
                item.insert(3, jumlah_harga)
        
    def update_item_price(self, nama_item, harga_per_item):
        for item in self.items:
            if item[0] == nama_item:
                item.pop(3)
                item.pop(2)
                item.insert(2, harga_per_item)
                jumlah_harga = harga_per_item * item[1]
                item.insert(3, jumlah_harga)
    """
    ### End of all update function
    """
    ### End of all update function



    """
    ### Fungsi delete untuk menghapus item yang kita pilih

    ### Parameter
    -----------------
    nama_item   : str

    ### Function
    -----------------
    .remove()
    """
    def delete_item(self, nama_item):
        for item in self.items:
            if item[0] == nama_item:
                self.items.remove(item)
    ### End of delete_item()



    """
    ### Reset function untuk mengosongkan seluruh item dari keranjang

    ### Function
    ------------
    .clear()
    """
    def reset_transaction(self):
        self.items.clear()
    ### End of reset_transaction()

    """
    ### Check Order untuk menampilkan item yang sudah masuk ke keranjang

    ### Memakai library tambahan dengan tabulate
    """
    def check_order(self):
        head = ["Item", "Jumlah item", "Harga/item", "Harga total"]
        print(tabulate(self.items, headers=head, tablefmt="grid"))

    def total_price(self):
        # List kosong untuk mengumpulkan seluruh jumlah harga per item
        total_bayar = []
        for item in self.items:
            jumlah_harga_per_item = item[1] * item[2]
            total_harga = 0
            total_harga += jumlah_harga_per_item
            total_bayar.append(total_harga)
        total = sum(total_bayar)

        """
        ### Membuat kondisi diskon dari total harga yang ditentukan

        if total > Rp 200.000 then discount 5%
        elif total > Rp 300.000 then discount 8%
        elif total > Rp 500.000 then discount 10%
        """

        if total > 500000:
            print(f"Total harga semua item adalah Rp {total}, maka anda mendapatkan diskon 10%")
            discount = 0.1
            total_bayar = int(total - (total * discount))
            print(f"Jadi total yang harus anda bayar adalah = Rp {total_bayar}")

        elif total > 300000:
            print(f"Total harga semua item adalah Rp {total}, maka anda mendapatkan diskon 8%")
            discount = 0.08
            total_bayar = int(total - (total * discount))
            print(f"Jadi total yang harus anda bayar adalah = Rp {total_bayar}")

        elif total > 200000:
            print(f"Total harga semua item adalah Rp {total}, maka anda mendapatkan diskon 5%")
            discount = 0.05
            total_bayar = int(total - (total * discount))
            print(f"Jadi total yang harus anda bayar adalah = Rp {total_bayar}")
            
print(type(Transaction))