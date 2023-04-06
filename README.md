# Python Project: Super-Cashier

## Latar Belakang _Project_:

__Super Cashier__ merupakan suatu program sederhana yang dapat digunakan para pelanggan untuk melakukan transaksi belanja pada suatu supermarket. Program ini menggunakan bahasa pemrograman `Python` yang dijalankan sesuai fungsi dasar mesin kasir sehingga para pelanggan dapat melakukan proses belanja secara mandiri atau _self-service_.


Program ini dibuat dengan mempertimbangkan beberapa hal:
1. Jika melakukan belanja di supermarket secara langsung dengan keadaan supermarket yang ramai pelanggan akan menyebabkan antrian semakin panjang dan membuat seluruh pembeli akan menunggu dengan sangat lama untuk melakukan pembayaran di kasir.
2. Ada beberapa pelanggan yang tidak berada di kota tempat supermarket itu berada, sehingga perlu adanya program dengan fitur fitur yang membantu menyelesaikan masalah tersebut.
3. Sehingga perlu dibuatnya suatu program yang dimana pelanggan dapat bisa langsung memasukkan item yang dibeli, jumlah item yang dieli, dan harga item yang dibeli serta fitur yang lain dengan harapan dapat menjangkau lebih banyak costumer serta meningkatkan kepuasan pelanggan dalam berbelanja di supermarket tersebut.

## _Feature Requirements_:

Berdasarkan latar belakang diatas, kita dapat membuat suatu solusi yaitu dengan membuat program yaitu __Super Cashier__. Dimana dalam program kasir mempunyai beberapa fitur permintaan yang di inginkan seperti:
- Pelanggan dapat melakukan belanja dengan memanggil `Class Transaction()`.
- Pelanggan dapat `menambahkan barang` belanjaan ke dalam memasukkan nama barang, jumlah barang, dan harga barang.
- Pelanggan dapat melakukan `perubahan` pada barang yang dibeli meliputi nama barang, jumlah barang, atau harga barang yang telah di beli.
- Pelanggan dapat `menghapus` salah satu barang yang telah dimasukkan kedalaman belanjaan.
- Pelanggan dapat  `membatalkan transaksi` / `menghapus semua daftar belanja` yang telah ditambahkan.
- Pelanggan yang berbelanja dapat melakukan `pengecekkan barang` dengan menampilkan daftar belanja yang telah ditambahkan sebelumnya.
- Program dapat membantu pelanggan untuk menghitung `harga total` dari seluruh barang belanja yang telah ditambahkan.
- Program dapat menentukan apakah pelanggan `mendapatkan diskon`. Dengan ketentuan sebagai berikut:
    - Jika total harga belanja pelanggan __diatas Rp. 200.000__ maka pelanggan akan mendapatkan diskon __5%__.
    - Jika total harga belanja pelanggan __diatas Rp. 300.000__ maka pelanggan akan mendapatkan diskon __8%__.
    - Jika total harga belanja pelanggan __diatas Rp. 500.000__ maka pelanggan akan mendapatkan diskon __10%__.

## Alur Program

<p align="center">
    <img src="https://user-images.githubusercontent.com/128567810/230119316-54c4466e-0f42-48ab-8755-50e53f818417.png" width="500">
</p>


Berdasarkan Diagram Alir, program tersebut akan berjalan seperti berikut:
1. Ketika program di mulai, pelanggan yang akan melakukan kegiatan berbelanja harus membuat ID Transaksi yang berguna untuk menjelankan program selanjutnya. 
2. Menu akan ditampilkan, pelanggan akan memilih menu program apa yang akan dijalankan selanjutnya. 
3. Pelanggan akan menambahkan barang yang akan dibeli dengan memasukkan nama barang, jumlah barang, dan harga barang yang akan dibeli.
    - Jika ingin menambahkan barang lagi, pelanggan dapat memiliih ‘Ya’.
4. Setelah melakukan penambahan barang yang dibeli, program akan menampilkan daftar belanjaan yang telah ditambahkan berserta total belanjaanya.
5. Pelanggan dapat melakukan pengecekkan daftar belanja.
    - Jika tidak terdapat kesalahan input, maka pelanggan dapat memilih ‘Tidak’
    - Jika ‘Ya’ dari tampilan daftar belanja terdapat kesalahan, maka pelanggan dapat memperbaharui nama/harga/jumlah/yang telah ditambahkan.
6. Selain itu, pelanggan dapat melakukan pengapusan barang yang telah di tambahkan dengan pilihan:
    - Menghapus salah satu barang atau lebih barang yang telah ditambahkan.
    - Melakukan pengapusan semua barang ada di daftar belanja, jika ingin membatalkan kegiatan belanja.
