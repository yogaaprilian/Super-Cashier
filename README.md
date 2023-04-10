# Python Project: Super-Cashier

## Latar Belakang _Project_

__Super Cashier__ merupakan program sederhana yang dapat digunakan para pelanggan untuk melakukan transaksi belanja di supermarket. Program ini menggunakan bahasa pemrograman `Python` yang dijalankan sesuai fungsi dasar mesin kasir sehingga para pelanggan dapat melakukan proses belanja secara mandiri atau _self-service_.


Program ini dibuat dengan mempertimbangkan beberapa hal:
1. Belanja di supermarket saat ramai akan membuat antrian di kasir semakin panjang, sehingga memaksa semua pembeli menunggu lama untuk melakukan pembayaran di kasir.
2. Supaya dapat memenuhi kebutuhan pelanggan yang berada di luar kota, supermarket perlu memiliki program dengan fitur-fitur yang dapat membantu menyelesaikan masalah mereka.
3. Untuk menjangkau lebih banyak pelanggan dan meningkatkan kepuasan mereka, dibutuhkan program yang memungkinkan pelanggan memasukkan item, jumlah, dan harga belanjaan mereka, serta fitur lainnya.

## _Feature Requirements_

Berdasarkan latar belakang diatas, kita dapat membuat suatu solusi yaitu dengan membuat program yaitu __Super Cashier__. Program Super Cashier memiliki beberapa fitur yang diinginkan, antara lain:
1. Pelanggan dapat melakukan belanja dengan memanggil `class Transaction()`.
2. Pelanggan dapat `menambahkan barang` belanjaan ke dalam program dengan memasukkan nama barang, jumlah barang, dan harga barang.
3. Pelanggan dapat melakukan `perubahan` pada barang yang dibeli seperti mengganti nama barang, jumlah barang, atau harga barang yang telah dibeli.
4. Pelanggan dapat `menghapus` salah satu barang yang telah dimasukkan ke dalam daftar belanjaan.
5. Pelanggan dapat `membatalkan transaksi` atau `menghapus semua daftar belanjaan` yang telah ditambahkan.
6. Pelanggan dapat `mengecek daftar belanjaan` yang telah ditambahkan sebelumnya.
7. Program dapat membantu pelanggan untuk `menghitung harga total` dari seluruh barang belanja yang telah ditambahkan.
8. Program dapat menentukan apakah pelanggan `mendapatkan potongan harga`, dengan ketentuan sebagai berikut:
   - Jika total harga belanja pelanggan __di atas Rp. 200.000__, maka pelanggan akan mendapatkan __potongan harga sebesar 5%__.
   - Jika total harga belanja pelanggan __di atas Rp. 300.000__, maka pelanggan akan mendapatkan __potongan harga sebesar 8%__.
   - Jika total harga belanja pelanggan __di atas Rp. 500.000__, maka pelanggan akan mendapatkan __potongan harga sebesar 10%__.

## Alur Program:

<p align="center">
    <img src="https://user-images.githubusercontent.com/128567810/230119316-54c4466e-0f42-48ab-8755-50e53f818417.png" width="500">
</p>


Berdasarkan Diagram Alir, program tersebut akan berjalan sebagai berikut:

1. Saat program dimulai, pengguna yang akan berbelanja harus membuat ID Transaksi yang berguna untuk menjalankan program selanjutnya.
2. Menu akan ditampilkan, pengguna akan memilih menu program yang akan dijalankan selanjutnya.
3. Pengguna akan menambahkan barang yang akan dibeli dengan memasukkan nama barang, jumlah barang, dan harga barang yang akan dibeli.
    - Jika ingin menambahkan barang lagi, pengguna dapat memilih ‘Ya’.
