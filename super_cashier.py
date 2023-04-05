"""
Module ini berisi kelas Transaction dan beberapa method untuk program Super Cashier,
yang digunakan untuk mengelola daftar belanja hingga melakukan pembayaran.

Module ini akan di import ke module menu.py
"""

import os  # Untuk menjalankan perintah clear terminal
from tabulate import tabulate  # Untuk membuat format tabel


class Transaction():
    """
    Kelas yang digunakan untuk melakukan transaksi belanja.
    Yang menyimpan seluruh transaksi barang, jumlah, dan harga

    Atributes:
    ----------
        daftar_belanja (dict) : Daftar barang belanja yang berisi {"nama": [jumlah,harga,total]}.

        total_harga_belanja (int) : Total harga dari semua barang yang telah dibeli.

        id_transaksi (int) : objek yang digunakan untuk memanggil klass transaksi

    Methods:
    --------
    add_item()
        Menambahkan barang ke daftar belanja

    list_item()
        Menampilkan daftar belanja setiap method lain dilakukan.
        Digunakan untuk pengecekkan barang awal.

    update_item_name()
        Mengganti nama barang pada daftar belanja.

    update_item_qty()
        Mengannti jumlah barang pada daftar belanja.

    update_item_price()
        Mengganti harga barang pada daftar belanja.

    delete_item()
        Mengahapus salah satu barang dari daftar belanja

    reset_transaction()
        Menghapus seluruh isi dari daftar belanja.
        Membatalkan transaksi

    check_order()
        Memeriksa seluruh isi daftar belanja,
        yang ditampilkan dalam bentuk table.

    total_price()
        Menghitung total harga dari transaksi yang dilakukan.
        Jika total seluruh harga memenuhi kriteria,
        maka akan mendapatkan potongan harga.

    """

    def __init__(self, id_transaksi):
        """
        Inisialisasi objek pada kelas Transaction.
        """
        # Keranjang belanja menampung daftar belanja
        self.daftar_belanja = {}

        # Counter yang digunakan untuk mengitung total harga belanja
        self.total_harga_belanja = 0

        # digunakan untuk memanggil kelas transaksi
        self.id_transaksi = id_transaksi

    def add_item(self):
        """
        Method yang digunakan untuk menambahkan barang kedalam daftar belanja.

        User akan diminta untuk memasukkan:
            1. nama_barang (str)
                jika terjadi error maka pesan akan ditampilkan

            2. jumlah_barang (int)
                Pengguna diminta untuk memasukkan jumlah barang yang ingin
                dibeli

            3. harga_barang (int)
                Pengguna diminta untuk memasukkan harga barang yang ingin
                dibeli

        Exceptions
        ----------
        ValueError:
            Jika jumlah atau harga barang yag dimasukkan selain angka (int),
            maka error akan muncul dan jumlah atau harga barang dianggap nol.
        """
        # Print Header untuk menambah nama barang
        print("==================")
        print("Menambahkan Barang")
        print("==================")

        # Input nama barang
        while True:
            nama_barang = input("Masukkan nama barang: ").title()
            if nama_barang == "":
                print(
                    "Anda belum memasukan apapun! Silahkan masukkan nama barang dengan benar!")
            else:
                break

        # Input jumlah dan harga barang
        jumlah_barang = input("Masukkan jumlah barang: ")
        harga_barang = input("Masukkan harga barang: ")

        # Mengubah input jumlah barang <str> menjadi <int>
        try:
            jumlah_barang = int(jumlah_barang)

        # Jika jumlah barang yang dimasukan selain angka atau spasi maka akan diubah menjadi 0
        except ValueError:
            print("Jumlah barang tidak tepat, dimasukkan sebagai 0")
            jumlah_barang = 0

        # Mengubah input harga barang <str> menjadi <int>
        try:
            harga_barang = int(harga_barang)

        # Jika harga barang yang dimasukan selain angka atau spasi maka akan diubah menjadi 0
        except ValueError:
            print("Harga barang tidak tepat, dimasukkan sebagai 0")
            harga_barang = 0

        # Tambahkan atau update barang dalam daftar belanja
        # Jika nama barang sudah ada dalam daftar belanja
        # Maka hanya jumlah barang yang ditambahkan.
        if nama_barang in self.daftar_belanja:
            print("Nama barang sudah ada, akan menambahkan jumlah saja")

            update_jumlah_barang = self.daftar_belanja[nama_barang][0] + \
                jumlah_barang
            total_harga = update_jumlah_barang * \
                self.daftar_belanja[nama_barang][0]

            self.daftar_belanja[nama_barang][0] = update_jumlah_barang
            self.daftar_belanja[nama_barang][1] = total_harga

        # Jika nama barang belum ada dalam daftar belanja, maka barang baru akan ditambahkan
        elif nama_barang not in self.daftar_belanja:
            total_harga = jumlah_barang * harga_barang

            self.daftar_belanja[nama_barang] = [
                jumlah_barang, harga_barang, total_harga]

        # Print jumlah barang yang di tambahkan
        print(f"Anda menambahkan barang '{nama_barang}' "
              f"sejumlah: {self.daftar_belanja[nama_barang][0]}")

        # Menanyakan ke pengguna apakah ingin menambahkan barang lagi atau tidak
        while True:
            tambah_barang = input(
                "Apakah ingin menambahkan barang lagi? (Ya/Tidak)").lower()
            if tambah_barang == "ya":
                os.system('cls')
                self.add_item()  # Kembali ke fungsi awal
                break
            if tambah_barang == "tidak":
                os.system('cls')  # Perintah untuk membuat clear terminal
                self.list_item()
                break
            else:
                print("Input tidak valid. Mohon masukkan Ya atau Tidak.")
                continue

    def list_item(self):
        """
        Method menampilkan daftar belanja pada daftar dengan format tabel.
        Dipanggil oleh fungsi lainnya untuk menampilkan daftar belanja,
        item yang telah ditambahkan atau diedit
        """

        headers = ["No", "Nama", "Jumlah", "Harga", "Total"]
        table_data = []
        index = 1  # Counter untuk menghasilkan nomor pada tabel

        # Looping untuk melakukan iterasi pada key dan value di daftar belanja
        for key, value in self.daftar_belanja.items():
            table_data.append([index, key, value[0], value[1], value[2]])
            index += 1  # Nomor pada tabel

        # Menampilkan daftar belanja berbentu tabel
        print("\n+---------------+")
        print("| Daftar Belanja:")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def update_item_name(self):
        """
        Method yang digunakan untuk mengubah nama barang pada daftar belanja.

        User diminta untuk memasukkan:
        1. nama_barang (str)
            Nama barang yang akan diganti

        2. nama_barang_baru (str)
            Nama barang yang akan mengganti nama barang yang ada.

        Returns:
        --------
            Pesan (str)
                yang menunjukan bahwa daftar belanja kosong
        """
        # Print header untuk mengubah nama barang
        print("====================")
        print("Mengubah Nama Barang")
        print("====================")

        # Untuk mengecek apakah daftar belanja masih kosong atau tidak
        if len(self.daftar_belanja) == 0:
            pesan = print("Maaf anda belum memasukkan apapun, daftar belanja masih kosong. "
                          "Silahkan berbelanja!")
            return pesan

        # Meminta input dari pengguna untuk nama yang akan diubah
        while True:
            nama_barang = input(
                "Masukkan nama barang yang ingin diubah: ").title()
            if nama_barang == "":  # Jika memasukkan input kosong
                print(
                    "Anda belum memasukan apapun! Silahkan masukkan nama barang dengan benar!")
            elif nama_barang not in self.daftar_belanja:  # Jika nama tidak ada di daftar belanja
                print(f"Nama barang '{nama_barang}' tidak ditemukan, "
                      "mohon input nama barang dengan benar!")
            else:
                break

        # Meminta input dari pengguna untuk nama barang baru
        while True:
            nama_barang_baru = input(
                "Masukkan nama barang yang baru: ").title()
            if nama_barang_baru == "":
                print(
                    "Anda belum memasukan apapun, silahkan masukkan nama barang dengan benar!")
            else:
                break

        # Mengubah nama barang pada daftar belanja
        self.daftar_belanja[nama_barang_baru] = self.daftar_belanja.pop(
            nama_barang)

        # Perintah untuk membuat clear terminal
        os.system('cls')

        # Menampilkan daftar belanja yang telah diubah
        self.list_item()

        # Menampilkan pesan nama barang berhasil diubah
        print(f"Nama barang berhasil diubah! barang '{nama_barang}' "
              f"diubah menjadi '{nama_barang_baru}'")

        # Menanyakan ke pengguna apakah ingin mengubah nama barang lain
        while True:
            tambah_barang = input(
                "Apakah ada nama barang yang ingin diubah lagi? (Ya/Tidak)").lower()
            if tambah_barang == "ya":
                self.update_item_name()  # Kembali ke fungsi awal
                break
            if tambah_barang == "tidak":
                os.system('cls')  # Perintah untuk membuat clear terminal
                self.list_item()
                break
            else:
                print("Input tidak valid. Mohon masukkan Ya atau Tidak!")
                continue

    def update_item_qty(self):
        """
        Method yang digunakan untuk mengubah jumlah barang pada daftar belanja.

        User diminta untuk memasukkan:
        1. nama_barang (str)
            Nama barang yang akan diganti

        2. jumlah_barang_baru (int)
            jumlah barang yang akan mengganti jumlah barang yang ada.

        Exceptions
        ----------
        ValueError:
            Jika jumlah atau harga barang yag dimasukkan selain angka (int),
            maka error akan muncul dan jumlah atau harga barang dianggap nol.

        Returns:
        --------
            Pesan (str)
                yang menunjukan bahwa daftar belanja kosong
        """
        # Print header untuk mengubah jumlah barang
        print("========================")
        print(" Mengubah Jumlah Barang ")
        print("========================")

        # Untuk mengecek apakah daftar belanja masih kosong atau tidak
        if len(self.daftar_belanja) == 0:
            pesan = print(
                "Anda belum memasukkan apapun, daftar belanja masih kosong. Silahkan berbelanja!")
            return pesan

        # Meminta input dari pengguna untuk nama yang akan diubah
        while True:
            nama_barang = input("Masukkan nama barang: ").title()
            if nama_barang == "":  # Jika memasukkan input kosong
                print(
                    "Anda belum memasukan apapun, silahkan masukkan nama barang dengan benar!")
            elif nama_barang not in self.daftar_belanja:  # Jika nama tidak ada di daftar belanja
                print(f"Nama barang '{nama_barang}' tidak ditemukan, "
                      "mohon input nama barang dengan benar!")
            else:
                break

        # Meminta input pengguna untuk jumlah barang baru
        while True:
            try:
                jumlah_barang_baru = int(
                    input("Masukkan jumlah barang yang baru: "))
                break

            except ValueError:
                print("Jumlah barang tidak tepat, tolong masukkan angka!")

        # Memperbaharui jumlah baru yang ada di daftar belanja
        self.daftar_belanja[nama_barang][0] = jumlah_barang_baru

        # Memperbaharui harga total per barang dengan jumlah barang baru
        total_harga_baru = jumlah_barang_baru * \
            self.daftar_belanja[nama_barang][1]

        # Memperbaharui total harga baru per barang dalam daftar belanja
        self.daftar_belanja[nama_barang][2] = total_harga_baru

        # Perintah untuk membuat clear terminal
        os.system('cls')

        # Menampilkan daftar belanja yang telah diubah
        self.list_item()

        # Menampilkan barang yang telah diubah jumlahnya
        print(f"Perubahan jumlah untuk nama barang '{nama_barang}' "
              f"berhasil! Jumlah diubah menjadi '{jumlah_barang_baru}'")

        # Menanyakan ke pengguna apakah ingin mengubah jumlah barang lain
        while True:
            tambah_barang = input(
                "Apakah ada jumlah barang yang ingin diubah lagi? (Ya/Tidak)").lower()
            if tambah_barang == "ya":
                self.update_item_qty()  # Kembali ke fungsi awal
                break
            if tambah_barang == "tidak":
                os.system('cls')  # Perintah untuk membuat clear terminal
                self.list_item()
                break
            else:
                print("Input tidak valid. Mohon masukkan Ya atau Tidak.")
                continue

    def update_item_price(self):
        """
        Method yang digunakan untuk mengubah harga barang pada daftar belanja.

        User diminta untuk memasukkan:
        1. nama_barang (str)
            Nama barang yang akan diganti

        2. harga_barang_baru (int)
            harga barang yang akan mengganti harga barang yang ada.

        Exceptions
        ----------
        ValueError:
            Jika jumlah atau harga barang yag dimasukkan selain angka (int),
            maka error akan muncul dan jumlah atau harga barang dianggap nol.

        Returns:
        --------
            Pesan (str)
                yang menunjukan bahwa daftar belanja kosong
        """
        # Print header untuk mengubah harga barang
        print("=====================")
        print("Mengubah Harga Barang")
        print("=====================")

        # Untuk mengecek apakah daftar belanja masih kosong atau tidak
        if len(self.daftar_belanja) == 0:
            pesan = print(
                "Anda belum memasukkan apapun, daftar belanja masih kosong. Silahkan berbelanja!")
            return pesan

        # Meminta input dari pengguna untuk nama yang akan diubah
        while True:
            nama_barang = input("Masukkan nama barang: ").title()
            if nama_barang == "":  # Jika memasukkan input kosong
                print(
                    "Anda belum memasukan apapun, silahkan masukkan nama barang dengan benar!")
            elif nama_barang not in self.daftar_belanja:  # Jika nama tidak ada di daftar belanja
                print(f"Nama barang '{nama_barang}' tidak ditemukan, "
                      "mohon input nama barang dengan benar")
            else:
                break

        # Meminta input pengguna untuk harga barang baru
        while True:
            try:
                harga_barang_baru = int(
                    input("Masukkan harga barang yang baru: "))
                break

            except ValueError:
                print("Harga barang tidak tepat, tolong masukkan angka")

        # Memperbaharui harga baru yang ada di daftar belanja
        self.daftar_belanja[nama_barang][1] = harga_barang_baru

        # Memperbaharui harga total per barang dengan harga barang yang baru
        total_harga_baru = harga_barang_baru * \
            self.daftar_belanja[nama_barang][0]

        # Memperbaharui total harga baru per barang dalam daftar belanja
        self.daftar_belanja[nama_barang][2] = total_harga_baru

        # Perintah untuk membuat clear terminal
        os.system('cls')

        # Menampilkan daftar belanja yang telah diubah
        self.list_item()

        # Menampilkan barang yang telah diubah harganya
        print(f"Perubahan harga untuk nama barang '{nama_barang}' berhasil! "
              f"harga diubah menjadi Rp.{harga_barang_baru}")

        # Menanyakan ke pengguna apakah ingin mengubah harga barang yang lain
        while True:
            tambah_barang = input(
                "Apakah ada harga barang yang ingin diubah lagi? (Ya/Tidak)").lower()
            if tambah_barang == "ya":
                self.update_item_price()  # Kembali ke fungsi awal
                break
            if tambah_barang == "tidak":
                os.system('cls')  # Perintah untuk clear terminal
                self.list_item()
                break
            else:
                print("Input tidak valid. Mohon masukkan Ya atau Tidak.")
                continue

    def delete_item(self):
        """
        Method yang digunakan untuk menghapus salah satu barang dari daftar belanja

        Pengguna diminta untuk memasukkan:
        1. nama_barang (str)
            Nama barang yang akan dihapus

        Returns:
        --------
            Pesan (str)
                yang menunjukan bahwa daftar belanja kosong
        """
        # Print header untuk menghapus barang
        print("================")
        print("Menghapus Barang")
        print("================")

        # Cek apakah daftar belanja kosong atau tidak
        if len(self.daftar_belanja) == 0:
            print("Daftar belanja masih kosong, tidak ada yang bisa dihapus. "
                  "Silahkan berbelanja dahulu!")
            return

        # Meminta pengguna untuk memasukkan nama barang yang ingin di hapus
        while True:
            nama_barang = input(
                "Masukkan nama barang yang ingin dihapus: ").title()
            if nama_barang == "":  # Jika memasukkan input kosong
                print(
                    "Anda belum memasukan apapun, silahkan masukkan nama barang dengan benar!")
            elif nama_barang not in self.daftar_belanja:  # Jika nama tidak ada di daftar belanja
                print(f"Nama barang '{nama_barang}' tidak ditemukan, "
                      "mohon input nama barang dengan benar!")
            else:
                break

        # Menghapus barang dari daftar belanja
        self.daftar_belanja.pop(nama_barang)

        # Perintah untuk membuat clear terminal
        os.system('cls')

        # Menampilkan daftar belanja yang telah diubah
        self.list_item()

        # Menampilkan barang yang berhasil di hapus
        print(f"'{nama_barang}' berhasil dihapus!")

        # Menanyakan pengguna apakah ingin menghapus barang lain atau tidak
        while True:
            tambah_barang = input(
                "Apakah ada barang yang ingin di hapus lagi? (Ya/Tidak)").lower()
            if tambah_barang == "ya":
                self.delete_item()  # kembali ke fungsi awal
                break
            if tambah_barang == "tidak":
                os.system('cls')  # Perintah untuk clear terminal
                self.list_item()
                break
            else:
                print("Input tidak valid. Mohon masukkan Ya atau Tidak.")
                continue

    def reset_transaction(self):
        """
        Method yang digunakan untuk membatalkan transaksi.
        Dapat menghapus semua barang dalam daftar belanja.

        Returns:
        --------
            Pesan (str)
                yang menunjukan bahwa daftar belanja kosong
        """
        # Print header membatalkan transaksi
        print("=====================")
        print("Membatalkan Transaksi")
        print("=====================")

        # Mengecek apakah di daftar belanja kosong tidak
        if len(self.daftar_belanja) == 0:
            pesan = print("Daftar belanja masih kosong, tidak ada yang bisa dibatalkan. "
                          "Silahkan berbelanja dahulu!")
            return pesan

        # Menanyakan kepada pengguna apakah yakin ingin mengapus semua barang
        while True:
            konfirmasi = input(
                "Apakah anda yakin untuk menghapus semua daftar belanja? (Ya/Tidak)")
            if konfirmasi == "ya":
                # Perintah menghapus seluruh data dalam daftar belanja
                self.daftar_belanja.clear()

                # clear terminal
                os.system('cls')

                # Menampilkan proses penghapusan seluruh barang berhasil
                print("Semua barang dalam daftar belanja telah dihapus!")
                self.list_item()
                break
            if konfirmasi == "tidak":
                self.list_item()
                break
            else:
                print("Input yang anda masukkan salah, tolong masukkan Ya atau Tidak")
                continue

    def check_order(self):
        """
        Method yang digunakan pengecekkan pada daftar belanja.

        Method ini melakukan proses sebagai berikut:
        1. Memeriksa apakah daftar belanja kosong atau tidak.
            Jika iya maka akan menampilkan pesan bahwa daftar belanja kosong.

        2. Memeriksa apakah nama barang terdapat inpu berupa spasi.
            Jika iya maka akan menampilkan pesan, kesalahan input nama barang.

        3. Memerika apakah jumlah atau harga barang apakah ada nilai minus atau nol.
            Jika iya maka akan menampilkan bahwa ada kesalahan input jumlah atau harga.

        Pengguna akan mendapatkan informasi:
        1. Daftar belanja yang telah di check
        2. Pesan yang berisi kesalahan atau pesanan yang dilakukan sudah benar
        """

        # Print header memeriksa pesanan
        print("=================")
        print("Memeriksa Pesanan")
        print("=================")

        if len(self.daftar_belanja) == 0:  # Jika daftar belanja kosong
            print("Daftar belanja masih kosong, anda belum memasukkan apapun!")
        elif " " in self.daftar_belanja:  # Jika terdapat spasi " " pada nama barang
            print("Terdapat kesalahan input pada nama barang, "
                  "Silahkan cek kembali daftar belanjaan anda!")
        # Mengecek pada jumlah dan harga barang apakah ada nilai minus atau nol
        elif any(data[0] <= 0 or data[1] <= 0 for data in self.daftar_belanja.values()):
            print("Terdapat kesalahan input pada Harga atau Jumlah Barang. "
                  "Silahkan cek kemmbali daftar belanjaan anda!")
        else:
            print("Pesanan anda sudah benar!")

        self.list_item()  # Menampilkan daftar belanja yang telah di periksa/check

    def total_price(self):
        """
        Menampilkan total harga belanja dan jumlah yang harus dibayarkan oleh pengguna.

        Potongan harga yang didapatkan pengguna harus memenuhi kriteria:
        1. Jika total harga belanja lebih dari 500_000,
            Maka akan mendapatkan potongan harga 10%

        1. Jika total harga belanja lebih dari 300_000,
            Maka akan mendapatkan potongan harga 8%

        1. Jika total harga belanja lebih dari 200_000,
            Maka akan mendapatkan potongan harga 5%

        Pengguna akan mendapatkan informasi berupa:
        1. Daftar belanja
        2. Total harga seluruh
        3. Total harga yang telah mendapatkan potongan harga
        """
        # Menampilkan header untuk pembayaran
        print("=================")
        print("    PEMBAYARAN   ")
        print("=================")

        # Menghitung total harga belanja
        for total in self.daftar_belanja:
            self.total_harga_belanja += self.daftar_belanja[total][2]

        # Menampilkan daftar belanja dalam bentuk tabel
        headers = ["No", "Nama", "Jumlah", "Harga", "Total"]
        table_data = []
        index = 1  # Counter untuk membuat nomor dalam tabel

        # Looping untuk mengeluarkan nilai key dan value dalam daftar belanja
        for key, value in self.daftar_belanja.items():
            table_data.append([index, key, value[0], value[1], value[2]])
            index += 1

        # Menampilkan seluruh daftar belanja dalam bentuk tabel
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

        # Menampilkan total harga belanja
        format_harga = f"{self.total_harga_belanja:,.0f}".replace(",", ".")
        pesan_total = f"Total belanja anda sebesar Rp. {format_harga}"
        print(pesan_total)

        # Menghitung panjang teks agar menyesuikan garis
        logo = (len(pesan_total)) - 1

        # Menampilkan garis horizontal di bawah total belanja
        print("+" + ("-" * logo) + "+")

        # Memberikan potongan harga jika total harga belanja memnuhi kriteria yang ada
        if self.total_harga_belanja > 500_000:
            potongan_harga = self.total_harga_belanja * 0.1
            self.total_harga_belanja -= potongan_harga
            print("Selamat! Anda mendapatkan diskon 10%")
            print("+-----------------------------------+")

        elif self.total_harga_belanja > 300_000:
            potongan_harga = self.total_harga_belanja * 0.08
            self.total_harga_belanja -= potongan_harga
            print("Selamat! Anda mendapatkan diskon 8%")
            print("+----------------------------------+")

        elif self.total_harga_belanja > 200_000:
            potongan_harga = self.total_harga_belanja * 0.05
            self.total_harga_belanja -= potongan_harga
            print("Selamat! Anda mendapatkan diskon 5%")
            print("+----------------------------------+")

        # Menampilkan jumlah yang harus dibayarkan setelah dikenakan potongan harga
        total_seluruh = f"{self.total_harga_belanja:,.0f}".replace(",", ".")
        total_pesan = f"Jumlah yang dibayarkan sebesar Rp. {total_seluruh}"
        print(total_pesan)

        # Menghitung panjang text agar menyesuikan garis
        logo = (len(total_pesan)) - 1

        # Menampilkan garis horizontal di bawah jumlah yang harus dibayarkan
        print("+" + ("-" * logo) + "+")
