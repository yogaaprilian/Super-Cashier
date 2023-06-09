"""
Modul ini digunakan untuk menampilkan menu pada program super cashier,
menu yang digunakan untuk pengguna lebih mudah melakukan transaksi belanja.
"""

import os  # Untuk menjalankan perintah clear terminal
from IPython.display import clear_output
from IPython import get_ipython
import super_cashier  # Untuk import kelas dan fungsi


# Jika program dijalankan di Jupyter Notebook
if get_ipython() is not None:
    # output akan dihapus ketika output baru dihasilkan
    clear_output(wait=True)

# Jika program dijalankan di terminal atau konsol
else:
    os.system('cls' if os.name == 'nt' else 'clear')

# Dictionary untuk menyimpan ID transaksi
ID_transaksi = []

# Print header untuk menu input ID transaksi
print("=======================\n",
      "   **SUPER CASHIER**   \n",
      "=======================")

# Pengguna diminta untuk membuat ID transaksi
while True:
    try:
        transaksi_ID = int(input("Masukkan ID transaksi (angka): "))
        break

    except ValueError:
        print('Mohon input ID transaksi dengan benar!')

# Menampilkan bahwa pengguna berhasil membuat ID transaksi
print(f"Berikut ID transaksi anda {transaksi_ID}, Selamat Berbelanja!\n")

# Menyimpan ID transaksi
ID_transaksi.append(transaksi_ID)

# instance variable untuk memanggil kelas transaksi
cashier = super_cashier.Transaction(transaksi_ID)


def tambah_barang():
    """Fungsi yang digunakan untuk memanggil method add_item()"""
    # Membersihkan terminal
    cashier.clear_screen()

    # Memanggil method Transaction.add_time()
    cashier.add_item()

    # Kembali ke menu belanja
    second_menu()


def ubah_nama():
    """Fungsi yang digunakan untuk memanggil method update_item_name()"""
    # Membersihkan terminal
    cashier.clear_screen()

    # Memanggil method Transaction.list_item() menampilkan daftar belanja
    cashier.list_item()

    # Memanggil method untuk mengubah nama
    cashier.update_item_name()

    # Kembali ke menu edit belanja/transaksi
    modify_menu()


def ubah_jumlah():
    """Fungsi yang digunakan untuk memanggil method updat_item_qty()"""
    # Membersihkan terminal
    cashier.clear_screen()

    # Memanggil method Transaction.list_item() menampilkan daftar belanja
    cashier.list_item()

    # Memanggil method untuk mengubah jumlah
    cashier.update_item_qty()

    # Kembali ke menu edit belanja/transaksi
    modify_menu()


def ubah_harga():
    """Fungsi yang digunakan untuk memanggil method updat_item_price()"""
    # Membersihkan terminal
    cashier.clear_screen()

    # Memanggil method Transaction.list_item() menampilkan daftar belanja
    cashier.list_item()

    # Memanggil method untuk mengubah harga
    cashier.update_item_price()

    # Kembali ke menu edit belanja/transaksi
    modify_menu()


def hapus_barang():
    """Fungsi ini digunakan untuk memanggil method delete_item()"""
    # Membersihkan terminal
    cashier.clear_screen()

    # Memanggil method Transaction.list_item() menampilkan daftar belanja
    cashier.list_item()

    # Memanggil method untuk menghapus barang
    cashier.delete_item()

    # Kembali ke menu edit belanja/transaksi
    modify_menu()


def reset_belanja():
    """Fungsi ini digunakan untuk memanggil method reset_transaction()"""
    # Membersihkan terminal
    cashier.clear_screen()

    # Memanggil method untuk menghapus seluruh barang
    cashier.reset_transaction()

    # Kembali ke menu belanja
    main_menu()


def periksa_belanja():
    """ Fungsi ini digunakan untuk memanggil method check_order()"""
    # Membersihkan terminal
    cashier.clear_screen()

    # Memanggil method untuk mengecek seluruh daftar belanja
    cashier.check_order()

    # Kembali ke menu belanja
    second_menu()


def bayar():
    """Fungsi ini digunakan untuk memanggil method total_price()"""
    # Membersihkan terminal
    cashier.clear_screen()

    # Memanggil method untuk melakukan pembayaran dan melihat total harga
    cashier.total_price()

    # Kembali ke menu utama
    main_menu()