4. Setelah melakukan penambahan barang yang dibeli, program akan menampilkan daftar belanjaan yang telah ditambahkan beserta total belanjanya.
5. Pengguna dapat memeriksa daftar belanja.
    - Jika tidak terdapat kesalahan input, maka pengguna dapat memilih ‘Tidak’
    - Jika ‘Ya’ dari tampilan daftar belanja terdapat kesalahan, maka pengguna dapat memperbarui nama/harga/jumlah yang telah ditambahkan.
6. Selain itu, pengguna dapat menghapus barang yang telah ditambahkan dengan pilihan:
    - Menghapus satu atau beberapa barang yang telah ditambahkan.
    - Menghapus semua barang yang ada di daftar belanja, jika ingin membatalkan kegiatan belanja.
7. Setelah memeriksa, program akan menampilkan total harga. Pengguna dapat memeriksa kembali apakah ada barang yang ingin diperbarui atau tidak.
    - Jika ya, proses akan dilanjutkan ke tahap pembayaran.
8. Pengguna akan mendapatkan diskon jika total dari seluruh harga memenuhi kriteria untuk mendapatkan diskon.
    
## Penjelasan Modul

Terdapat dua modul yang digunakan dalam program __Super Cashier__ yaitu:

### Module `Super_Cashier.py`

Modul ini berisi program yang akan dieksekusi saat pelanggan berbelanja menggunakan program __Super Cashier__. Modul ini mengunakan _library_/_module_ dari bahasa pemograman python yaitu:

1. `os` digunakan untuk membantu membersihkan terminal atau konsol ketika program dijalankan
2. `tabulate` digunakan untuk membuat tabel ketika menampilkan daftar belanja atau melakukan pembayaran.
3. `Ipython` digunakan untuk membantu membersihkan output pada Jupyter Notebook

Modul ini memiliki kelas `Transaction()` yang berisi beberapa metode, yaitu:

#### 1. Method `__init__()`
Merupakan _method_ yang digunakan untuk menginisialisasi suatu objek ketika objek tersebut dibuat di _method_ lain. 

_Method_ ini berisi:
- `self.daftar_belanja` untuk menyimpan daftar belanja pelanggan. 
- `self.total_harga_belanja` yang digunakan sebagai penghitung untuk menjumlahkan total harga seluruh belanjaan.
- `id_transaksi` atribut objek yang digunakan untuk memanggil kelas transaksi.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L13-L79

#### 2. Method `add_item()`
Merupakan _method_ yang digunakan untuk menambahkan barang ke dalam daftar belanja dengan memasukkan `nama_barang`, `jumlah_barang`, dan `harga_barang`.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L80-L178

#### 3. Method `list_item()`
Merupakan _method_ yang digunakan untuk menampilkan daftar belanja dalam bentuk tabel setelah pelanggan selesai melakukan transaksi. Untuk membuat tabel, digunakan module `tabulate` pada Python.

_Method_ ini akan dipanggil oleh _method_ lain didalam `Class Transaction()`

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L179-L199

#### 4. Method `clear_screen()`

merupakan _method_ yang digunakan untuk membersihkan output pada terminal ketika program dijalankan.

_Method_ ini menggunakan _library_ `os` untuk mengakses _system command_ yang dapat membersihkan tampilan output pada terminal dengan menggunakan perintah yang berbeda-beda tergantung pada sistem operasi yang digunakan oleh pengguna.

_Method_ ini juga dirancang agar dapat digunakan di Jupyter Notebook atau lingkungan lainnya dengan cara yang sama.

_Method_ ini juga dipanggil oleh _method_ lain baik itu didalam modul `super_cashier.py` atau `menu.py`

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L200-L220

#### 5. Method `update_item_name()`
Merupakan _method_ yang digunakan untuk mengubah nama barang jika terjadi kesalahan input nama atau pelanggan ingin mengganti nama barang.

Pada _method_ ini, pelanggan diminta untuk memasukkan    `nama_barang` yang lama dan `nama_barang_baru` yang akan menjadi nama baru dari barang tersebut.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L221-L299