7. Setelah melakukan pengecekkan, program akan melakukan penampilan harga total. Pelanggaan dapat mengecek kembali apakah masih ada barang yang ingin di perbaharui atau tidak.
8. Jika maka proses akan dilanjutkan ke tahap pembayaran
    - Pelanggan akan mendapatkan harga diskon apalagi total dari seluruh harga memenuhi kriteria mendapatkan diskon.
    
## Penjelasan Modul

Terdapat dua modul yang digunakan dalam program __Super Cashier__ yaitu:

### Module `Super_Cashier.py`

Dalam modul ini berisi program yang akan dijalankan ketika pengguna melakukan belanja menggunakan program __Super Cashier__. Dalam _module_ ini mengunakan _library_/_module_ dari bahasa pemograman python yaitu:

1. `os` yang digunakan untuk membantu _clear_ terminal ketika program dijalankan
2. `tabulate` yang digunakan untuk membuat table ketika menampilkan daftar belanja atau melakukan pembayaran.
3. `Ipython` yang digunakan untuk membntu membersihkan output pada jupyter notebook

Dalam modul ini terdapat `Class Transaction` yang didalamnya terdapat beberapa method meliputi:

#### 1. Method `__init__()`
Merupakan _method_ yang digunakan untuk menginisialisasi suatu objek jika objek tersebut dibuat di _method_ lain. 

Dalam _method_ ini memuat 
- `self.daftar_belanja` untuk menyimpan daftar belanja penguna 
- `self.total_harga_belanja` yang digunakan sebagai _counter_ untuk menjumlahkan total harga seluruh belanjaan.
- `id_transaksi` atribut objek yang digunakan untuk memanggil kelas transaksi

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L13-L79

#### 2. Method `add_item()`
Merupakan _method_ yang digunakan untuk menambahkan daftar belanja dengan memasuka nilai `nama_barang`, `jumlah_barang`, dan `harga_barang`

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L80-L178

#### 3. Method `list_item()`
Merupakan _method_ yang digunakan menampilkan daftar belanja ketika pengguna selesai melakukan transaksi.

_Method_ ini akan dipanggil oleh _method_ lain didalam `Class Transaction()`

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L179-L199

#### 4. Method `clear_screen()`

merupakan _method_ yang digunakan untuk membersihkan output ketika program dijalankan.

_Method_ ini menyesuaikan jika pengguna ingin membuka program dari windows ataupun dari sistem operasi lain. Selain itu, method yang digunakan untuk membersihkan output ini disesuikan untuk bisa dipakai di jupyter notebook atau di terminal maupun konsol.

_Method_ ini juga dipanggil oleh _method_ lain baik itu didalam modul `super_cashier.py` atau `menu.py`

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L200-L220

#### 5. Method `update_item_name()`
_Method_ yang digunakan untuk mengubah nama barang jika terjadi kesalahan input nama atau pelanggan ingin mengganti nama barang.

Pada _method_ ini pengguna diminta untuk memasukkan    `nama_barang` yang lama dan `nama_barang_baru`.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L221-L299

#### 6. Method `update_item_qty()`
_Method_ yang digunakan untuk mengubah jumlah barang jika terjadi kesalahan input jumlah barang dan pelanggan ingin mengubah jumlah barang tersebut

Pada _method_ ini pengguna diminta untuk memasukkan `nama_barang` yang ingin diubah dan `jumlah_barang_baru`.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L300-L389

#### 7. Method `update_item_price()`
Merupakan _method_ yang digunakan untuk mengubah harga per barang jika terjadi kesalahan input harga barang dan pelanggan ingin mengubah jumlah barang tersebut.

Pada _method_ ini pengguna diminta untuk memasukkan `nama_barang` yang ingin diubah dan `harga_barang_baru`.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L390-L479

#### 8. Method `delete_item()`
Merupakan _method_ yang dapat digunakan oleh pengguna untuk menghapus salah satu barang.

Pada _method_ ini pengguna akan diminta untuk memasukkan `nama_barang` yang akan dihapus.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L480-L543

#### 9. Method `reset_transaction()`
_Method_ ini digunakan untuk menghapus seluruh transaksi yang telah dilakukan.

_Method_ ini juga dapat digunakan jika pengguna ingin membatalkan transaksi.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L544-L586

#### 10. Method `check_order()`
_Method_ yang digunakan untuk melakukan pemeriksaan pada daftar belanja.

