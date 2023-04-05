# Python Project: Super-Cashier

## Latar Belakang Project:

__Super Cashier__ merupakan suatu program sederhana yang dapat digunakan para pelanggan untuk melakukan transaksi belanja pada suatu supermarket. Program ini menggunakan bahasa pemrograman `Python` yang dijalankan sesuai fungsi dasar mesin kasir sehingga para pelanggan dapat melakukan proses belanja secara mandiri atau _self-service_.

Program ini dibuat dengan mempertimbangkan beberapa hal:
1. Jika melakukan belanja di supermarket secara langsung dengan keadaan supermarket yang ramai pelanggan akan menyebabkan antrian semakin panjang dan membuat seluruh pembeli akan menunggu dengan sangat lama untuk melakukan pembayaran di kasir.
2. Ada beberapa pelanggan yang tidak berada di kota tempat supermarket itu berada, sehingga perlu adanya program dengan fitur fitur yang membantu menyelesaikan masalah tersebut.
3. Sehingga perlu dibuatnya suatu program yang dimana pelanggan dapat bisa langsung memasukkan item yang dibeli, jumlah item yang dieli, dan harga item yang dibeli serta fitur yang lain dengan harapan dapat menjangkau lebih banyak costumer serta meningkatkan kepuasan pelanggan dalam berbelanja di supermarket tersebut.

## Fitur dan Kebutuhan:
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
    - Jika total harga belanja pelanggan __diatas Rp. 300.000 maka__ pelanggan akan mendapatkan diskon __8%__.
    - Jika total harga belanja pelanggan __diatas Rp. 500.000__ maka pelanggan akan mendapatkan diskon __10%__.

## Alur Program
<p align="center">
    <img src="https://github.com/yogaaprilian/Super-Cashier/blob/fe34064e9426479902da4e0fa1895bdbe17c91fb/Flow%20Chart%20Project.png" width="500">
</p>

Berdasarkan Diagram Alir, program tersebut akan berjalan seperti berikut:
- Ketika program di mulai, pelanggan yang akan melakukan kegiatan berbelanja harus membuat ID Transaksi yang berguna untuk menjelankan program selanjutnya. 
- Menu akan ditampilkan, pelanggan akan memilih menu program apa yang akan dijalankan selanjutnya. 
- Pelanggan akan menambahkan barang yang akan dibeli dengan memasukkan nama barang, jumlah barang, dan harga barang yang akan dibeli.
    - Jika ingin menambahkan barang lagi, pelanggan dapat memiliih ‘Ya’.
- Setelah melakukan penambahan barang yang dibeli, program akan menampilkan daftar belanjaan yang telah ditambahkan berserta total belanjaanya.
- Pelanggan dapat melakukan pengecekkan daftar belanja.
    - Jika tidak terdapat kesalahan input, maka pelanggan dapat memilih ‘Tidak’
    - Jika ‘Ya’ dari tampilan daftar belanja terdapat kesalahan, maka pelanggan dapat memperbaharui nama/harga/jumlah/yang telah ditambahkan.
- Selain itu, pelanggan dapat melakukan pengapusan barang yang telah di tambahkan dengan pilihan:
    - Menghapus salah satu barang atau lebih barang yang telah ditambahkan.
    - Melakukan pengapusan semua barang ada di daftar belanja, jika ingin membatalkan kegiatan belanja.
- Setelah melakukan pengecekkan, program akan melakukan penampilan harga total. Pelanggaan dapat mengecek kembali apakah masih ada barang yang ingin di perbaharui atau tidak.
- Jika maka proses akan dilanjutkan ke tahap pembayaran
    - Pelanggan akan mendapatkan harga diskon apalagi total dari seluruh harga memenuhi kriteria mendapatkan diskon.


