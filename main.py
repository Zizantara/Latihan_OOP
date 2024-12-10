from data.mahasiswa import Mahasiswa
from view.input_form import InputForm
from view.mahasiswa import MahasiswaList


def main():
    list_mahasiswa = MahasiswaList()

    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Daftar Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Hapus Data Mahasiswa")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == "1":
            mahasiswa = InputForm.get_input()
            list_mahasiswa.tambah_mahasiswa(mahasiswa)
            print("Data mahasiswa berhasil ditambahkan.")
        elif pilihan == "2":
            print("Daftar Mahasiswa:")
            list_mahasiswa.tampilkan_mahasiswa()
        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
            list_mahasiswa.ubah_data_mahasiswa(nim)
        elif pilihan == "4":
            nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
            list_mahasiswa.hapus_data_mahasiswa(nim)
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