def keluar():
    """Fungsi yang digunakan jika pelanggan keluar dari transaksi"""

    cashier.clear_screen()

    # Menanyakan apakah pengguna yakin untuk keluar
    while True:
        konfirmasi = input(
            "Apakah anda yakin untuk keluar? (Ya/Tidak)").lower()
        if konfirmasi == "ya":
            break

        if konfirmasi == "tidak":
            main_menu()

        else:
            print("Input yang anda masukkan salah, tolong masukkan Ya atau Tidak")
            continue

    # Clear Terminal
    cashier.clear_screen()

    # Menampilkan pesan terima kasih
    print("============================================\n")
    print("Terimakasih telah menggunakan Super Cashier!\n")
    print("============================================")


def modify_menu():
    """
    Fungsi yang digunakan untuk menampilkan menu edit transaksi.

    Exceptions
    ----------
    ValueError:
        Jika pengguna memasukkan selain angka (int),
        Maka except akan terjadi dimana akan menyampaikan pesan untuk menginput angka (int)
    """

    # Menampilkan daftar menu edit transaksi
    print("================================")
    print("     **MENU EDIT TRANSAKSI**    ")
    print("================================")
    print("1. Ubah Nama Barang")
    print("2. Ubah Jumlah Barang")
    print("3. Ubah Harga Barang")
    print("4. Hapus Barang")
    print("5. Hapus Semua Barang")
    print("6. Kembali ke Menu Belanja")

    # Meminta pelanggan untuk memilih menu edit transaksi
    while True:
        try:
            edit_menu = int(input("Pilih menu edit transaksi [1-6]: "))
            break

        except ValueError:
            print('Input yang anda masukkan salah! Input harus berupa angka')

    # Memanggil menu sesuai yang dipilih
    if edit_menu == 1:
        ubah_nama()
    elif edit_menu == 2:
        ubah_jumlah()
    elif edit_menu == 3:
        ubah_harga()
    elif edit_menu == 4:
        hapus_barang()
    elif edit_menu == 5:
        reset_belanja()
    elif edit_menu == 6:
        second_menu()


def second_menu():
    """
    Fungsi yang digunakan untuk menampilkan menu belanja.

    Exceptions
    ----------
    ValueError:
        Jika pengguna memasukkan selain angka (int),
        Maka except akan terjadi dimana akan menyampaikan pesan untuk menginput angka (int)
    """

    # Menampilkan daftar menu belanja
    print("================================")
    print("        **MENU BELANJA**        ")
    print("================================")
    print("1. Mulai Berbelanja")
    print("2. Edit Daftar Belanja")
    print("3. Periksa Daftar Belanja")
    print("4. Pembayaran")
    print("5. Kembali ke Menu Utama")

    # Meminta pelanggan untuk memilih pilihan menu
    while True:
        try:
            menu_kedua = int(input("Pilih menu belanja [1-5]: "))
            break

        except ValueError:
            print('Input yang anda masukkan salah! Input harus berupa angka')

    # Memanggil menu sesuai yang dipilih
    if menu_kedua == 1:
        tambah_barang()
    elif menu_kedua == 2:
        modify_menu()
    elif menu_kedua == 3:
        periksa_belanja()
    elif menu_kedua == 4:
        bayar()
    elif menu_kedua == 5:
        main_menu()


def main_menu():
    """
    Fungsi yang digunakan untuk menampilkan menu utama.

    Exceptions
    ----------
    ValueError:
        Jika pengguna memasukkan selain angka (int),
        Maka except akan terjadi dimana akan menyampaikan pesan untuk menginput angka (int)
    """

    # Menampilkan daftar menu super cashier
    print("================================")
    print("     **MENU SUPER CASHIER**     ")
    print("================================")
    print("1. Belanja\n2. Keluar")

    # Meminta pelanggan untuk memasukkan pilihan menu
    while True:
        try:
            menu_utama = int(input("Pilih menu super cashier [1 atau 2]: "))
            break

        except ValueError:
            print('Input yang anda masukkan salah! Input harus berupa angka')

    # Memanggil menu sesuai yang dipilih
    if menu_utama == 1:
        second_menu()
    elif menu_utama == 2:
        keluar()
        return


# Memanggil menu utama setelah membuat ID transaksi
main_menu()