#### 6. Method `update_item_qty()`
Merupakan _method_ yang digunakan untuk mengubah jumlah barang jika terjadi kesalahan input jumlah barang dan pelanggan ingin mengubah jumlah barang tersebut.

Pada _method_ ini, pelanggan diminta untuk memasukkan `nama_barang` yang ingin diubah dan `jumlah_barang_baru` yang merupakan nilai baru dari jumlah barang yang ingin ingin diubah.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L300-L389

#### 7. Method `update_item_price()`
Merupakan _method_ yang digunakan untuk mengubah harga per barang jika terjadi kesalahan input harga barang dan pelanggan ingin mengubah harga barang tersebut.

Pada method ini pelanggan diminta untuk memasukkan `nama_barang` yang ingin diubah dan `harga_barang_baru` sebagai parameter untuk mengubah harga per barang pada daftar belanja.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L390-L479

#### 8. Method `delete_item()`
Merupakan _method_ yang dapat digunakan oleh pelanggan untuk menghapus salah satu barang dari daftar belanja.

Pada _method_ ini pelanggan akan diminta untuk memasukkan `nama_barang` yang akan dihapus. Setelah itu, method ini akan mencari barang yang diinputkan dan menghapusnya dari daftar belanja.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L480-L543

#### 9. Method `reset_transaction()`
_Method_ ini digunakan untuk menghapus seluruh transaksi yang telah dilakukan.

_Method_ ini juga dapat digunakan jika pelanggan ingin membatalkan transaksi.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L544-L586

#### 10. Method `check_order()`
_Method_ yang digunakan untuk melakukan pemeriksaan pada daftar belanja.

Dikarenakan program __Super Cashier__ masih menggunakan sistem _self service_ yang dimana pelanggan dapat melakukan kesalahan input. _Method_ ini akan membantu pelanggan untuk memeriksa apakah semua yang telah dimasukan dalam daftar belanja sudah benar atau belum.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L587-L624

#### 11. Method `total_price()`
Method `total_price()` melakukan perulangan pada seluruh barang pada daftar belanja dan mengalikan jumlah barang dengan harga per barang. Kemudian, hasil perkalian tersebut ditambahkan ke dalam variabel `total_harga_belanja` yang merupakan _counter_ untuk menjumlahkan seluruh total harga belanjaan.

Jika pelanggan memenuhi kriteria mendapatkan potongan harga, maka method ini akan mengurangi harga total belanjaan sesuai dengan potongan harga yang diberikan. Akhirnya, _method_ ini akan mengembalikan harga total belanjaan setelah dipotong (jika ada).

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L625-L705

### Module `menu.py`

Modul ini berisi fungsi-fungsi yang membentuk __Menu Program__ yang membantu pelanggan untuk menjalankan __Super Cashier__ agar lebih mudah untuk dijalankan.

Modul ini menggunakan beberapa _library_ seperti `os` dan `IPython` yang tersedia pada Python. Kedua _library_ ini digunakan untuk membersihkan output sebelum atau setelah pelanggan melakukan kegiatan berbelanja. Pembersihan tersebut bisa digunakan di terminal atau di Jupyter Notebook.

Selain itu, modul `menu.py` meng-_import_ modul `super_cashier.py` untuk dapat menjalankan programnya.

Di dalam `module.py` terdapat beberapa fungsi, yaitu:

#### 1. Input `ID Transaksi`

Bagian pemrograman ini digunakan untuk membuat instance dari `class Transaction()` untuk bisa dijalankan pada modul ini. 

Sebelum meminta pengguna untuk memasukkan `ID Transaksi`, output pada terminal atau Jupyter notebook dibersihkan terlebih dahulu menggunakan fungsi `clear_output()` berasal dari library `IPython.display`, dan fungsi `os.system()` berasal dari library `os`. Kedua fungsi ini dapat digunakan pada terminal atau di Jupyter Notebook untuk membersihkan tampilan output sebelumnya.

