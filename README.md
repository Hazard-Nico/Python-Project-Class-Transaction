# Python-Project-Class-Transaction
--------------------------------------------------------------------------------------------------------------------
# Membuat Class Transaksi

Fungsi yang akan dipasang ke dalam Class:
1. add_item => menambah satu item ke dalam keranjang
2. update_item => edit salah satu item di keranjang
3. delete_item => menghapus salah satu item keranjang
4. reset_transaction => menghapus seluruh isi keranjang
5. check_order => mengecek dan print output isi keranjang

Disini ada beberapa langkah yang akan dimasukkan menjadi Function di dalam Class:
1. Membuat Class Transaction

2. Membuat Function __init__
    def __init__(self):
        self.items = []

3. Membuat function add_item(self, nama_item, jumlah_item, harga_per_item)
    - nama_item         : str => nama barang
    - jumlah_item       : int => jumlah per barang yang akan dimasukkan
    - harga_per_item    : int => harga barang
    - Perlu menambahkan variabel Jumlah Harga per jumlah item:
        jumlah_harga = jumlah_item * harga_per_item

4. Membuat function update_item(self, nama_item, ...), ada 3 fungsi update yang akan dimasukkan
    - update_item_nama(self, nama_item, new_nama) => merubah nama barang
        - nama_item : str => nama barang yang dipilih
        - new_nama  : str => nama baru dari barang yang di pilih
    - update_item_qty(self, nama_item, jumlah_item) => merubah jumlah barang
        - nama_item     : str => nama barang yang dipilih
        - jumlah_item   : int => merubah jumlah barang
    - update_item_price(self, nama_item, harga_per_item) => mengganti harga barang
        - nama_item     : str => nama barang yang dipilih
        - harga_per_item   : int => merubah harga per barang

5. Membuat function delete_item(self, nama_item), memakai fungsi .remove()

6. Membuat function reset_transaction(self), memakai fungsi .clear()

7. Membuat function check_order()
    - Disini ada menambahkan library baru untuk tampilan list menjadi bentuk tabel
    - tabulate(list, headers, tablefmt)
        - list      : [] 
        - header    : [] => header untuk menampilkan header row table
        - tablefmt  : "grid" => Bisa menggunakan grid atau bentuk tabel lainnya
    - Cek dokumentasi tabulate: 
        - https://github.com/astanin/python-tabulate

8. Membuat function total_harga()
    - Function untuk menghitung total harga dari seluruh harga per item di dalam keranjang
    - total_harga += total seluruh jumlah harga => Melakukan iterasi menambahkan seluruh jumlah harga
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##### Cara Install Tabulate
- pip install tabulate

##### Cara Import Tabulate
- from tabulate import tabulate
