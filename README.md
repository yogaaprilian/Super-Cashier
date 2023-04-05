# Python Project: Super-Cashier

## Latar Belakang Project:

__Super Cashier__ merupakan suatu program sederhana yang dapat digunakan para pelanggan untuk melakukan transaksi belanja pada suatu supermarket. Program ini menggunakan bahasa pemrograman `Python` yang dijalankan sesuai fungsi dasar mesin kasir sehingga para pelanggan dapat melakukan proses belanja secara mandiri atau _self-service_.


Program ini dibuat dengan mempertimbangkan beberapa hal:
1. Jika melakukan belanja di supermarket secara langsung dengan keadaan supermarket yang ramai pelanggan akan menyebabkan antrian semakin panjang dan membuat seluruh pembeli akan menunggu dengan sangat lama untuk melakukan pembayaran di kasir.
2. Ada beberapa pelanggan yang tidak berada di kota tempat supermarket itu berada, sehingga perlu adanya program dengan fitur fitur yang membantu menyelesaikan masalah tersebut.
3. Sehingga perlu dibuatnya suatu program yang dimana pelanggan dapat bisa langsung memasukkan item yang dibeli, jumlah item yang dieli, dan harga item yang dibeli serta fitur yang lain dengan harapan dapat menjangkau lebih banyak costumer serta meningkatkan kepuasan pelanggan dalam berbelanja di supermarket tersebut.

## Feature Requirements:

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
    <img src="https://user-images.githubusercontent.com/128567810/230075253-12365b6b-c4b5-4ddd-b49f-c377894a63e1.png" width="500">
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

Dalam modul ini berisi program yang akan dijalankan ketika pengguna melakukan belanja menggunakan program __Super Cashier__. Dalam module ini mengunakan _library_ dari bahasa pemograman python yaitu:

1. `Python os Module` yang digunakan untuk membantu _clear_ terminal ketika program dijalankan
2. `Python tabulate Module` yang digunakan untuk membuat table ketika menampilkan daftar belanja atau melakukan pembayaran.

Dalam modul ini terdapat `Class Transaction` yang didalamnya terdapat beberapa method meliputi:

#### 1. Method `__init__()`
Merupakan _method_ yang digunakan untuk menginisialisasi suatu objek jika objek tersebut dibuat di _method_ lain. 

Dalam _method_ ini memuat 
- `self.daftar_belanja` untuk menyimpan daftar belanja penguna 
- `self.total_harga_belanja` yang digunakan sebagai _counter_ untuk menjumlahkan total harga seluruh belanjaan.

https://github.com/yogaaprilian/Super-Cashier/blob/0cac923e6eb815a11963867192e308121c7db5da/super_cashier.py#L12-L67

#### 2. Method `add_item()`
Merupakan _method_ yang digunakan untuk menambahkan daftar belanja dengan memasuka nilai `nama_barang`, `jumlah_barang`, dan `harga_barang`

https://github.com/yogaaprilian/Super-Cashier/blob/0cac923e6eb815a11963867192e308121c7db5da/super_cashier.py#L69-L167

#### 3. Method `list_item()`
Merupakan _method_ yang digunakan menampilkan daftar belanja ketika pengguna selesai melakukan transaksi.

_Method_ ini akan dipanggil oleh _method_ lain didalam `Class Transaction()`

https://github.com/yogaaprilian/Super-Cashier/blob/0cac923e6eb815a11963867192e308121c7db5da/super_cashier.py#L168-L188

#### 4. Method `update_item_name()`
_Method_ yang digunakan untuk mengubah nama barang jika terjadi kesalahan input nama atau pelanggan ingin mengganti nama barang.

Pada _method_ ini pengguna diminta untuk memasukkan nama yang lama dan nama yang baru.

https://github.com/yogaaprilian/Super-Cashier/blob/0cac923e6eb815a11963867192e308121c7db5da/super_cashier.py#L189-L267

#### 5. Method `update_item_qty()`
_Method_ yang digunakan untuk mengubah jumlah barang jika terjadi kesalahan input jumlah barang dan pelanggan ingin mengubah jumlah barang tersebut

Pada _method_ ini pengguna diminta untuk memasukkan nama yang ingin diubah dan jumlah yang baru.

https://github.com/yogaaprilian/Super-Cashier/blob/0cac923e6eb815a11963867192e308121c7db5da/super_cashier.py#L268-L357

#### 6. Method `update_item_price()`
Merupakan _method_ yang digunakan untuk mengubah harga per barang jika terjadi kesalahan input harga barang dan pelanggan ingin mengubah jumlah barang tersebut.

Pada _method_ ini pengguna diminta untuk memasukkan nama yang ingin diubah dan harga per barang yang baru.

https://github.com/yogaaprilian/Super-Cashier/blob/0cac923e6eb815a11963867192e308121c7db5da/super_cashier.py#L358-L447

#### 7. Method `delete_item()`
Merupakan _method_ yang dapat digunakan oleh pengguna untuk menghapus salah satu barang.

Pada _method_ ini pengguna akan diminta untuk memasukkan nama barang yang akan dihapus.

https://github.com/yogaaprilian/Super-Cashier/blob/0cac923e6eb815a11963867192e308121c7db5da/super_cashier.py#L448-L511

#### 8. Method `reset_transaction()`
_Method_ ini digunakan untuk menghapus seluruh transaksi yang telah dilakukan.

_Method_ ini juga dapat digunakan jika pengguna ingin membatalkan transaksi.

https://github.com/yogaaprilian/Super-Cashier/blob/0cac923e6eb815a11963867192e308121c7db5da/super_cashier.py#L512-L550

#### 9. Method `check_order()`
_Method_ yang digunakan untuk melakukan pemeriksaan pada daftar belanja.

Dikarenakan program __Super Cashier__ masih menggunakan sistem _self service_ yang dimana pengguna dapat melakukan kesalahan input. _Method_ ini akan membantu pengguna untuk memeriksa apakah semua yang telah dimasukkan dalam daftar belanja sudah benar atau belum.

https://github.com/yogaaprilian/Super-Cashier/blob/0cac923e6eb815a11963867192e308121c7db5da/super_cashier.py#L552-L589

#### 10. Method `total_price()`
Jika pengguna telah selesai melakukan belanja, maka dapat menggunakan _method_ ini untuk menjumlahkan seluruh daftar belanja yang ada.

_Method_ ini juga digunakan untuk menghitung apabila total harga belanja pengguna memenuhi kriteria akan mendapatkan potongan harga.

https://github.com/yogaaprilian/Super-Cashier/blob/0cac923e6eb815a11963867192e308121c7db5da/super_cashier.py#L590-L670

### Module `menu.py`

## Hasil Test Case

## Kesimpulan dan Saran