Pelanggan akan diminta untuk memasukkan `ID Transaksi` yang berupa __angka (int)__. Angka tersebut nantinya akan dimasukkan ke dalam instance variabel dan menjadi atribut objek untuk memanggil `class Transaction()`.

```python
cashier = super_cashier.Transaction(transaksi_ID)
```

Berikut merupakan program yang digunakan dalam bagian ini:

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/menu.py#L11-L47

#### 2. Pemanggil Method pada `class Transaction()`

Bagian pemrograman ini berisi fungsi-fungsi yang akan dipanggil pada bagian fungsi `main_menu()`, `second_menu()`, dan `modify_menu()`. 

Fungsi-fungsi tersebut akan digunakan ketika dipilih oleh pelanggan. Seluruhnya terdapat sembilan fungsi yang akan memanggil _method_ yang ada pada `class Transaction()`.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/menu.py#L48-L183

#### 3. Menu Edit Belanja `modify_menu()`

Fungsi ini berisi beberapa pilihan menu yang digunakan untuk melakukan perubahan pada barang yang dibeli.

Jika ada perubahan yang perlu dilakukan, pelanggan dapat menggunakan menu ini.

Fungsi ini memiliki enam menu, di mana setiap nomor menu dapat memanggil _method_ tertentu.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/menu.py#L184-L229

#### 4. Menu Belanja `second_menu()`

Berbeda dengan fungsi `modify_menu()`, fungsi ini digunakan oleh pelanggan untuk melakukan transaksi belanja.

Menu ini terdiri dari lima pilihan menu, di mana setiap pilihan akan memanggil fungsi lain yang ada pada modul `main.py`.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/menu.py#L230-L272

#### 5. Menu Utama `main_menu()`

Menu ini merupakan menu utama yang muncul setelah pelanggan memasukkan `ID transaksi`.

Menu ini hanya berisi dua pilihan menu, yaitu:
- `1. Belanja` yang akan langsung memanggil fungsi `second_menu()` untuk melakukan belanja 
- `2. Keluar` yang akan memanggil fungsi `keluar()` ketika pelanggan ingin keluar dari program __Super Cashier__.

Selain itu, fungsi ini dipanggil di akhir dan di luar fungsi ini, untuk memulai program setelah `ID Transaksi` dibuat.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/menu.py#L273-L308

## Hasil Test Case

Ada beberapa test yang dilakukan untuk menguji apakah program __Super Cashier__ ini dapat dijalankan atau tidak.

Test Case ini dilakukan di `Jupyter Notebook` dengan beberapa kasus yang meliputi:

### Test Case 1

Pelanggan ingin menambahkan dua barang baru menggunakan _method_ `add_item()`. Barang yang ditambahkan sebagai berikut:
- Nama Barang: Ayam Goreng, Jumlah: 2, Harga: 20_0000
- Nama Barang: Pasta Gigi, Jumlah: 3, Harga: 15_000

Dari program `Super Cashier` dihasilkan output:

```python
trnsct_123 = Transaction(1234567)

trnsct_123.add_item()
```