Dikarenakan program __Super Cashier__ masih menggunakan sistem _self service_ yang dimana pengguna dapat melakukan kesalahan input. _Method_ ini akan membantu pengguna untuk memeriksa apakah semua yang telah dimasukkan dalam daftar belanja sudah benar atau belum.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L587-L624

#### 11. Method `total_price()`
Jika pengguna telah selesai melakukan belanja, maka dapat menggunakan _method_ ini untuk menjumlahkan seluruh daftar belanja yang ada.

_Method_ ini juga digunakan untuk menghitung apabila total harga belanja pengguna memenuhi kriteria akan mendapatkan potongan harga.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/super_cashier.py#L625-L705

### Module `menu.py`

Modul ini merupakan modul yang berisi __Menu Program__ yang membantu pengguna untuk menjalankan __Super Cashier__ agar lebiih mudah untuk dijalankan.

Dalam modul ini menggunakan beberapa _library_ seperti `os` dan `Ipython` yang ada pada `python`. Kedua _library_ ini digunakan untuk memberishkan outputsesudah atau sebelum pelanggan melakukan kegiatan berbelanja. Dan pembersihan tersebut bisa digunakan di terminal atau di jupyter notebook

Selain itu, dalam module `menu.py` ini, meng-import module `super_cashier.py` untuk dapat menjalankan programnya.

Di dalam `module.py` terdapat kode program dan fungsi meliputi:

#### 1. Input `ID Transaksi`

Bagian pemograman ini digunakan untuk memanggil `class Transaction()` untuk bisa dijalankan pada module ini. 

Sebelum pengguna memasukkan `ID Transaksi` terminal atau bagian output akan dibersihan.

Pengguna akan memasukkan `ID Transaksi` yang berupa `angka (int)` yang nantinya angka tersebut akan dimasukkan kedalam _instance_ variabel dan menjadi atribut objek untuk memanggil `class Transaction()`.

```python
cashier = super_cashier.Transaction(transaksi_ID)
```

Berikut merupakan program yang digunakan dalam bagian ini:

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/menu.py#L11-L47

#### 2. Pemanggil Method `class Transaction()`

Pemograman yang berada pada bagian ini berisi fungsi-fungsi yang nantinya akan dipilih pada bagian fungsi `second_menu()` dan `modify_menu()`. 

Fungsi tersebut digunakan nantinya apabila dipilih oleh pengguna. Total ada sembilan fungsi yang nantinya digunakan untuk memanggil _method_ yang ada pada `class Transaction()`.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/menu.py#L48-L183

#### 3. Menu Edit Belanja `modify_menu()`

Fungsi ini merupakan fungsi yang berisi beberapa pilihan menu yang digunakan untuk melakukan perubahan pada barang yang dibeli.

Ketika pelanggan merasa ada yang perlu diubah, maka dapat menggunakan menu ini.

Dalam fungsi ini terdapat enam menu yang dimana setiap nomor tersebut dapat memanggil _method_ tertentu.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/menu.py#L184-L229

#### 4. Menu Belanja `second_menu()`

Berbeda dari fungsi `modify_menu()`, fungsi ini digunakan untuk pengguna melakukan transaksi belanja.

Menu ini berisi lima menu yang dimana dari setiap menunya akan memanggil fungsi yang lain yang ada pada modul `main.py`.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/menu.py#L230-L272

#### 5. Menu Utama `main_menu()`

Menu yang muncul pertama kali setelah pengguna memasukkan ID transaksi yang dimana merukan menu utama.

Menu ini hanya berisi dua pilihan menu yaitu 
- `1. Belanja` yang akan langsung masuk ke fungsi `second_menu()` untuk melakukan belanja 
- `2. Keluar` yang akan memanggil fungsi `keluar()` ketika pelanggan ingin keluar dari program __Super Cashier__.

Selain ini diakhir dan diluar fungsi ini, fungsi ini dipanggil, untuk dapat memulai program setelah `ID Transaski` dibuat.

https://github.com/yogaaprilian/Super-Cashier/blob/bf8c84e55002a384de150800158ae973cf78c7b4/menu.py#L273-L308

## Hasil Test Case

Ada beberapa test yang dilakukan untuk menguji apakah program __Super Cashier__ ini dapat dijalankan atau tidak.

Test Case ini dilakukan di `Jupyter Notebook` dengan beberapa kasus yang meliputi:

### Test Case 1

Pengguna ingin menambahkan dua barang baru menggunakan _method_ `add_item()`. Barang yang ditambahkan sebagai berikut:
- Nama Barang: Ayam Goreng, Jumlah: 2, Harga: 20_0000
- Nama Barang: Pasta Gigi, Jumlah: 3, Harga: 15_000