![Test Case 1](https://user-images.githubusercontent.com/128567810/230122201-baa8e650-4dd3-482e-b30b-1f77ca92349c.png)

### Test Case 2

Ada keadaan dimana pelanggan salah membeli salah satu barang dari belanjaan yang telah ditambahkan, maka pelanggan menggunakan _method_ `delete_item()` untuk menghapus item. Item yang ingin dihapuskan adalah __Pasta Gigi__

Dari program `Super Cashier` dihasilkan output:

```python
trnsct_123.delete_item()
```

![Test Case 2](https://user-images.githubusercontent.com/128567810/230122259-d3e5a055-0ed6-4b8c-8f5b-b2d194ecd389.png)

### Test Case 3

Ternyata setelah dipikir - pikir pelanggan salah memasukkan item yang ingin dibelanjakan! Daripada menghapus satu - satu, maka pelanggan cukup menggunakan method `reset_transaction()` untuk menghapus semua item yang sudah ditambahkan.

Dari program `Super Cashier` dihasilkan output:

```python
trnsct_123.delete_item()
```

![Test Case 3](https://user-images.githubusercontent.com/128567810/230119211-3f7efbd8-8d86-4e81-9f09-02bda4f60950.png)

### Test Case 4

Setelah pelanggan selesai berbelanja, pelanggan akan menghitung total belanja yang harus digunakan menggunakan _method_ `total_price()`. Sebelum mengeluarkan output total belanja akan menampilkan barang-barang yang dibeli.

Dari program `Super Cashier` dihasilkan output:

```python
trnsct_321.total_price()
```

![Test Case 4](https://user-images.githubusercontent.com/128567810/230119248-739eb53c-3f6d-475e-b5b8-71a90cc93eb3.png)

## Kesimpulan

Program __Super Cashier__ dapat membantu pelanggan melakukan aktivitas berbelanja tanpa harus datang ke supermarket, sehingga dapat mengurangi antrian pembayaran yang ada di tempat berbelanja. Fitur-fitur utama dari program ini adalah:

1. Pelanggan dapat memasukkan nama, jumlah, dan harga barang ke dalam daftar belanja.
2. Pelanggan dapat mengubah daftar belanja, menghapus atau membatalkan transaksi jika terjadi kesalahan penginputan barang.
3. Setelah melakukan pembelian, pelanggan dapat memeriksa daftar belanja untuk memastikan kebenaran barang yang dibeli.
4. Setelah pembelian selesai, pelanggan dapat melakukan pembayaran secara otomatis dan sistem akan menghitung potongan harga yang didapatkan.

Program __Super Cashier__ memiliki tampilan yang mudah digunakan oleh pelanggan dan dapat disesuaikan dengan kebutuhan bisnis. Dengan demikian, program ini merupakan contoh aplikasi kasir sederhana yang dapat dikembangkan.

## _Future Works_

Beberapa kemungkinan pengembangan program Super Cashier di masa depan meliputi:

1. __Peningkatan antarmuka pelanggan__: Menambahkan fitur seperti antarmuka yang lebih ramah pelanggan atau lebih interaktif dapat meningkatkan pengalaman pelanggan dan memudahkan penggunaan aplikasi.

2. __Pembayaran yang lebih fleksibel__: Selain pembayaran tunai, program dapat dikembangkan dengan menambahkan opsi pembayaran kartu kredit dan e-wallet agar lebih fleksibel dan memudahkan pelanggan dalam melakukan pembayaran.

3. __Pengelolaan stok barang__: Dapat ditambahkan fitur pengelolaan stok barang untuk memantau jumlah barang yang tersedia di gudang dan memperingatkan jika stok barang hampir habis agar pemilik toko dapat mengambil tindakan yang diperlukan.

4. __Laporan penjualan__: Program dapat dilengkapi dengan fitur laporan penjualan untuk membantu pemilik toko memantau penjualan dan menganalisis data penjualan secara lebih mudah dan efisien, sehingga dapat membantu dalam pengambilan keputusan bisnis yang lebih baik.

Selain pengembangan program yang telah disebutkan sebelumnya, program yang telah dibuat ini membutuhkan saran perbaikan agar dapat menjadi lebih baik. Apabila anda berkenan, saya mengharapkan masukan dari Anda untuk meningkatkan kualitas program ini. Terima kasih

### Informasi Penggunaan

Untuk menggunakan program ini, Anda dapat membuka file `menu.py` dan menjalankan program melalui terminal atau konsol.

Jika ingin menjalankan program pada __Jupyter Notebook__, Anda bisa mengunduh file `menu.py`, `super_cashier.py`, dan `Super_Cashier.ipynb`, kemudian menempatkannya dalam satu folder. Setelah itu, Anda dapat menjalankan file `Super_Cashier.ipynb` melalui __Jupyter Notebook__.