Dari program `Super Cashier` dihasilkan output:

```python
trnsct_123 = Transaction(1234567)

trnsct_123.add_item()
```

![Test Case 1](https://user-images.githubusercontent.com/128567810/230122201-baa8e650-4dd3-482e-b30b-1f77ca92349c.png)

### Test Case 2

Ada keadaan dimana pengguna salah membeli salah satu barang dari belanjaan yang telah ditambahkan, maka pengguna menggunakan _method_ `delete_item()` untuk menghapus item. Item yang ingin dihapuskan adalah __Pasta Gigi__

Dari program `Super Cashier` dihasilkan output:

```python
trnsct_123.delete_item()
```

![Test Case 2](https://user-images.githubusercontent.com/128567810/230122259-d3e5a055-0ed6-4b8c-8f5b-b2d194ecd389.png)

### Test Case 3

Ternyata setelah dipikir - pikir pengguna salah memasukkan item yang ingin dibelanjakan! Daripada menghapus satu - satu, maka pengguna cukup menggunakan method `reset_transaction()` untuk menghapus semua item yang sudah ditambahkan.

Dari program `Super Cashier` dihasilkan output:

```python
trnsct_123.delete_item()
```

![Test Case 3](https://user-images.githubusercontent.com/128567810/230119211-3f7efbd8-8d86-4e81-9f09-02bda4f60950.png)

### Test Case 4

Setelah pengguna selesai berbelanja, pengguna akan menghitung total belanja yang harus digunakan menggunakan _method_ `total_price()`. Sebelum mengeluarkan output total belanja akan menampilkan barang-barang yang dibeli.

Dari program `Super Cashier` dihasilkan output:

```python
trnsct_321.total_price()
```

![Test Case 4](https://user-images.githubusercontent.com/128567810/230119248-739eb53c-3f6d-475e-b5b8-71a90cc93eb3.png)

## Kesimpulan

Dari program yang telah dibuat, proyek _Super Cashier_ dapat membantu pengguna dalam melakukan aktifitas berbelanja tanpa harus datang ke supermarket. Selain itu, program ini dapat mengurangi antrian pembayaran yang ada di tempat berbelanja karena para pelanggan/pengguna dapat langsung melakukan pembayaran melalui program ini tanpa harus membayar dikasir.

Program _Super Cashier_ memiliki beberapa fitur utama yaitu:
1. Pengguna program ini dapat memasukkan nama, jumlah, dan harga barang ke daftar belanja.
2. Pengguna dapat mengubah daftar belanja dan juga dapat menghapus atau membatalkan transaksi jika terjadi kesalahan ketika penginputan barang.
3. Setelah melakukan kegiatan berbelanja, pengguna juga dapat melakukan pemeriksaan pada dafatar belanja untuk memastikan semua barang ditambahkan sudah benar.
4. Setelah berbelanja, pengguna dapat melakukan pembayaran dimana pembayaran otomatis langsung menghitung potongan harga yang didapatkan oleh pelanggan.

Proyek _Super Cashier_ juga dibuat dengan tampilan yang mudah digunakan oleh pengguna. Sehingga _Super Cashier_ ini merupakan contoh aplikasi kasir sederhana yang bisa dikembangkan dan disesuaikan dengan kebutuhan bisnis.

## _Future Works_

Ada beberapa kemungkinan yang dapat dikembangkan dari program _Super Cashier_ kedepannya, meliputi:
1. Peningkatan antar muka pengguna. Menambahkan fitur seperti antarmuka yang lebih ramah pengguna atau lebih interaktif dapat meningkatkan pengalaman pengguna dan memudahkan mereka dalam menggunakan aplikasi.
2. Walaupun program ini bersifat sederhana, menu pembayaran dapat dikembangkan, dengan pengguna dapat memasukan pembayaran baik itu berupa cash, kartu kredit, ataupun e-wallet. Sehingga akan membuat aplikasi lebih fleksibel dan memudahkan pelanggan untuk dapat melakukan pembayaran.
3. Karena ini merupakan sistem belanja. Perlu ditambahkan fitur yang mengatur tentang __stok barang__ sehingga adanya pembaharuan ketika barang itu terjual ataupun memperingatkan ketika stock barang yang dibeli oleh pelanggan akan habis.
4. Untuk memudahkan pemilik supermarket mendata laporan penjualan. Dibutuhkan fitu laporan penjualan, dimana fitur ini akan menghasilakan laporan penjualan dari barang yang telah di beli oleh para pelanggan. Sehingga akan membantu pemilik supermarket untuk membuat keputusan yang lebih baik untuk meningkatkan keuntungan supermarket.
